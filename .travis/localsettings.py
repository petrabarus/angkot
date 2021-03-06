DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'angkot',
        'USER': 'angkot',
        'PASSWORD': 'angkot',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# GOOGLE_ANALYTICS_IGNORE = False
# GOOGLE_ANALYTICS_ID = ''
# GOOGLE_ANALYTICS_HOST = ''
# MAPBOX_KEY = ''
# BING_MAPS_KEY = ''

# USERVOICE_CODE = '''
# <!-- UserVoice JavaScript SDK (only needed once on a page) -->
# <script>(function(){var uv=document.createElement('script');uv.type='text/javascript';uv.async=true;uv.src='//widget.uservoice.com/USER-VOICE-ID.js';var s=document.getElementsByTagName('script')[0];s.parentNode.insertBefore(uv,s)})()</script>
# 
# <!-- A tab to launch the Classic Widget -->
# <script>
# UserVoice = window.UserVoice || [];
# UserVoice.push(['showTab', 'classic_widget', {
#   mode: 'feedback',
#   primary_color: '#cc6d00',
#   link_color: '#007dbf',
#   forum_id: 217173,
#   tab_label: 'Feedback',
#   tab_color: '#cc6d00',
#   tab_position: 'middle-right',
#   tab_inverted: false
# }]);
# </script>
# '''

ACCOUNT_USERNAME_PREFIX = 'user'
ANGKOT_CONTRIBUTOR_TERMS_URL = ''
ANGKOT_PRIVACY_POLICY_URL = ''

# Authentication keys from providers

GOOGLE_OAUTH2_CLIENT_ID = ''
GOOGLE_OAUTH2_CLIENT_SECRET = ''

FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''

TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''

