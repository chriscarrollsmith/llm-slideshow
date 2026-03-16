import os
import subprocess


def save_and_view_threejs(scene_code: str, filename: str = "scene.html", title: str = "Three.js Scene") -> str:
    """Save and open an interactive 3D scene built with Three.js.

    Write the body of a Three.js scene as an ES module script. The following
    imports are available via import map:

        import * as THREE from 'three';
        import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
        import { FontLoader } from 'three/addons/loaders/FontLoader.js';
        import { TextGeometry } from 'three/addons/geometries/TextGeometry.js';
        import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
        import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
        // ... any other three/addons/* module

    A boilerplate scene, camera, renderer, OrbitControls, lights, resize
    handler, and animation loop are NOT provided — write everything yourself
    so you have full control. Your code is the entire <script type="module">
    block.

    Tips for good scenes:
    - Always add OrbitControls for interactivity.
    - Use MeshStandardMaterial or MeshPhysicalMaterial with proper lighting.
    - Add a ground plane or grid for spatial reference.
    - Use requestAnimationFrame for animation loops.
    - Set renderer.setPixelRatio(devicePixelRatio) for sharp rendering.
    - Handle window resize events.

    Args:
        scene_code: ES module JavaScript code for a Three.js scene.
        filename: Output filename (default: scene.html).
        title: Page title shown in the browser tab.
    """
    if not filename.endswith(".html"):
        filename += ".html"

    output_dir = os.path.expanduser("~/threejs-outputs")
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<title>{title}</title>
<style>
  body {{ margin: 0; overflow: hidden; background: #000; }}
</style>
</head><body>
<script type="importmap">
{{ "imports": {{
    "three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"
}} }}
</script>
<script type="module">
{scene_code}
</script>
</body></html>"""

    with open(filepath, "w") as f:
        f.write(html)

    try:
        if hasattr(os, "uname") and os.uname().sysname == "Darwin":
            subprocess.Popen(["open", filepath])
        elif os.name == "nt":
            os.startfile(filepath)
        else:
            subprocess.Popen(["xdg-open", filepath])
    except Exception as e:
        return f"Saved to {filepath} but could not open: {e}"

    return f"Scene opened: {filepath}"