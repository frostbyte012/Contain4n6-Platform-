import tkinter as tk
import subprocess

def run_docker_command():
    command = entry.get()
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, output)
    except subprocess.CalledProcessError as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {e.output}")

def pull_image():
    image_id = image_entry.get()
    try:
        output = subprocess.check_output(f"docker pull {image_id}", shell=True, stderr=subprocess.STDOUT, text=True)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, output)
    except subprocess.CalledProcessError as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {e.output}")

def list_containers():
    try:
        output = subprocess.check_output("docker ps", shell=True, stderr=subprocess.STDOUT, text=True)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, output)
    except subprocess.CalledProcessError as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {e.output}")

def create_container():
    container_name = container_entry.get()
    image_id = image_entry.get()
    try:
        output = subprocess.check_output(f"docker run --name {container_name} -d {image_id}", shell=True, stderr=subprocess.STDOUT, text=True)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, output)
    except subprocess.CalledProcessError as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {e.output}")

def inspect_image():
    image_id = inspect_image_entry.get()
    try:
        output = subprocess.check_output(f"sudo docker inspect {image_id}", shell=True, stderr=subprocess.STDOUT, text=True)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, output)
    except subprocess.CalledProcessError as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {e.output}")

def image_history():
    image_id = history_image_entry.get()
    try:
        output = subprocess.check_output(f"sudo docker history {image_id}", shell=True, stderr=subprocess.STDOUT, text=True)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, output)
    except subprocess.CalledProcessError as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {e.output}")

def docker_info():
    try:
        output = subprocess.check_output("sudo docker info", shell=True, stderr=subprocess.STDOUT, text=True)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, output)
    except subprocess.CalledProcessError as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {e.output}")

def image_list():
    try:
        output = subprocess.check_output("sudo docker image ls", shell=True, stderr=subprocess.STDOUT, text=True)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, output)
    except subprocess.CalledProcessError as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {e.output}")

def attack_root_shell():
    image_id = attack_image_entry.get()
    name_shell = name_shell_entry.get()

    try:
        command = f"sudo -S docker run -v /:/hostOS --name {name_shell} {image_id}"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        output, error = process.communicate()
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, output)
        if error:
            result_text.insert(tk.END, f"Error : {error}")

    except subprocess.CalledProcessError as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {e.output}")



root = tk.Tk()
root.title("CONTAIN4n6")

# Heading
heading_label = tk.Label(root, text="CONTAIN4n6", font=("Helvetica", 18, "bold"))
heading_label.pack()

# Sub-heading
sub_heading_label = tk.Label(root, text="Deepraj Majumdar [M23CSE012]\nSunirban Sarkar [M23CSE029]", font=("Helvetica", 12))
sub_heading_label.pack()


label = tk.Label(root, text="Enter Docker Command:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

button = tk.Button(root, text="Run Command", command=run_docker_command)
button.pack()

image_label = tk.Label(root, text="Enter Docker Image ID:")
image_label.pack()

image_entry = tk.Entry(root, width=50)
image_entry.pack()

pull_button = tk.Button(root, text="Pull Image", command=pull_image)
pull_button.pack()

container_label = tk.Label(root, text="Enter Container Name:")
container_label.pack()

container_entry = tk.Entry(root, width=50)
container_entry.pack()

create_button = tk.Button(root, text="Create Container", command=create_container)
create_button.pack()

inspect_image_label = tk.Label(root, text="Inspect Image ID:")
inspect_image_label.pack()

inspect_image_entry = tk.Entry(root, width=50)
inspect_image_entry.pack()

inspect_button = tk.Button(root, text="Inspect Image", command=inspect_image)
inspect_button.pack()

history_image_label = tk.Label(root, text="Image History ID:")
history_image_label.pack()

history_image_entry = tk.Entry(root, width=50)
history_image_entry.pack()

history_button = tk.Button(root, text="Image History", command=image_history)
history_button.pack()

info_button = tk.Button(root, text="Docker Info", command=docker_info)
info_button.pack()

image_list_button = tk.Button(root, text="Image List", command=image_list)
image_list_button.pack()

attack_label = tk.Label(root, text="Enter Custom Image ID:")
attack_label.pack()

attack_image_entry = tk.Entry(root, width=50)
attack_image_entry.pack()

name_shell_label = tk.Label(root, text="Enter Custom Name for Shell:")
name_shell_label.pack()

name_shell_entry = tk.Entry(root, width=50)
name_shell_entry.pack()

attack_button = tk.Button(root, text="Attack Root Shell", command=attack_root_shell)
attack_button.pack()

list_button = tk.Button(root, text="List Containers", command=list_containers)
list_button.pack()

result_text = tk.Text(root, height=20, width=80)
result_text.pack()

root.mainloop()
