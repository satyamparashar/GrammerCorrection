import gradio as gr
from gramformer import Gramformer

gf = Gramformer(models=1, use_gpu=False)  # 0 = detector, 1 = highlighter, 2 = corrector, 3 = all


def correct(sentence):
    res = gf.correct(sentence)  # Gramformer correct

    # Convert set to list if necessary
    res_list = list(res) if isinstance(res, set) else res

    return res_list[0] if res_list and len(res_list) > 0 else "Error: Unable to correct the sentence."


app_inputs = gr.Textbox(lines=2, placeholder="Enter sentence here...")
interface = gr.Interface(fn=correct,
                         inputs=app_inputs,
                         outputs='text',
                         title='Hello, I\'m Your Friend')
interface.launch()
