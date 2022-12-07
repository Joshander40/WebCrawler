import PySimpleGUI as sg

def create(result_list_array, headings):

  results_list_window_layout= [
      [sg.Table(
        values=result_list_array,
        headings=headings,
        max_col_width=50,
        auto_size_columns=True,
        display_row_numbers=True,
        justification='left',
        num_rows=10,
        key="-PTABLE-",
        enable_events = True,
        row_height=35
      )]
  ]

  results_list_window = sg.Window("Results of selected link", 
  results_list_window_layout, modal=True)

  while True:
      event, values = results_list_window.read()
      if event == "Exit" or event == sg.WIN_CLOSED:
        break
  
  results_list_window.close()