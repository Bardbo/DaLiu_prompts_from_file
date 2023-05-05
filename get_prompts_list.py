real_model = ["braBeautiful", "camellia", "fantasticmixReal", "fidelity", "henmix25", "henmixReal_v20", "henmixReal_v22",
              "kencan", "newmarsmix", "xsmix"]
cartoon_models = ["3Guofeng3", "beenyouToon", "breakdro", 'cetus', "colorBox", "Counterfeit", "dalcefo", "disillusion",
                  "duelanime", "facebomb", "fantasticmix_V20", "furnace47", "grapefruit", "hassaku", "kuromimix", 
                  "libramix", "meinahentai", "meinamix_meinaV8", "meinamix_meinaV9", "meinapastel_V4", "mistoonAnime",
                  "mixProV4", "OldFish", "pastelLines", "pastelMix", "perfectWorld", "personaStyle", "pikasAni", "popPop",
                  "primemix_ani", "prememix_color", "recAnimated", "V08", "velaMix", "wintermoon", "wlop", "yesmix", "yorrrl"]

prompt_tags = {
    "sd_model": real_model+cartoon_models,
    "prompt": "(best quality, masterpiece:1.3),  1 girl, (pale skin, korean mixed, kpop idol:1.2), pale skin, bunny ears, leotard, side boob, (slender, skinny+thin thighs, cleavage:1.2), medium breasts, thigh gap, perfect hips",
    "negative_prompt": "(worst quality:1.4), (low quality:1.4), (thick legs:1.3), (fat:1.2), (abs, muscular, rib, wide hips:1.2), (ng_deepnegative_v1_75t:1.2), badhandv4, (teeth, open mouth, loli, 2 girls, multiple girls:1.2), (bokeh, blurry, censored:1.2), (greyscale, monochrome:1.0), cartoon, comic, multi view, text, title, logo, signature",
    "seed": -1,
    "sampler_name": "DPM++ SDE Karras",
    "batch_size": 4,
    "n_iter": 1,
    "steps": 25,
    "cfg_scale": 10,
    "width": 512,
    "height": 768,
}

print(f"""模型数：{len(prompt_tags["sd_model"])}""")

with open("prompts_list.txt", "w") as f:
    for m in prompt_tags["sd_model"]:
        s = [f"--sd_model {m}"]
        for k,v in prompt_tags.items():
            if k != "sd_model":
                if isinstance(v, str):
                    s.append(f'''--{k} "{v}"''')
                else:
                    s.append(f"--{k} {v}")
        s = " ".join(s)
        f.write(s+"\n")
        