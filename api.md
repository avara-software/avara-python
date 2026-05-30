# Shared Types

```python
from avara.types import (
    APIKeyReference,
    AssignableUserLevel,
    ClinicRole,
    ExpressCustomerReference,
    InvitationExpiredFilter,
    InvitationStatus,
    InvitedSource,
    Severity,
    UserLevel,
    UserReference,
)
```

# AutoScribe

Types:

```python
from avara.types import (
    HeightUnit,
    ReportStatus,
    Sex,
    StudyReportMetadata,
    StudyReportStatus,
    WeightUnit,
)
```

## Studies

Types:

```python
from avara.types.auto_scribe import (
    PriorReport,
    ReportIDWithStatus,
    StudyCreateResponse,
    StudyRetrieveResponse,
    StudyUpdateResponse,
    StudyListResponse,
    StudyCancelResponse,
    StudyRerouteURLResponse,
    StudyRetrieveByUidResponse,
    StudyUncancelResponse,
    StudyViewerOnlyRerouteURLResponse,
)
```

Methods:

- <code title="post /v1/autoScribe/studies">client.auto_scribe.studies.<a href="./src/avara/resources/auto_scribe/studies.py">create</a>(\*\*<a href="src/avara/types/auto_scribe/study_create_params.py">params</a>) -> <a href="./src/avara/types/auto_scribe/study_create_response.py">StudyCreateResponse</a></code>
- <code title="get /v1/autoScribe/studies/{studyId}">client.auto_scribe.studies.<a href="./src/avara/resources/auto_scribe/studies.py">retrieve</a>(study_id) -> <a href="./src/avara/types/auto_scribe/study_retrieve_response.py">StudyRetrieveResponse</a></code>
- <code title="patch /v1/autoScribe/studies/{studyId}">client.auto_scribe.studies.<a href="./src/avara/resources/auto_scribe/studies.py">update</a>(study_id, \*\*<a href="src/avara/types/auto_scribe/study_update_params.py">params</a>) -> <a href="./src/avara/types/auto_scribe/study_update_response.py">StudyUpdateResponse</a></code>
- <code title="get /v1/autoScribe/studies">client.auto_scribe.studies.<a href="./src/avara/resources/auto_scribe/studies.py">list</a>(\*\*<a href="src/avara/types/auto_scribe/study_list_params.py">params</a>) -> <a href="./src/avara/types/auto_scribe/study_list_response.py">SyncCursorStudies[StudyListResponse]</a></code>
- <code title="post /v1/autoScribe/studies/cancel">client.auto_scribe.studies.<a href="./src/avara/resources/auto_scribe/studies.py">cancel</a>(\*\*<a href="src/avara/types/auto_scribe/study_cancel_params.py">params</a>) -> <a href="./src/avara/types/auto_scribe/study_cancel_response.py">StudyCancelResponse</a></code>
- <code title="post /v1/autoScribe/studies/reroute-url">client.auto_scribe.studies.<a href="./src/avara/resources/auto_scribe/studies.py">reroute_url</a>(\*\*<a href="src/avara/types/auto_scribe/study_reroute_url_params.py">params</a>) -> <a href="./src/avara/types/auto_scribe/study_reroute_url_response.py">StudyRerouteURLResponse</a></code>
- <code title="get /v1/autoScribe/studies/by-uid/{studyInstanceUid}">client.auto_scribe.studies.<a href="./src/avara/resources/auto_scribe/studies.py">retrieve_by_uid</a>(study_instance_uid) -> <a href="./src/avara/types/auto_scribe/study_retrieve_by_uid_response.py">StudyRetrieveByUidResponse</a></code>
- <code title="post /v1/autoScribe/studies/uncancel">client.auto_scribe.studies.<a href="./src/avara/resources/auto_scribe/studies.py">uncancel</a>(\*\*<a href="src/avara/types/auto_scribe/study_uncancel_params.py">params</a>) -> <a href="./src/avara/types/auto_scribe/study_uncancel_response.py">StudyUncancelResponse</a></code>
- <code title="post /v1/autoScribe/studies/viewer-only-reroute-url">client.auto_scribe.studies.<a href="./src/avara/resources/auto_scribe/studies.py">viewer_only_reroute_url</a>(\*\*<a href="src/avara/types/auto_scribe/study_viewer_only_reroute_url_params.py">params</a>) -> <a href="./src/avara/types/auto_scribe/study_viewer_only_reroute_url_response.py">StudyViewerOnlyRerouteURLResponse</a></code>

