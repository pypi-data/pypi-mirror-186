def is_billing_rates_installed():
    from NEMO_user_details.templatetags.user_details_tags import app_installed

    return app_installed("NEMO_billing.rates")
