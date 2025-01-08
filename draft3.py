import google.generativeai as genai
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

# Configure the Gemini Gen AI API
genai.configure(api_key="AIzaSyBtYB7Da8VNN8paGnsA2fSNx69UqYfTXao")  # Replace with your API key

# Function to send a message to the AI and display the response
def send_message():
    user_message = user_input.get()
    if not user_message:
        messagebox.showwarning("Input Error", "Please enter a message.")
        return

    # Display user's message in the chat
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"You: {user_message}\n", ("user",))
    chat_display.config(state=tk.DISABLED)
    chat_display.see(tk.END)
    user_input.set("")  # Clear the input field

    try:
        # Send the message to Gemini AI
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_message)
        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, f"Gemini AI: {response.text}\n", ("ai",))
        chat_display.config(state=tk.DISABLED)
        chat_display.see(tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to switch to dark mode
def enable_dark_mode():
    root.configure(bg="#2c3e50")
    header_label.configure(bg="#1a252f", fg="#ffffff")
    chat_frame.configure(bg="#2c3e50")
    chat_display.configure(bg="#34495e", fg="#ecf0f1")
    input_frame.configure(bg="#2c3e50")
    input_entry.configure(style="Dark.TEntry")
    send_button.configure(style="Dark.TButton")

# Function to switch to light mode
def enable_light_mode():
    root.configure(bg="#e0f7fa")
    header_label.configure(bg="#00796b", fg="#ffffff")
    chat_frame.configure(bg="#ffffff")
    chat_display.configure(bg="#fafafa", fg="#333333")
    input_frame.configure(bg="#e0f7fa")
    input_entry.configure(style="Light.TEntry")
    send_button.configure(style="Light.TButton")

# Create the main GUI window
root = tk.Tk()
root.title("Gemini AI Chatbot")
root.geometry("800x600")
root.configure(bg="#e0f7fa")

# Header
header_label = tk.Label(root, text="Gemini AI Chatbot", font=("Poppins", 30, "bold"), fg="#ffffff", bg="#00796b", pady=10)
header_label.pack(fill=tk.X)

# Chat Display Frame
chat_frame = tk.Frame(root, bg="#ffffff", padx=10, pady=10)
chat_frame.pack(expand=True, fill=tk.BOTH)

# Chat Display with Watermark
chat_display = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, bg="#fafafa", fg="#333333", font=("Poppins", 12), state=tk.DISABLED)
chat_display.tag_configure("user", foreground="#2196f3")
chat_display.tag_configure("ai", foreground="#e91e63")
chat_display.insert("1.0", "\n\n\n             Ask me anything....", ("watermark",))
chat_display.tag_configure("watermark", foreground="#b0bec5", font=("Poppins", 20, "italic"))
chat_display.pack(expand=True, fill=tk.BOTH)

# User Input Frame
input_frame = tk.Frame(root, bg="#e0f7fa", pady=10)
input_frame.pack(fill=tk.X)

user_input = tk.StringVar()
input_entry = ttk.Entry(input_frame, textvariable=user_input, font=("Poppins", 14))
input_entry.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
input_entry.bind("<Return>", lambda event: send_message())

send_button = ttk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=10)

# Dark Mode and Light Mode Buttons
mode_frame = tk.Frame(root, bg="#e0f7fa", pady=10)
mode_frame.pack(fill=tk.X)

dark_mode_button = ttk.Button(mode_frame, text="Dark Mode", command=enable_dark_mode)
dark_mode_button.pack(side=tk.LEFT, padx=20)

light_mode_button = ttk.Button(mode_frame, text="Light Mode", command=enable_light_mode)
light_mode_button.pack(side=tk.RIGHT, padx=20)

# Customizing Styles
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Poppins", 14), padding=5)
style.configure("TEntry", padding=5)
style.configure("Dark.TButton", background="#34495e", foreground="#ecf0f1")
style.configure("Dark.TEntry", fieldbackground="#34495e", foreground="#ecf0f1")
style.configure("Light.TButton", background="#fafafa", foreground="#333333")
style.configure("Light.TEntry", fieldbackground="#fafafa", foreground="#333333")

# Run the GUI event loop
root.mainloop()
