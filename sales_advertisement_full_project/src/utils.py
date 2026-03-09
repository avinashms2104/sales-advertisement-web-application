def calculate_conversion_rate(conversions, clicks):
    if clicks == 0:
        return 0
    return conversions / clicks