## Users

Types:

```python
from avara.types.auto_scribe import (
    UserRetrieveResponse,
    UserUpdateResponse,
    UserListResponse,
    UserInviteResponse,
    UserReactivateResponse,
    UserRevokeAccessResponse,
)
```

Methods:

- <code title="get /v1/autoScribe/users/{userId}">client.auto_scribe.users.<a href="./src/avara/resources/auto_scribe/users/users.py">retrieve</a>(user_id) -> <a href="./src/avara/types/auto_scribe/user_retrieve_response.py">UserRetrieveResponse</a></code>
- <code title="patch /v1/autoScribe/users/{userId}">client.auto_scribe.users.<a href="./src/avara/resources/auto_scribe/users/users.py">update</a>(user_id, \*\*<a href="src/avara/types/auto_scribe/user_update_params.py">params</a>) -> <a href="./src/avara/types/auto_scribe/user_update_response.py">UserUpdateResponse</a></code>
- <code title="get /v1/autoScribe/users">client.auto_scribe.users.<a href="./src/avara/resources/auto_scribe/users/users.py">list</a>(\*\*<a href="src/avara/types/auto_scribe/user_list_params.py">params</a>) -> <a href="./src/avara/types/auto_scribe/user_list_response.py">SyncCursorUsers[UserListResponse]</a></code>
- <code title="post /v1/autoScribe/users">client.auto_scribe.users.<a href="./src/avara/resources/auto_scribe/users/users.py">invite</a>(\*\*<a href="src/avara/types/auto_scribe/user_invite_params.py">params</a>) -> <a href="./src/avara/types/auto_scribe/user_invite_response.py">UserInviteResponse</a></code>
- <code title="post /v1/autoScribe/users/reactivate">client.auto_scribe.users.<a href="./src/avara/resources/auto_scribe/users/users.py">reactivate</a>(\*\*<a href="src/avara/types/auto_scribe/user_reactivate_params.py">params</a>) -> <a href="./src/avara/types/auto_scribe/user_reactivate_response.py">UserReactivateResponse</a></code>
- <code title="post /v1/autoScribe/users/revoke-access">client.auto_scribe.users.<a href="./src/avara/resources/auto_scribe/users/users.py">revoke_access</a>(\*\*<a href="src/avara/types/auto_scribe/user_revoke_access_params.py">params</a>) -> <a href="./src/avara/types/auto_scribe/user_revoke_access_response.py">UserRevokeAccessResponse</a></code>

### Invitations

Types:

```python
from avara.types.auto_scribe.users import (
    InvitationRetrieveResponse,
    InvitationUpdateResponse,
    InvitationListResponse,
    InvitationRevokeResponse,
)
```

Methods:

- <code title="get /v1/autoScribe/users/invitations/{invitationId}">client.auto_scribe.users.invitations.<a href="./src/avara/resources/auto_scribe/users/invitations.py">retrieve</a>(invitation_id) -> <a href="./src/avara/types/auto_scribe/users/invitation_retrieve_response.py">InvitationRetrieveResponse</a></code>
- <code title="patch /v1/autoScribe/users/invitations/{invitationId}">client.auto_scribe.users.invitations.<a href="./src/avara/resources/auto_scribe/users/invitations.py">update</a>(invitation_id, \*\*<a href="src/avara/types/auto_scribe/users/invitation_update_params.py">params</a>) -> <a href="./src/avara/types/auto_scribe/users/invitation_update_response.py">InvitationUpdateResponse</a></code>
- <code title="get /v1/autoScribe/users/invitations">client.auto_scribe.users.invitations.<a href="./src/avara/resources/auto_scribe/users/invitations.py">list</a>(\*\*<a href="src/avara/types/auto_scribe/users/invitation_list_params.py">params</a>) -> <a href="./src/avara/types/auto_scribe/users/invitation_list_response.py">SyncCursorInvitations[InvitationListResponse]</a></code>
- <code title="post /v1/autoScribe/users/invitations/revoke">client.auto_scribe.users.invitations.<a href="./src/avara/resources/auto_scribe/users/invitations.py">revoke</a>(\*\*<a href="src/avara/types/auto_scribe/users/invitation_revoke_params.py">params</a>) -> <a href="./src/avara/types/auto_scribe/users/invitation_revoke_response.py">InvitationRevokeResponse</a></code>

