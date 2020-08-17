btn_closed_promo_banner = "//i[contains(@class,'popupCloseIcon')]"
btn_closed_news_video = "//div[@id='closeBtn']"


def get_banner_selector_list() -> list:
    return [btn_closed_promo_banner].copy()