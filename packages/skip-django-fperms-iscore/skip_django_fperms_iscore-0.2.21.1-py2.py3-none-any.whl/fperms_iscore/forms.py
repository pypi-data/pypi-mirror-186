from django.core.exceptions import ValidationError
from django.utils.translation import ugettext
from django.utils.translation import ugettext_lazy as _

from fperms.base import Group
from fperms.conf import settings as fperms_settings
from fperms.models import Perm

from is_core.forms.models import SmartModelForm, ModelMultipleChoiceField


def max_or_zero(*values):
    return max(0, 0, *values)


def get_all_group_pks(groups):
    pks = set()
    for group in groups:
        pks.add(group.pk)
        pks.update(get_all_group_pks(group.fgroups.all()))
    return pks


def get_max_bottom_level(group):
    return 1 + max_or_zero(*[get_max_bottom_level(subgroup) for subgroup in group.fgroups.all()])


def get_max_top_level(group):
    return 1 + max_or_zero(*[get_max_top_level(supgroup) for supgroup in group.parents.all()])


def get_group_level(group, subgroups):
    level = 0
    if group.pk:
        level = get_max_top_level(group) - 1
    return level + max_or_zero(*[get_max_bottom_level(subgroup) for subgroup in subgroups])


class PermsFormMixin(SmartModelForm):

    fperms = ModelMultipleChoiceField(label=_('permissions'), queryset=Perm.objects.all(), required=False)

    def _init_fperms(self, field):
        if self.instance.pk:
            field.initial = self.instance.fperms.values_list('pk', flat=True)

    def _post_save(self, obj):
        super()._post_save(obj)
        if 'fperms' in self.cleaned_data:
            obj.fperms.set(self.cleaned_data['fperms'])


class GroupsFormMixin(SmartModelForm):

    fgroups = ModelMultipleChoiceField(label=_('permission groups'), queryset=Group.objects.all(), required=False)

    def _init_fperms(self, field):
        if self.instance.pk:
            field.initial = self.instance.fgroups.values_list('pk', flat=True)

    def _post_save(self, obj):
        super()._post_save(obj)
        if 'fgroups' in self.cleaned_data:
            obj.fgroups.set(self.cleaned_data['fgroups'])


class GroupForm(SmartModelForm):

    fgroups = ModelMultipleChoiceField(label=_('subgroups'), queryset=Group.objects.all(), required=False)

    def clean_fgroups(self):
        fgroups = self.cleaned_data['fgroups']

        if self.instance.pk in get_all_group_pks(fgroups):
            raise ValidationError(ugettext('Cycles are not allowed'))

        if get_group_level(self.instance, fgroups) > fperms_settings.PERM_GROUP_MAX_LEVEL:
            raise ValidationError(ugettext('Max group level was reached'))

        return fgroups
