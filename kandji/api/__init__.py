# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from kandji.api.audit_log_api import AuditLogApi
    from kandji.api.automated_device_enrollment_integrations_api import AutomatedDeviceEnrollmentIntegrationsApi
    from kandji.api.blueprints_api import BlueprintsApi
    from kandji.api.device_actions_api import DeviceActionsApi
    from kandji.api.device_information_api import DeviceInformationApi
    from kandji.api.device_secrets_api import DeviceSecretsApi
    from kandji.api.library_items_api import LibraryItemsApi
    from kandji.api.prism_api import PrismApi
    from kandji.api.settings_api import SettingsApi
    from kandji.api.tags_api import TagsApi
    from kandji.api.threats_api import ThreatsApi
    from kandji.api.users_api import UsersApi
    from kandji.api.vulnerabilities_api import VulnerabilitiesApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from kandji.api.audit_log_api import AuditLogApi
from kandji.api.automated_device_enrollment_integrations_api import AutomatedDeviceEnrollmentIntegrationsApi
from kandji.api.blueprints_api import BlueprintsApi
from kandji.api.device_actions_api import DeviceActionsApi
from kandji.api.device_information_api import DeviceInformationApi
from kandji.api.device_secrets_api import DeviceSecretsApi
from kandji.api.library_items_api import LibraryItemsApi
from kandji.api.prism_api import PrismApi
from kandji.api.settings_api import SettingsApi
from kandji.api.tags_api import TagsApi
from kandji.api.threats_api import ThreatsApi
from kandji.api.users_api import UsersApi
from kandji.api.vulnerabilities_api import VulnerabilitiesApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
