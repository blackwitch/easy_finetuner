
# Easy Finetuner

[![Open In Colab](https://img.shields.io/static/v1?label=Open%20in%20Colab&message=사용법&color=yellow&logo=googlecolab)](https://colab.research.google.com/github/choijhyeok/easy_finetuner/blob/main/%EA%B0%9C%EC%9D%B8_%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%85%8B%EC%9D%84_%ED%86%B5%ED%95%9C_llama2_fine_tune.ipynb)

&nbsp;



Easy Finetuner는 llama2 계열 모델의 쉬운 fine-tune 방법을 설명하기 위해서 제작하였습니다. 


(발표영상 : https://www.youtube.com/live/4I9AUFuBlFs?feature=shared)

&nbsp;


(2024.02.07) 로컬에서 실행할 수 있도록 일부 파일을 수정하고 데이터셋 구축, 추가 모델 적용을 위해 수정하였습니다. 

(torch 2.2.0 , cuda 12.1에 맞춰서 수정되어 있으니 다른 버전을 사용하시는 분은 그에 맞게 수정해 사용하세요.)

&nbsp;


## Custom Dataset 추가방법

- 사용자 개인의 Dataset을 example-datasets 아래에 huggingface의 datasets 형식으로 저장시키면 dataset load가 쉽게 적용이 가능합니다.
- 자세한 방법은 위의 colab을 참고해 주세요.

&nbsp;
### Usage
```
git clone https://github.com/choijhyeok/easy_finetuner.git
cd easy_finetuner
pip install -r requirements.txt
```

&nbsp;

## 주의사항

- 모든 Parameter는 colab T4 GPU에 최적화 되도록 설정했습니다. (만약 다른 GPU를 사용하고 싶다면 confing.py에서 fb16, bf16 을 사용하고자 하는 GPU에 맞게 변경해 주세요)
- huggingface의 PEFT 패키지의 SFTTrainer, lora를 사용합니다.
- 현재는 llama2 기반의 모델에만 적용가능하게 설정했습니다. (fine-tune, load, inference 모두)
- torch는 다음과 같이 설치하세요.
&nbsp;
### torch 설치 (cuda 12.1에 맞는 nightly 버전 설치)
```
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121
```

&nbsp;
## Reference 
- https://github.com/lxe/simple-llm-finetuner