## Reports

Types:

```python
from avara.types.auto_scribe import (
    ReportListResponse,
    ReportAddendumResponse,
    ReportCancelAddendumResponse,
    ReportPdfResponse,
    ReportTextResponse,
)
```

Methods:

- <code title="get /v1/autoScribe/reports">client.auto_scribe.reports.<a href="./src/avara/resources/auto_scribe/reports.py">list</a>(\*\*<a href="src/avara/types/auto_scribe/report_list_params.py">params</a>) -> <a href="./src/avara/types/auto_scribe/report_list_response.py">ReportListResponse</a></code>
- <code title="post /v1/autoScribe/reports/{reportId}/addendum">client.auto_scribe.reports.<a href="./src/avara/resources/auto_scribe/reports.py">addendum</a>(report_id) -> <a href="./src/avara/types/auto_scribe/report_addendum_response.py">ReportAddendumResponse</a></code>
- <code title="post /v1/autoScribe/reports/{reportId}/cancel-addendum">client.auto_scribe.reports.<a href="./src/avara/resources/auto_scribe/reports.py">cancel_addendum</a>(report_id) -> <a href="./src/avara/types/auto_scribe/report_cancel_addendum_response.py">ReportCancelAddendumResponse</a></code>
- <code title="get /v1/autoScribe/reports/pdf">client.auto_scribe.reports.<a href="./src/avara/resources/auto_scribe/reports.py">pdf</a>(\*\*<a href="src/avara/types/auto_scribe/report_pdf_params.py">params</a>) -> <a href="./src/avara/types/auto_scribe/report_pdf_response.py">ReportPdfResponse</a></code>
- <code title="get /v1/autoScribe/reports/text">client.auto_scribe.reports.<a href="./src/avara/resources/auto_scribe/reports.py">text</a>(\*\*<a href="src/avara/types/auto_scribe/report_text_params.py">params</a>) -> <a href="./src/avara/types/auto_scribe/report_text_response.py">ReportTextResponse</a></code>

# Viewer

Types:

```python
from avara.types import StudyViewerStatus
```

## Studies

Types:

```python
from avara.types.viewer import (
    StudyCreateResponse,
    StudyRetrieveResponse,
    StudyUpdateResponse,
    StudyListResponse,
    StudyCancelResponse,
    StudyRerouteURLResponse,
    StudyRetrieveByUidResponse,
    StudyUncancelResponse,
)
```

Methods:

