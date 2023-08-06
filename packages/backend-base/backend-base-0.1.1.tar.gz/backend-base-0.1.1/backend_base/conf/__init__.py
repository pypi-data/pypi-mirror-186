"""
Based on the django.conf module. see: https://github.com/django/django/blob/main/django/conf/__init__.py    # noqa: E501
Settings and configuration for The backend Base.
Read values from the module specified by the BACKEND_CONFIG environment
variable, and then from core.config.settings; see the settings.py
for a list of all possible variables.
"""


import importlib
import types
from typing import Union
from backend_base.exceptions import ImproperlyConfigured
from backend_base.conf import global_settings
from backend_base.utils.environment import get_env
from backend_base.utils.functional import (
    empty,
    LazyObject
)

SETTINGS_MODULE_ENVIRONMENT_VARIABLE = "BACKEND_CONFIG"


class LazySettings(LazyObject):
    """
    A lazy proxy for either global Backend settings or a custom settings object.
    The user can manually configure settings prior to using them. Otherwise,
    BackEnd uses the settings module pointed to by BACKEND_CONFIG.
    """     # noqa: E501

    def _setup(self, name: Union[str, None] = None) -> None:
        """
        Load the settings module pointed to by the environment variable. This
        is used the first time settings are needed, if the user hasn't
        configured settings manually.

        Parameters:
            name Union[str, None]: The name of the setting that triggered
                this load. This is only used to improve the error message.

        Raises:
            ImproperlyConfigured: If the settings module cannot be imported.

        Returns:
            None
        """
        settings_module: Union[str, None] = get_env(
            SETTINGS_MODULE_ENVIRONMENT_VARIABLE,
            'config.settings'
        )
        if not settings_module:
            desc: str = ("setting %s" % name) if name else "settings"
            raise ImproperlyConfigured(
                "Requested %s, but settings are not configured. "
                "You must either define the environment variable %s "
                "or call settings.configure() before accessing settings."
                % (desc, SETTINGS_MODULE_ENVIRONMENT_VARIABLE)
            )

        self._wrapped: Settings = Settings(settings_module)

    def __repr__(self) -> str:
        """
        Return a string representation of this LazySettings instance.

        Returns:
            str: The string representation of this LazySettings instance.
        """
        # Hardcode the class name as otherwise it yields 'Settings'.
        if self._wrapped is empty:
            return '<LazySettings [Unevaluated]>'
        return '<LazySettings "%(settings_module)s">' % {
            'settings_module': self._wrapped.SETTINGS_MODULE,
        }

    def __getattr__(self, name: str) -> object:
        """
        Return the value of a setting and cache it in self.__dict__.

        Parameters:
            name str: The name of the setting to return.

        Returns:
            object: The value of the setting.

        Raises:
            AttributeError: If the setting does not exist.

        """
        if self._wrapped is empty:
            self._setup(name)
        val: object = getattr(self._wrapped, name)

        self.__dict__[name]: object = val
        return val

    def __setattr__(self, name: str, value: object) -> None:
        """
        Set the value of setting. Clear all cached values if _wrapped changes
        (@override_settings does this) or clear single values when set.

        Parameters:
            name str: The name of the setting to set.
            value object: The value to set the setting to.

        Returns:
            None
        """
        if name == '_wrapped':
            self.__dict__.clear()
        else:
            self.__dict__.pop(name, None)
        super().__setattr__(name, value)

    def __delattr__(self, name: str) -> None:
        """
            Delete a setting and clear it from cache if needed.

            Parameters:
                name str: The name of the setting to delete.

            Returns:
                None
        """
        super().__delattr__(name)
        self.__dict__.pop(name, None)

    def configure(
            self,
            default_settings: types.ModuleType = global_settings,
            **options: dict
    ) -> None:
        """
        Called to manually configure the settings. The 'default_settings'
        parameter sets where to retrieve any unspecified values from (its
        argument must support attribute access (__getattr__)).

        Parameters:
            default_settings types.ModuleType: The module to retrieve
                unspecified values from.
            options dict: The settings to set.

        Returns:
            None

        Raises:
            RuntimeError: If the settings are already configured.
        """
        if self._wrapped is not empty:
            raise RuntimeError('Settings already configured.')
        holder: UserSettingsHolder = UserSettingsHolder(default_settings)
        for name, value in options.items():
            if not name.isupper():
                raise TypeError('Setting %r must be uppercase.' % name)
            setattr(holder, name, value)
        self._wrapped: UserSettingsHolder = holder

    @property
    def configured(self) -> bool:
        """
        Return True if the settings have already been configured.

        Returns:
            bool: True if the settings have already been configured.
        """
        return self._wrapped is not empty


