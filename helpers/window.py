def calculate_center_of_screen_position(screen_width: int, screen_height: int, window_width: int, window_height: int):
    """Calculate the center position of the window based on the screen size and desired window width & height

    Args:
        screen_width (int): screen width (in px)
        screen_height (int): screen height (in px)
        window_width (int): window width (in px)
        window_height (int): window height (in px)

    Returns:
        string: new window position & size
    """
    x_pos = int((screen_width/2) - (window_width/2))
    y_pos = int((screen_height/2) - (window_height/2))

    return f'{window_width}x{window_height}+{x_pos}+{y_pos}'
