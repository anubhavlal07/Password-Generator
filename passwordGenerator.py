import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
import string
import random
import hashlib
import base64
import tempfile
import webbrowser


# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Configure font
font_style = tkfont.Font(family="Consolas", size=12)

# Set background color to a darker theme
root.configure(bg="#333333")  # Dark grey color

# Set padding
padding = 20

# Variables to store user choices
var_special = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_alphabets = tk.BooleanVar(value=True)

# Function to display project info
def project_info():
    info_text = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Project Information</title>
    <style>
      body {
        display: flex;
        justify-content: center;
        font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        align-items: center;
        min-height: 100vh;
        margin: 0;
        background-color: #f0f0f0;
      }

      .card {
        max-width: 600px;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        background-color: #fff;
      }

      h1,
      h2 {
        text-align: left;
      }

      p {
        margin-bottom: 20px;
      }

      table {
        width: 100%;
        margin-bottom: 20px;
        border-collapse: collapse;
      }

      th,
      td {
        padding: 12px;
        text-align: left;
        border: 1px solid #ddd;
      }

      th {
        background-color: #f2f2f2;
      }
    </style>
  </head>

  <body>
    <div class="card">
      <h1>Project Information</h1>
      <p>
        This project developed by <b>SecureSquad</b> as part of a
        <b>Cyber Security Internship.</b> This project is designed to
        <b
          >Secure the Organizations in the Real World from Cyber Frauds
          performed by Hackers.</b
        >
      </p>

      <h2>Project Details</h2>
      <table>
        <tr>
          <td><strong>Project Name</strong></td>
          <td>Strong and Secured Password Generator</td>
        </tr>
        <tr>
          <td><strong>Project Description</strong></td>
          <td>Developing a tool to Create Strong and Secured Passwords</td>
        </tr>
        <tr>
          <td><strong>Project Start Date</strong></td>
          <td>29-FEB-2024</td>
        </tr>
        <tr>
          <td><strong>Project End Date</strong></td>
          <td>22-MAR-2024</td>
        </tr>
        <tr>
          <td><strong>Project Status</strong></td>
          <td>Completed</td>
        </tr>
      </table>

      <h2>Developer Details</h2>
      <table>
        <tr>
          <td><strong>Employee ID</strong></td>
          <td><strong>Name</strong></td>
          <td><strong>Email</strong></td>
        </tr>
        <tbody id="membersList"></tbody>
      </table>

      <h2>Company Details</h2>
      <table>
        <tr>
          <td><strong>Contact Email</strong></td>
          <td>contact@suprajatechnologies.com</td>
        </tr>
        <tr>
          <td><strong>Company Name</strong></td>
          <td>Supraja Technologies</td>
        </tr>
      </table>
    </div>

    <script>
      const members = [
        {
          name: "Anubhav Lal",
          id: "ST#IS#6182",
          email: "anubhavlal.15@gmail.com",
        },
        {
          name: "Karthikeyan N",
          id: "ST#IS#6204",
          email: "nkarthikeyan00763@gmail.com",
        },
        {
          name: "Padmapani S.N.",
          id: "ST#IS#6191",
          email: "padmapani11@gmail.com",
        },
        {
          name: "Abhithaa C",
          id: "ST#IS#6194",
          email: "mail2abhi23@gmail.com",
        },
        {
          name: "Yamini S",
          id: "ST#IS#6196",
          email: "yaminisankar024@gmail.com",
        },
      ];

      members.sort((a, b) => a.id.localeCompare(b.id));
      const membersList = document.getElementById("membersList");
      members.forEach((member) => {
        const row = document.createElement("tr");
        row.innerHTML = `
        <td>${member.id}</td>
        <td>${member.name}</td>
        <td>${member.email}</td>`;
        membersList.appendChild(row);
      });
    </script>
  </body>