class Settings:
    def __init__(
        self,
        settings_module: str,
    ) -> None:
        """
        A settings object, that allows settings to be accessed as properties.

        For example:
            settings = Settings('config.settings')
            print(settings.DEBUG)

        Note:
            All setting names are converted to UPPERCASE.

        Parameters:
            settings_module str: The module to retrieve settings from.

        Returns:
            None

        Raises:
            ImportError: If the settings module cannot be imported.
            TypeError: If the settings module does not support attribute
                access (__getattr__).
        """

        # update this dict from global settings (but only for ALL_CAPS settings)    # noqa: E501
        # make union of all settings from base_global_settings and settings_module
        for setting in dir(global_settings):
            if setting.isupper():
                setattr(
                    self,
                    setting,
                    getattr(
                        global_settings,
                        setting
                    )
                )

        # store the settings module in case someone later cares
        self.SETTINGS_MODULE: str = settings_module

        mod: types.ModuleType = importlib.import_module(self.SETTINGS_MODULE)

        self._explicit_settings: set = set()
        for setting in dir(mod):
            if setting.isupper():
                setting_value: object = getattr(mod, setting)
                setattr(self, setting, setting_value)
                self._explicit_settings.add(setting)

    def is_overridden(self, setting: str) -> bool:
        """
        Return True if the setting is overridden.

        Parameters:
            setting str: The name of the setting to check.

        Returns:
            bool: True if the setting is overridden.
        """
        return setting in self._explicit_settings

    def __repr__(self) -> str:
        """
        Return the string representation of this Settings instance.

        Returns:
            str: The string representation of this Settings instance.
        """
        return '<%(cls)s "%(settings_module)s">' % {
            'cls': self.__class__.__name__,
            'settings_module': self.SETTINGS_MODULE,
        }


class UserSettingsHolder:
    """Holder for user configured settings."""
    # SETTINGS_MODULE doesn't make much sense in the manually configured
    # (standalone) case.
    SETTINGS_MODULE = None

    def __init__(self, default_settings: types.ModuleType) -> None:
        """
        Requests for configuration variables not in this class are satisfied
        from the module specified in default_settings (if possible).

        Parameters:
            default_settings types.ModuleType: The module to retrieve
                unspecified values from.

        Returns:
            None
        """
        self.__dict__['_deleted']: set = set()
        self.default_settings: types.ModuleType = default_settings

    def __getattr__(self, name: str) -> object:
        """
        Return the value of a setting and cache it in self.__dict__.

        Parameters:
            name str: The name of the setting to return.

        Returns:
            object: The value of the setting.

        Raises:
            AttributeError: If the setting does not exist.
        """
        if not name.isupper() or name in self._deleted:
            raise AttributeError
        return getattr(self.default_settings, name)

    def __setattr__(self, name: str, value: object) -> None:
        """
        Set a setting and clear it from cache if needed.

        Parameters:
            name str: The name of the setting to set.
            value object: The value to set the setting to.

        Returns:
            None
        """
        self._deleted.discard(name)
        super().__setattr__(name, value)

    def __delattr__(self, name: str) -> None:
        """
        Delete a setting and clear it from cache if needed.

        Parameters:
            name str: The name of the setting to delete.

        Returns:
            None
        """

        self._deleted.add(name)
        if hasattr(self, name):
            super().__delattr__(name)

    def __dir__(self) -> list:
        """
        Return a list of all settings.

        Returns:
            list: A list of all settings.
        """
        return sorted(
            s for s in [*self.__dict__, *dir(self.default_settings)]
            if s not in self._deleted
        )

    def is_overridden(self, setting: str) -> bool:
        """
        Return True if the setting is overridden.

        Parameters:
            setting str: The name of the setting to check.

        Returns:
            bool: True if the setting is overridden.
        """

        deleted = (setting in self._deleted)
        set_locally: bool = (setting in self.__dict__)
        set_on_default: bool = getattr(
            self.default_settings,
            'is_overridden',
            lambda s: False
        )(setting)
        return deleted or set_locally or set_on_default

    def __repr__(self) -> str:
        """
        Return the string representation of this UserSettingsHolder instance.

        Returns:
            str: The string representation of this UserSettingsHolder instance.
        """
        return '<%(cls)s>' % {
            'cls': self.__class__.__name__,
        }


settings: LazySettings = LazySettings()
