import os
import subprocess


def save_and_open_svg(svg_content: str, filename: str = "output.svg") -> str:
    """Save SVG content to a file and open it in the default browser/viewer.

    Args:
        svg_content: A complete SVG string (should start with <svg).
        filename: Name for the saved file (default: output.svg).
    """
    if not filename.endswith(".svg"):
        filename += ".svg"

    output_dir = os.path.expanduser("~/svg-outputs")
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w") as f:
        f.write(svg_content)

    # Try to open in default viewer (works on macOS, Linux, Windows)
    try:
        if os.name == "darwin" or os.uname().sysname == "Darwin":
            subprocess.Popen(["open", filepath])
        elif os.name == "nt":
            os.startfile(filepath)
        else:
            subprocess.Popen(["xdg-open", filepath])
    except Exception as e:
        return f"Saved to {filepath} but could not open viewer: {e}"

    return f"SVG saved and opened: {filepath}"