</html>

    """
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as f:
        f.write(info_text)
        webbrowser.open_new_tab(f.name)

# Function to generate passwords
def generate_passwords():
    passwords = []
    for _ in range(5):
        password_length_str = entry_length.get()
        if not password_length_str:
            password_length = 12  # Set default length to 12 if no value entered
        else:
            password_length = int(password_length_str)
            
        use_special = var_special.get()
        use_numbers = var_numbers.get()
        use_alphabets = var_alphabets.get()

        characters = ''
        if use_special:
            characters += string.punctuation
        if use_numbers:
            characters += string.digits
        if use_alphabets:
            characters += string.ascii_letters

        if not characters:
            password = "Please select at least one character type."
        else:
            password = ''.join(random.choice(characters) for _ in range(password_length))
        
        passwords.append(password)
    
    # Calculate hash values for passwords
    hashed_passwords = []
    for password in passwords:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        hashed_passwords.append(hashed_password)
    
    # Sort passwords based on hash values
    passwords_sorted = [x for _, x in sorted(zip(hashed_passwords, passwords), reverse=True)]
    
    # Display passwords with padding
    result_text.config(state="normal")
    result_text.delete("1.0", "end")
    for password in passwords_sorted:
        result_text.insert("end", password + "\n")
    result_text.config(state="disabled")
    
    # Update text widget size based on content
    update_text_widget_size()
    
    # Show text widget and center it
    result_text.pack(anchor="center", padx=padding, pady=10)
    
    # Show message about password complexity
    complexity_label.pack(anchor="center", padx=padding, pady=10)

def update_text_widget_size():
    width = max(len(line) for line in result_text.get("1.0", "end-1c").split("\n")) + 2
    height = result_text.get("1.0", "end").count("\n") + 2
    result_text.config(width=width, height=height)

# Project Info button
info_button = tk.Button(root, text="Project Info", command=project_info, bg="#4CAF50", fg="white", font=font_style,borderwidth=0, highlightthickness=0)
info_button.pack(anchor="center", padx=padding, pady=(padding, 0))
# Title label
title_label = tk.Label(root, text="Password Generator", bg="#333333", fg="#f0f0f0", font=tkfont.Font(family="Consolas", size=18, weight="bold"))
title_label.pack(pady=padding)

# Password Length label and entry
length_label = tk.Label(root, text="Password Length:", bg="#333333", fg="#f0f0f0", font=font_style)
length_label.pack(anchor="w", padx=padding, pady=(0, 5))
entry_length = tk.Entry(root, font=font_style, width=20)  # Reduced width
entry_length.pack(anchor="w", padx=padding, pady=(0, padding))

# Character types checkboxes
special_check = ttk.Checkbutton(root, text="Special Characters", variable=var_special, style='Green.TCheckbutton')
special_check.pack(anchor="w", padx=padding, pady=(0, 5))
number_check = ttk.Checkbutton(root, text="Numbers", variable=var_numbers, style='Green.TCheckbutton')
number_check.pack(anchor="w", padx=padding, pady=(0, 5))
alphabets_check = ttk.Checkbutton(root, text="Alphabets", variable=var_alphabets, style='Green.TCheckbutton')
alphabets_check.pack(anchor="w", padx=padding, pady=(0, 5))

# Generate Passwords button
generate_button = tk.Button(root, text="Generate", command=generate_passwords, bg="#4CAF50", fg="white", font=font_style,borderwidth=0, highlightthickness=0)
generate_button.pack(anchor="center", padx=padding, pady=(padding, 0))

# Password complexity label
complexity_label = tk.Label(root, text="Passwords are displayed in the order \n of their complexity based on hash values.", bg="#333333", fg="#f0f0f0", font=tkfont.Font(family="Consolas", size=10, weight="bold"))

# Generated Passwords text area
result_text = tk.Text(root, bg="#333333", fg="#f0f0f0", font=font_style, wrap="none", borderwidth=0, highlightthickness=0)

# Define a custom style for the checkbuttons
style = ttk.Style()
style.configure('Green.TCheckbutton', foreground='green', background="#333333")

# Set favicon
favicon_base64 = "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X8WrL7+KAw86EKefeTrS6eGd0PjB+x9gxhUz8O47mx60093djb889hf89Ym/4shPHonPf+nzaGqq7rvYF194Eb+b87vNHvrS19uHvz35Nzz91NM47nPH4XNf/Nywr//Siy/hpmtvQnfPplOhli9bjrvvvBsP3fcQjvvCcfj0UZ+u6o4rDEM8+tCjuPt/7t7sNs2rVq7C/ffej788/hecNuk0fOSAjwy7jXvuugd3/c9dsOGGn+WqijfffBO3zLoF991zH0448QQccNABJf8sSdDd04277rgLjz362GZ/3rfeegu/m/M7PPboY5h6zlTsuFPp27FvrMxK4i6qKh4AfPuc3Q/QYvGfogmrfH5zY9wh1Jw+OQ6KlpJem81kh91JDQqCAJf9+jK8/tqmneHGln+wHI8/9ji6urqw5957Ip0qrc0Xnnuh5LPTR40aVfKdeXd3N/5w+x9w8+ybh3SAznvvvodFCxbhYx//2JDnWaxYvgK//PkvsWL51ot2qooli5fgL4/9BalUCruP2r3kO4aHH3wYPd2l7Zt+4EEHlnxn/u477+LG627En+760zbbV1XMe30egiDAvh8aeiXppRdfwtVXXI18YesLoYIgwKuvvIpn5z6L7bbfDjvsUNq22vl8Hg/cV/oxyUcdcxRyDaWV0V95+RXMuGIGnvrbUygWt775a7FYxLPPPIvddt8NO+449E7rzjvuxN133r3NuVw9PT145ulnsGD+AowaNQrNzaVVG955+x38/Zm/l/TabC6Loz9zdEmvtaHFo488iplXzMT8efO3+fN2d3Xj2aefxUEfPQgNDQ0ltbkxVUVvb8lnIfhrutZcMvCJoKWdp1gJqtwLqAJUS0+qyik13f0/d2PRwkVDfr4NLR558BH88Ps/xKMPPbpJVp1ENrR4+MGH8YPv/wCPPPzIsGKe9/o83HP3PUN+/k3X3zSs0+R6enpw+62346c/+ileefmVIb8uTj09Pbjtt7eVFPN999y32crL5nR1dWH29bPXDkcNxfvvvY8rL7sSl19y+WYrMEm0fszvvfvekF9nQ4vZ188e8vtt3uvz8Oe7/zys2F5/9XX89Mc/xa233Iru7sQsRtuq1155DT/90U8x55Y5m60abcmarjW44dobIpvoXvbQbB4jBuYA+Ml6J6sCNT6RyTUV9wlAd083Hn7w4dJe292NW2+5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"
favicon_data = base64.b64decode(favicon_base64)
root.iconphoto(True, tk.PhotoImage(data=favicon_data))

root.mainloop()
