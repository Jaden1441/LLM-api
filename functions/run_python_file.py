import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
   try:
      abs_working_dir = os.path.abspath(working_directory)
      abs_file_path = os.path.normpath(os.path.join(abs_working_dir,file_path))

      if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
         return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
      if not os.path.isfile(abs_file_path):
         return  f'Error: "{file_path}" does not exist or is not a regular file'
      if not abs_file_path.endswith(".py"):
         return f'Error: "{file_path}" is not a Python file'

      command = ["python", abs_file_path]
      
      if args is not None:
         command.extend(args)
      
      sp = subprocess.run(command, text=True, cwd=abs_working_dir,
                           capture_output=True, timeout=30)

      output = []
      
      if sp.returncode != 0:
         output.append(f"Process exited with code {sp.returncode}")

      if not sp.stdout and not sp.stderr:
         output.append("No output produced")
      
      if sp.stdout:
         output.append(f"STDOUT:\n{sp.stdout}")

      if sp.stderr:
         output.append(f"STDERR:\n{sp.stderr}")


      return "\n".join(output)

   except Exception as e:
      return f"Error: {str(e)}"