- <code title="post /v1/viewer/studies">client.viewer.studies.<a href="./src/avara/resources/viewer/studies.py">create</a>(\*\*<a href="src/avara/types/viewer/study_create_params.py">params</a>) -> <a href="./src/avara/types/viewer/study_create_response.py">StudyCreateResponse</a></code>
- <code title="get /v1/viewer/studies/{studyId}">client.viewer.studies.<a href="./src/avara/resources/viewer/studies.py">retrieve</a>(study_id) -> <a href="./src/avara/types/viewer/study_retrieve_response.py">StudyRetrieveResponse</a></code>
- <code title="patch /v1/viewer/studies/{studyId}">client.viewer.studies.<a href="./src/avara/resources/viewer/studies.py">update</a>(study_id, \*\*<a href="src/avara/types/viewer/study_update_params.py">params</a>) -> <a href="./src/avara/types/viewer/study_update_response.py">StudyUpdateResponse</a></code>
- <code title="get /v1/viewer/studies">client.viewer.studies.<a href="./src/avara/resources/viewer/studies.py">list</a>(\*\*<a href="src/avara/types/viewer/study_list_params.py">params</a>) -> <a href="./src/avara/types/viewer/study_list_response.py">SyncCursorStudies[StudyListResponse]</a></code>
- <code title="post /v1/viewer/studies/cancel">client.viewer.studies.<a href="./src/avara/resources/viewer/studies.py">cancel</a>(\*\*<a href="src/avara/types/viewer/study_cancel_params.py">params</a>) -> <a href="./src/avara/types/viewer/study_cancel_response.py">StudyCancelResponse</a></code>
- <code title="post /v1/viewer/studies/reroute-url">client.viewer.studies.<a href="./src/avara/resources/viewer/studies.py">reroute_url</a>(\*\*<a href="src/avara/types/viewer/study_reroute_url_params.py">params</a>) -> <a href="./src/avara/types/viewer/study_reroute_url_response.py">StudyRerouteURLResponse</a></code>
- <code title="get /v1/viewer/studies/by-uid/{studyInstanceUid}">client.viewer.studies.<a href="./src/avara/resources/viewer/studies.py">retrieve_by_uid</a>(study_instance_uid) -> <a href="./src/avara/types/viewer/study_retrieve_by_uid_response.py">StudyRetrieveByUidResponse</a></code>
- <code title="post /v1/viewer/studies/uncancel">client.viewer.studies.<a href="./src/avara/resources/viewer/studies.py">uncancel</a>(\*\*<a href="src/avara/types/viewer/study_uncancel_params.py">params</a>) -> <a href="./src/avara/types/viewer/study_uncancel_response.py">StudyUncancelResponse</a></code>

## Users

Types:

```python
from avara.types.viewer import (
    UserRetrieveResponse,
    UserUpdateResponse,
    UserListResponse,
    UserInviteResponse,
    UserReactivateResponse,
    UserRevokeAccessResponse,
)
```

Methods:

- <code title="get /v1/viewer/users/{userId}">client.viewer.users.<a href="./src/avara/resources/viewer/users/users.py">retrieve</a>(user_id) -> <a href="./src/avara/types/viewer/user_retrieve_response.py">UserRetrieveResponse</a></code>
- <code title="patch /v1/viewer/users/{userId}">client.viewer.users.<a href="./src/avara/resources/viewer/users/users.py">update</a>(user_id, \*\*<a href="src/avara/types/viewer/user_update_params.py">params</a>) -> <a href="./src/avara/types/viewer/user_update_response.py">UserUpdateResponse</a></code>
- <code title="get /v1/viewer/users">client.viewer.users.<a href="./src/avara/resources/viewer/users/users.py">list</a>(\*\*<a href="src/avara/types/viewer/user_list_params.py">params</a>) -> <a href="./src/avara/types/viewer/user_list_response.py">SyncCursorUsers[UserListResponse]</a></code>
- <code title="post /v1/viewer/users">client.viewer.users.<a href="./src/avara/resources/viewer/users/users.py">invite</a>(\*\*<a href="src/avara/types/viewer/user_invite_params.py">params</a>) -> <a href="./src/avara/types/viewer/user_invite_response.py">UserInviteResponse</a></code>
- <code title="post /v1/viewer/users/reactivate">client.viewer.users.<a href="./src/avara/resources/viewer/users/users.py">reactivate</a>(\*\*<a href="src/avara/types/viewer/user_reactivate_params.py">params</a>) -> <a href="./src/avara/types/viewer/user_reactivate_response.py">UserReactivateResponse</a></code>
- <code title="post /v1/viewer/users/revoke-access">client.viewer.users.<a href="./src/avara/resources/viewer/users/users.py">revoke_access</a>(\*\*<a href="src/avara/types/viewer/user_revoke_access_params.py">params</a>) -> <a href="./src/avara/types/viewer/user_revoke_access_response.py">UserRevokeAccessResponse</a></code>

### Invitations

Types:

```python
from avara.types.viewer.users import (
    InvitationRetrieveResponse,
    InvitationUpdateResponse,
    InvitationListResponse,
    InvitationRevokeResponse,
)
```

Methods:

