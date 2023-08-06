
class AppKeys:
    """
    Store application keys in one place.
    
    :var: GITHUB_TOKEN
    :var: VAULT_ADDR
    :var: IMAGE_API_RELATIVE_URL
    :var: IMAGE_ENHANCE_API_RELATIVE_URL
    """

    GITHUB_TOKEN = 'GITHUB_TOKEN'
    VAULT_ADDR = 'VAULT_ADDR'
    IMAGE_API_RELATIVE_URL = 'image_api_relative_url'
    IMAGE_ENHANCE_API_RELATIVE_URL = 'image_enhance_api_relative_url'


class ImageVariants:
    """
    Store allowed values for the image variant.
    
    :var: STANDARD
    :var: THUMBNAIL
    :var: ORIGINAL
    :var: DEFAULT
    """

    STANDARD = 'standard'
    THUMBNAIL = 'thumbnail'
    ORIGINAL = 'original'
    DEFAULT = STANDARD
