
from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from openedx.features.enterprise_support.utils import is_enterprise_learner
from openedx.core.djangoapps.programs.utils import is_user_enrolled_in_program_type


class DemographicsStatusView(APIView):
    """

    """
    authentication_classes = (JwtAuthentication, SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        """
        GET /api/user/v1/accounts/demographics_status

        This is a Web API to determine whether or not we should show Demographics to a learner
        based on their enrollment status.
        """
        user = request.user
        # Is the learner enrolled in MicroBachelors Program or is the learner an Enterprise learner?
        is_user_in_microbachelors_program = is_user_enrolled_in_program_type(user, "microbachelors")
        display_demographics = is_user_in_microbachelors_program or is_enterprise_learner(user)
        return Response({'display': display_demographics})
