# 🖼️ BG Remover API

_Remove image backgrounds instantly using AI — no Photoshop required._

Built with [rembg](https://github.com/danielgatis/rembg) + deployed via [Bolt.new](https://bolt.new) as a ready-to-use API.

Perfect for e-commerce, designers, content creators, and developers who need automated background removal at scale.

---

## ✨ Features

- ✅ Upload JPG/PNG → Get transparent PNG in seconds
- ✅ No credit card or signup needed to test
- ✅ Fast, serverless, scalable
- ✅ Easy integration (curl, Python, JS, etc.)
- ✅ MIT Licensed — free to use & modify

---

## 🚀 Live Demo Endpoint

Try it now — replace `your-photo.jpg` with your image path:

```bash
curl -X POST \
  https://bg-remover-api-xxxx.bolt.new/remove-bg \
  -F "image=@your-photo.jpg" \
  --output result.png