- <code title="get /v1/viewer/users/invitations/{invitationId}">client.viewer.users.invitations.<a href="./src/avara/resources/viewer/users/invitations.py">retrieve</a>(invitation_id) -> <a href="./src/avara/types/viewer/users/invitation_retrieve_response.py">InvitationRetrieveResponse</a></code>
- <code title="patch /v1/viewer/users/invitations/{invitationId}">client.viewer.users.invitations.<a href="./src/avara/resources/viewer/users/invitations.py">update</a>(invitation_id, \*\*<a href="src/avara/types/viewer/users/invitation_update_params.py">params</a>) -> <a href="./src/avara/types/viewer/users/invitation_update_response.py">InvitationUpdateResponse</a></code>
- <code title="get /v1/viewer/users/invitations">client.viewer.users.invitations.<a href="./src/avara/resources/viewer/users/invitations.py">list</a>(\*\*<a href="src/avara/types/viewer/users/invitation_list_params.py">params</a>) -> <a href="./src/avara/types/viewer/users/invitation_list_response.py">SyncCursorInvitations[InvitationListResponse]</a></code>
- <code title="post /v1/viewer/users/invitations/revoke">client.viewer.users.invitations.<a href="./src/avara/resources/viewer/users/invitations.py">revoke</a>(\*\*<a href="src/avara/types/viewer/users/invitation_revoke_params.py">params</a>) -> <a href="./src/avara/types/viewer/users/invitation_revoke_response.py">InvitationRevokeResponse</a></code>

# Express

Types:

```python
from avara.types import (
    ExpressCreateResponse,
    ExpressRetrieveResponse,
    ExpressUpdateResponse,
    ExpressListResponse,
    ExpressDeactivateResponse,
    ExpressReactivateResponse,
)
```

Methods:

- <code title="post /v1/express">client.express.<a href="./src/avara/resources/express/express.py">create</a>(\*\*<a href="src/avara/types/express_create_params.py">params</a>) -> <a href="./src/avara/types/express_create_response.py">ExpressCreateResponse</a></code>
- <code title="get /v1/express/{expressCustomerId}">client.express.<a href="./src/avara/resources/express/express.py">retrieve</a>(express_customer_id) -> <a href="./src/avara/types/express_retrieve_response.py">ExpressRetrieveResponse</a></code>
- <code title="patch /v1/express/{expressCustomerId}">client.express.<a href="./src/avara/resources/express/express.py">update</a>(express_customer_id, \*\*<a href="src/avara/types/express_update_params.py">params</a>) -> <a href="./src/avara/types/express_update_response.py">ExpressUpdateResponse</a></code>
- <code title="get /v1/express">client.express.<a href="./src/avara/resources/express/express.py">list</a>(\*\*<a href="src/avara/types/express_list_params.py">params</a>) -> <a href="./src/avara/types/express_list_response.py">SyncCursorExpressCustomers[ExpressListResponse]</a></code>
- <code title="post /v1/express/{expressCustomerId}/deactivate">client.express.<a href="./src/avara/resources/express/express.py">deactivate</a>(express_customer_id) -> <a href="./src/avara/types/express_deactivate_response.py">ExpressDeactivateResponse</a></code>
- <code title="post /v1/express/{expressCustomerId}/reactivate">client.express.<a href="./src/avara/resources/express/express.py">reactivate</a>(express_customer_id) -> <a href="./src/avara/types/express_reactivate_response.py">ExpressReactivateResponse</a></code>

## Users

Types:

```python
from avara.types.express import UserAddResponse, UserRemoveResponse
```

Methods:

- <code title="post /v1/express/{expressCustomerId}/users">client.express.users.<a href="./src/avara/resources/express/users.py">add</a>(express_customer_id, \*\*<a href="src/avara/types/express/user_add_params.py">params</a>) -> <a href="./src/avara/types/express/user_add_response.py">UserAddResponse</a></code>
- <code title="delete /v1/express/{expressCustomerId}/users">client.express.users.<a href="./src/avara/resources/express/users.py">remove</a>(express_customer_id, \*\*<a href="src/avara/types/express/user_remove_params.py">params</a>) -> <a href="./src/avara/types/express/user_remove_response.py">UserRemoveResponse</a></code>

# Webhooks

Types:

```python
from avara.types import (
    ReportDeliveredEvent,
    ReportDeliveredResponse,
    StudyAccessRequestedEvent,
    StudyAccessRequestedResponse,
    WebhookEvent,
    UnsafeUnwrapWebhookEvent,
    UnwrapWebhookEvent,
)
```
