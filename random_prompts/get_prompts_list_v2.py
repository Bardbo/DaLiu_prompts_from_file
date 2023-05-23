import random
import pandas as pd
import argparse

prompt_table = pd.read_excel("prompt.xlsx")
prompt_table = prompt_table.dropna(axis=1, how='all')
prompt_table = {k:prompt_table[k].dropna().tolist() for k in prompt_table.columns}

stable_params_table = pd.read_excel("stable_parms.xlsx")
stable_params_table = stable_params_table.dropna(axis=1, how='all')
# 注意此处会把浮点数转成整数
numeric_cols = stable_params_table.select_dtypes(include=['float']).columns
if len(numeric_cols):
    print("浮点数列", numeric_cols)
    stable_params_table[numeric_cols] = stable_params_table[numeric_cols].astype('Int64')
stable_params_table = {k:stable_params_table[k].dropna().tolist() for k in stable_params_table.columns}

def generate(n):
    with open("prompts_list.txt", "w", encoding="utf-8") as f1, open("tags.txt", "w", encoding="utf-8") as f2:
        f1_ls, f2_ls, sd_model_ls = [], [], []
        for i in range(n):
            # prompt
            prompt = []
            for _, v in prompt_table.items():
                prompt.append(random.choice(v))
            prompt = ",".join(prompt)
            # stable_params
            stable_params = {k:random.choice(v) for k, v in stable_params_table.items()}
            s1 = [f'''--prompt "{prompt}"''']
            for k, v in stable_params.items():
                if (k != "sd_model") and isinstance(v, str):
                    s1.append(f'''--{k} "{v}"''')
                else:
                    s1.append(f"--{k} {v}")
            s1 = " ".join(s1)
            f1_ls.append(s1)
            f2_ls.append(f"""{prompt}\nNegative prompt: {stable_params.get("negative_prompt")}\nSteps: {stable_params.get("steps")}, Sampler: {stable_params.get("sampler_name")}, CFG scale: {stable_params.get("cfg_scale")}, Seed: {stable_params.get("seed")}, Size: {stable_params.get("width")}x{stable_params.get("height")}\n\n""")
            sd_model_ls.append(stable_params.get("sd_model", i))
        f1_ls = [x for _, x in sorted(zip(sd_model_ls, f1_ls))]
        f2_ls = [x for _, x in sorted(zip(sd_model_ls, f2_ls))]
        f1.write("\n".join(f1_ls))
        f2.write("".join(f2_ls))
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='生成prompt list文件')
    parser.add_argument('n', type=int, help='生成条数')
    args = parser.parse_args()
    generate(args.n)