## decide-what-to-watch
Decide what to watch using the power of randomness!

## The problem

Suppose you have different things to watch while you're resting: 

- Series on your favourite streaming platform
- "Watch Later" playlist on YouTube
- Some interesting lectures on YouTube

You're likely to choose the most entertaining option every time.
That is not quite reasonable, if you generally want to watch all
of mentioned things at least in some proportions (not 100:0:0).

## The solution

This script allows you to specify all your chill-content sources:

```json
{
  "alternatives": [
    {
      "link": "https://www.google.com",
      "weight": 50,
      "description": "Your favourite streaming service with films/series"
    },
    {
      "link": "https://www.youtube.com/playlist?list=...",
      "weight": 15,
      "description": "Awesome lectures about ... (easy and straightforward)"
    },
        {
      "link": "https://www.youtube.com/playlist?list=...",
      "weight": 15,
      "description": "Some other awesome lectures"
    },
    {
      "link": "https://www.youtube.com/playlist?list=...",
      "weight": 5,
      "description": "Watch Later playlist with useful videos"
    }
  ]
}
```

And then allow the script to **decide for you what to watch now**:
```bash
decide
```

And one of the links that you've provided will open in the browser. Resistance 
is useless. Just watch. 

## Details
- The `weights` you provide are used to determine the probability of 
  opening each link
- Add only the content that you really want to watch (to avoid 
  disobedience)
- Weight sum does not have to be 100 or something else. Use the values you 
  like: weights distribution `20`:`30`:`50` is equal to `4`:`6`:`10` or 
  `2`:`3`:`5`
- All links must start with "`https://`"

# Installation
## Prerequisites
- Python 3.6+ (note: it's better not to use `venv`)
- Linux/Windows/Mac

## How to install
Run these commands in your terminal:
```bash
cd ~/Downloads  # or anywhere else
git clone https://github.com/m-danya/decide-what-to-watch
cd decide-what-to-watch
pip install .
# and then restart the terminal
```
## How to configure
Run `decide --config` in your terminal. This will open the configuration 
file in your default text editor. Paste an example config into it (you can find 
it in the beginning of *"The solution"* section) and modify it as you want.

Also, you can run `decide --show-config-path` to get the path to configuration 
file.

## How to run
Run this command in your terminal:
```bash
decide
```

## More
[Статья в блоге](https://m-danya.ru/decide-what-to-watch/)

