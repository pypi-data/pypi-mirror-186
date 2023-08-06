from django.core.management.base import BaseCommand
from django.db.models import F, Value
from django.db.models.functions import Concat
from django.utils.translation import ugettext

from chamber.shortcuts import get_object_or_none
from chamber.utils.decorators import translation_activate_block

from fperms import get_perm_model

from fperms_iscore import enums
from fperms_iscore.permissions import permissions


Perm = get_perm_model()


class Command(BaseCommand):

    help = 'Synchronize fperms permissions with database'

    def add_arguments(self, parser):
        parser.add_argument('--clean-obsolete', action='store_true', dest='clean_obsolete', default=False,
                            help='Remove obsolete permissions if it was used.')

    @translation_activate_block
    def handle(self, **options):
        self.stdout.write('Syncing permissions')
        updated_permission_pks = set()
        created_permission_pks = set()
        unchanged_permissions_pks = set()
        for permission in permissions.values():
            perm = get_object_or_none(
                Perm, type=enums.PERM_TYPE_CORE, codename=permission.name, name=permission.verbose_name
            )
            if perm:
                unchanged_permissions_pks.add(perm.pk)
            else:
                perm, created = Perm.objects.update_or_create(
                    type=enums.PERM_TYPE_CORE,
                    codename=permission.name,
                    defaults={
                        'name': permission.verbose_name
                    }
                )
                if created:
                    created_permission_pks.add(perm.pk)
                else:
                    updated_permission_pks.add(perm.pk)
        self.stdout.write(' Updated: {}'.format(len(updated_permission_pks)))
        self.stdout.write(' Created: {}'.format(len(created_permission_pks)))

        self.stdout.write('Removing unused permissions')
        nonexistent_unused_permissions_qs = Perm.objects.exclude(
            pk__in=updated_permission_pks | created_permission_pks | unchanged_permissions_pks
        ).filter(
            fgroups__isnull=True, users__isnull=True
        )
        count = nonexistent_unused_permissions_qs.count()
        nonexistent_unused_permissions_qs.delete()
        self.stdout.write(' Removed: {}'.format(count))

        nonexistent_used_permissions_qs = Perm.objects.exclude(
            pk__in=updated_permission_pks | created_permission_pks | unchanged_permissions_pks
        )
        if options.get('clean_obsolete'):
            self.stdout.write('Removing used permissions')
            count = nonexistent_used_permissions_qs.count()
            nonexistent_used_permissions_qs.delete()
            self.stdout.write(' Removed: {}'.format(count))
        elif nonexistent_used_permissions_qs.exists():
            self.stderr.write(
                f'Found used obsolete permissions ({nonexistent_used_permissions_qs.count()}), '
                f'run command with "--clean-obsolete" parameter for cleaning'
            )
            obsolete_string = ugettext(' (obsolete)')
            nonexistent_used_permissions_qs.exclude(
                name__endswith=obsolete_string
            ).update(
                name=Concat(F('name'), Value(obsolete_string))
            )
