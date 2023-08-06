# selenium_simplification
[GitHub](https://github.com/ICreedenI/selenium_simplification) | [PyPI](https://pypi.org/project/selenium-simplification/)  

This is not the final documentation.

Make Selenium simple. Using Selenium in a pythonic style without having to google how to do non-trivial stuff.

Currently implemented:
- driver for Chrome as SeleniumChrome
- easy access to some configurations for Chrome - change the following for hopefully rather obvious effects:
  - headless
  - keep_alive
  - log_level_3
  - muted
  - start_maximized
  - window_position
  - window_size
  - profile
  - log_capabilities
  - page_load_strategy
  - extensions
  - user_agent
- a ton of functions with tasks you might want to perform if you hadn't to google them for half an hour
  - get_titel
  - get_links
  - get_header_h1
  - get_current_scroll_position
  - get_current_scroll_position_of_webelement
  - get_all_attributes_selenium
  - get_all_attributes_bs4
  - get_all_attributes
  - get_parent_of_element
  - highlight
  - perma_highlight
  - undo_highlight
  - get_max_body_scroll_height
  - open_new_tab
  - open_new_window
  - scroll_in_webelement
  - scroll_alt
  - scroll
  - scroll_with_action
  - scroll_with_action_timed
  - scroll_with_action_conditional
  - try_to_do_this_with_timeout
  - process_browser_logs_for_network_events
  - zoom
  - wait_for_element
  - wait_for_element_improvised
  - wait_for_clickable
  - wait_for_visibility
  - action_chain
  - download_src
  - download_blob_src_by_xpath
  - download_all_blob_srcs
  - download_all_img_srcs
  - download_all_video_srcs
  - scroll_in_container
  - trigger_event_webelement
  - is_visible
