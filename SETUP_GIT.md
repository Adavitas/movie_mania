# Git Setup Instructions

## Initial Setup

1. **Initialize Git Repository**
```bash
git init
```

2. **Add Remote Repository**
```bash
git remote add origin git@github.com:Adavitas/movie_mania.git
```

3. **Check Remote**
```bash
git remote -v
```

4. **Add All Files**
```bash
git add .
```

5. **Create First Commit**
```bash
git commit -m "Initial commit: Movie Mania - Stanford Code in Place Final Project"
```

6. **Push to GitHub**
```bash
git branch -M main
git push -u origin main
```

## Subsequent Updates

After making changes:
```bash
git add .
git commit -m "Your commit message"
git push
```

## Check Status
```bash
git status
```

## View Commit History
```bash
git log --oneline
```

---

**Note:** Make sure you have SSH keys set up with GitHub before pushing.
