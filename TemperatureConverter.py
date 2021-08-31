import tkinter as tk

# Root window
window = tk.Tk()

# Labels
user_input_label = tk.Label(text="Please enter the temperature you wish to convert")
user_input_label.pack()
user_input_field = tk.Entry(window)
user_input_field.pack()

# A functin that converts celcius to farenheit and vice-versa
# Updates the GUI such that the result is displayed in a label element
def temperature_converter():
    user_input = user_input_field.get().lower()
    try:
        if "f" in user_input:
            temp_f = float(user_input.replace("f", ""))
            temp_c = ((temp_f - 32) * 5) / 9
            result = tk.Label(text=f"Result:-  {round(temp_c, 3)}°C")
            result.pack()
        elif "c" in user_input:
            temp_c = float(user_input.replace("c", ""))
            temp_f = (1.8 * temp_c) + 32
            result = tk.Label(text=f"Result:-  {round(temp_f, 3)}°F")
            result.pack()
        else:
            print("Make sure to include 'c' for celsius or 'f' for farenheit at the end of the input")
            print("bruh")
    except:
        print("Error occured, please re-run program")
        
submit_button = tk.Button(text="Submit", command = temperature_converter)


submit_button.pack()
window.mainloop()
