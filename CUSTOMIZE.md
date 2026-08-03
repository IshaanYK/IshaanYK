# 🚀 How to Customize & Deploy for Your GitHub Profile

Want an animated, cyber-styled, interactive GitHub profile README like this one? You can fork this repository and set it up for your own GitHub profile in just **3 simple steps**!

---

## ⚡ Step 1: Fork & Rename Repository

1. Click **Fork** at the top right of this repository.
2. Rename the repository to match your **exact GitHub username**:
   - Example: If your GitHub username is `octocat`, rename the repo to `octocat/octocat`.
   - *GitHub will automatically display this repository's README on your profile page!*

---

## 🛠️ Step 2: Customize Your Info & Widgets

Clone your repository locally:
```bash
git clone https://github.com/<YOUR_USERNAME>/<YOUR_USERNAME>.git
cd <YOUR_USERNAME>
```

### 1. Update Header Banner (`scripts/make_header_banner.py`)
- Open `scripts/make_header_banner.py`.
- Edit your name, education/tagline, and the cycling typewriter sentences (`l1`, `l2`, `l3`, `l4`).

### 2. Update Neofetch Card (`scripts/make_info_card.py`)
- Open `scripts/make_info_card.py`.
- Change `HOST = "YOUR_USERNAME"` and customize the `ROWS` list (Role, Focus, Status, Tech Stack, Highlights).

### 3. Update Audio Player (`scripts/make_music_player.py`)
- Open `scripts/make_music_player.py`.
- Change the track title, artist name, or audio link to your favorite song or video!

### 4. Update Contribution Graph User (`scripts/fetch_contributions.py`)
- Open `scripts/fetch_contributions.py`.
- Change `GH_PROFILE_USER = "YOUR_USERNAME"`.

### 5. Update Profile README Links (`README.md`)
- Open `README.md`.
- Replace all instances of `IshaanYK`, links, portfolio, and social badges with your handle.

---

## 🎨 Step 3: Build & Push to GitHub!

Run the one-command builder script to regenerate all SVGs at once:

```bash
python scripts/build_all.py
```

Then commit and push your changes:

```bash
git add .
git commit -m "Customize profile for my GitHub"
git push origin main
```

---

## 🤖 Step 4: Enable Automated Daily Graph Updates (Optional)

This repo includes a GitHub Action (`.github/workflows/update-profile-art.yml`) that automatically refreshes your contribution graph and streak metrics every day!

To enable it:
1. Go to your repo's **Settings** -> **Actions** -> **General**.
2. Scroll to **Workflow permissions**.
3. Select **Read and write permissions** and click **Save**.

---

🎉 **Done!** Visit `https://github.com/<YOUR_USERNAME>` to see your new animated GitHub profile live!
