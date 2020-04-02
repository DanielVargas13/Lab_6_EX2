import os.path
from os import path
import csv
import subprocess

def createCsv(urls,locs):
  with open("/Lab_6_EX2/PopPython/RepositoriosPythonLOCDavi.csv", 'w', newline='') as n_file:

    fnames = [
        'URL;',
        'LOC;'
    ]

    csv_writer = csv.DictWriter(n_file, fieldnames=fnames, dialect="excel-tab")
    csv_writer.writeheader()
    for y in range(len(urls)):
        csv_writer.writerow(
            {
                'URL;': "{};".format(urls[y]),
                'LOC;': "{};".format(locs[y])
            })

def getTotal(result):
    index = 0
    total = ""
    ch = result[index]
    while ch == " ":
        index += 1
        ch = result[index]
    while ch != " ":
        total += ch
        index += 1
        ch = result[index]
    return total
    
size = 500

locs = []

urls_repo = []

urls = [
    'https://github.com/PaddlePaddle/models',
    'https://github.com/davidhalter/jedi',
    'https://github.com/sshwsfc/xadmin',
    'https://github.com/jarun/googler',
    'https://github.com/scikit-learn-contrib/imbalanced-learn',
    'https://github.com/deepmind/graph_nets',
    'https://github.com/django/channels',
    'https://github.com/tschellenbach/Stream-Framework',
    'https://github.com/smacke/subsync',
    'https://github.com/SpiderClub/weibospider',
    'https://github.com/MrS0m30n3/youtube-dl-gui',
    'https://github.com/smicallef/spiderfoot',
    'https://github.com/jiaaro/pydub',
    'https://github.com/wb14123/seq2seq-couplet',
    'https://github.com/HypothesisWorks/hypothesis',
    'https://github.com/facebookarchive/augmented-traffic-control',
    'https://github.com/airbnb/knowledge-repo',
    'https://github.com/vi3k6i5/flashtext',
    'https://github.com/encode/httpx',
    'https://github.com/foosel/OctoPrint',
    'https://github.com/django-oscar/django-oscar',
    'https://github.com/wireservice/csvkit',
    'https://github.com/ashnkumar/sketch-code',
    'https://github.com/jrnl-org/jrnl',
    'https://github.com/euske/pdfminer',
    'https://github.com/mher/flower',
    'https://github.com/google/clusterfuzz',
    'https://github.com/flask-admin/flask-admin',
    'https://github.com/fogleman/Minecraft',
    'https://github.com/facebookarchive/huxley',
    'https://github.com/angr/angr',
    'https://github.com/JakeWharton/pidcat',
    'https://github.com/jazzband/pip-tools',
    'https://github.com/d2l-ai/d2l-en',
    'https://github.com/commonmark/commonmark-spec',
    'https://github.com/MycroftAI/mycroft-core',
    'https://github.com/deepmipt/DeepPavlov',
    'https://github.com/nuno-faria/tiler',
    'https://github.com/pre-commit/pre-commit',
    'https://github.com/gregmalcolm/python_koans',
    'https://github.com/NullArray/AutoSploit',
    'https://github.com/bitcoin/bips',
    'https://github.com/MagicStack/asyncpg',
    'https://github.com/paralax/awesome-honeypots',
    'https://github.com/cloudtools/troposphere',
    'https://github.com/cloudera/hue',
    'https://github.com/alicevision/meshroom',
    'https://github.com/stephenmcd/mezzanine',
    'https://github.com/persepolisdm/persepolis',
    'https://github.com/seemoo-lab/opendrop',
    'https://github.com/google/trax',
    'https://github.com/WenDesi/lihang_book_algorithm',
    'https://github.com/okfn-brasil/serenata-de-amor',
    'https://github.com/OpenNMT/OpenNMT-py',
    'https://github.com/eriklindernoren/PyTorch-YOLOv3',
    'https://github.com/gorakhargosh/watchdog',
    'https://github.com/cupy/cupy',
    'https://github.com/PyCQA/pycodestyle',
    'https://github.com/deepmind/learning-to-learn',
    'https://github.com/longld/peda',
    'https://github.com/Netflix/security_monkey',
    'https://github.com/GoogleCloudPlatform/python-docs-samples',
    'https://github.com/OmkarPathak/pygorithm',
    'https://github.com/Kinto/kinto',
    'https://github.com/fmfn/BayesianOptimization',
    'https://github.com/lisa-lab/DeepLearningTutorials',
    'https://github.com/posativ/isso',
    'https://github.com/commaai/research',
    'https://github.com/NicolasHug/Surprise',
    'https://github.com/jisaacks/GitGutter',
    'https://github.com/malwaredllc/byob',
    'https://github.com/ujjwalkarn/DataSciencePython',
    'https://github.com/platformio/platformio-core',
    'https://github.com/martinblech/xmltodict',
    'https://github.com/princewen/tensorflow_practice',
    'https://github.com/stewartmcgown/uds',
    'https://github.com/spesmilo/electrum',
    'https://github.com/hzy46/Deep-Learning-21-Examples',
    'https://github.com/microsoft/nlp-recipes',
    'https://github.com/NervanaSystems/neon',
    'https://github.com/dwyl/english-words',
    'https://github.com/avinassh/rockstar',
    'https://github.com/realpython/discover-flask',
    'https://github.com/micahflee/onionshare',
    'https://github.com/twisted/twisted',
    'https://github.com/django-crispy-forms/django-crispy-forms',
    'https://github.com/sdispater/pendulum',
    'https://github.com/fluentpython/example-code',
    'https://github.com/jadore801120/attention-is-all-you-need-pytorch',
    'https://github.com/openimages/dataset',
    'https://github.com/edgedb/edgedb',
    'https://github.com/neozhaoliang/pywonderland',
    'https://github.com/pudo/dataset',
    'https://github.com/utkuozbulak/pytorch-cnn-visualizations',
    'https://github.com/lmcinnes/umap',
    'https://github.com/chrippa/livestreamer',
    'https://github.com/MVIG-SJTU/AlphaPose',
    'https://github.com/floydhub/dl-docker',
    'https://github.com/misterch0c/shadowbroker',
    'https://github.com/snorkel-team/snorkel',
    'https://github.com/StackStorm/st2',
    'https://github.com/Lasagne/Lasagne',
    'https://github.com/dpkp/kafka-python',
    'https://github.com/YadiraF/PRNet',
    'https://github.com/dylanaraps/pywal',
    'https://github.com/qiyeboy/IPProxyPool',
    'https://github.com/ajalt/fuckitpy',
    'https://github.com/wepe/MachineLearning',
    'https://github.com/machinelearningmindset/deep-learning-roadmap',
    'https://github.com/dschep/ntfy',
    'https://github.com/facebookresearch/DrQA',
    'https://github.com/ricequant/rqalpha',
    'https://github.com/encode/starlette',
    'https://github.com/conan-io/conan',
    'https://github.com/MorvanZhou/Tensorflow-Tutorial',
    'https://github.com/jayfk/statuspage',
    'https://github.com/jazzband/tablib',
    'https://github.com/AirtestProject/Airtest',
    'https://github.com/naturomics/CapsNet-Tensorflow',
    'https://github.com/lukemelas/EfficientNet-PyTorch',
    'https://github.com/CouchPotato/CouchPotatoServer',
    'https://github.com/1adrianb/face-alignment',
    'https://github.com/emre/storm',
    'https://github.com/PokemonGoF/PokemonGo-Bot',
    'https://github.com/xonsh/xonsh',
    'https://github.com/minimaxir/textgenrnn',
    'https://github.com/sripathikrishnan/redis-rdb-tools',
    'https://github.com/dmlc/gluon-cv',
    'https://github.com/fastmonkeys/stellar',
    'https://github.com/django-tastypie/django-tastypie',
    'https://github.com/Qix-/better-exceptions',
    'https://github.com/fizyr/keras-retinanet',
    'https://github.com/shidenggui/easytrader',
    'https://github.com/nvdv/vprof',
    'https://github.com/maurosoria/dirsearch',
    'https://github.com/xingyizhou/CenterNet',
    'https://github.com/asweigart/pyautogui',
    'https://github.com/NVIDIA/apex',
    'https://github.com/stanfordnlp/stanza',
    'https://github.com/twintproject/twint',
    'https://github.com/junyanz/iGAN',
    'https://github.com/scikit-image/scikit-image',
    'https://github.com/karpathy/arxiv-sanity-preserver',
    'https://github.com/reinderien/mimic',
    'https://github.com/miguelgrinberg/Flask-SocketIO',
    'https://github.com/iodide-project/pyodide',
    'https://github.com/prompt-toolkit/ptpython',
    'https://github.com/NVlabs/stylegan2',
    'https://github.com/pandolia/qqbot',
    'https://github.com/laramies/theHarvester',
    'https://github.com/yhat/ggpy',
    'https://github.com/hwalsuklee/tensorflow-generative-model-collections',
    'https://github.com/mementum/backtrader',
    'https://github.com/offu/WeRoBot',
    'https://github.com/volatilityfoundation/volatility',
    'https://github.com/stamparm/maltrail',
    'https://github.com/pavelgonchar/colornet',
    'https://github.com/iGhibli/iOS-DeviceSupport',
    'https://github.com/conda/conda',
    'https://github.com/nylas/sync-engine',
    'https://github.com/Jrohy/multi-v2ray',
    'https://github.com/DEAP/deap',
    'https://github.com/adamchainz/django-cors-headers',
    'https://github.com/pypa/virtualenv',
    'https://github.com/jcjohnson/pytorch-examples',
    'https://github.com/PySimpleGUI/PySimpleGUI',
    'https://github.com/yosinski/deep-visualization-toolbox',
    'https://github.com/openstack/openstack',
    'https://github.com/taoufik07/responder',
    'https://github.com/google/roboto',
    'https://github.com/jarun/buku',
    'https://github.com/LonamiWebs/Telethon',
    'https://github.com/jmcarp/robobrowser',
    'https://github.com/yahoo/TensorFlowOnSpark',
    'https://github.com/bigchaindb/bigchaindb',
    'https://github.com/Kozea/WeasyPrint',
    'https://github.com/amdegroot/ssd.pytorch',
    'https://github.com/MechanicalSoup/MechanicalSoup',
    'https://github.com/googleapis/google-api-python-client',
    'https://github.com/LazoCoder/Pokemon-Terminal',
    'https://github.com/google/grr',
    'https://github.com/rarcega/instagram-scraper',
    'https://github.com/ritiek/spotify-downloader',
    'https://github.com/aidlearning/AidLearning-FrameWork',
    'https://github.com/awentzonline/image-analogies',
    'https://github.com/hylang/hy',
    'https://github.com/librosa/librosa',
    'https://github.com/spulec/moto',
    'https://github.com/zzzeek/sqlalchemy',
    'https://github.com/cchen156/Learning-to-See-in-the-Dark',
    'https://github.com/mrjbq7/ta-lib',
    'https://github.com/trekhleb/learn-python',
    'https://github.com/rkern/line_profiler',
    'https://github.com/nameko/nameko',
    'https://github.com/instagrambot/instabot',
    'https://github.com/ReactiveX/RxPY',
    'https://github.com/jorgebastida/awslogs',
    'https://github.com/kkroening/ffmpeg-python',
    'https://github.com/samuelhwilliams/Eel',
    'https://github.com/msiemens/tinydb',
    'https://github.com/codertimo/BERT-pytorch',
    'https://github.com/QUANTAXIS/QUANTAXIS',
    'https://github.com/mwouts/jupytext',
    'https://github.com/buriburisuri/speech-to-text-wavenet',
    'https://github.com/rossant/awesome-math',
    'https://github.com/Pylons/pyramid',
    'https://github.com/eudicots/Cactus',
    'https://github.com/byt3bl33d3r/CrackMapExec',
    'https://github.com/spyoungtech/grequests',
    'https://github.com/facebook/codemod',
    'https://github.com/opencv/cvat',
    'https://github.com/amperser/proselint',
    'https://github.com/hhatto/autopep8',
    'https://github.com/Guake/guake',
    'https://github.com/mininet/mininet',
    'https://github.com/PyGithub/PyGithub',
    'https://github.com/endernewton/tf-faster-rcnn',
    'https://github.com/Tautulli/Tautulli',
    'https://github.com/arielf/weight-loss',
    'https://github.com/gaubert/gmvault',
    'https://github.com/simonw/datasette',
    'https://github.com/s3tools/s3cmd',
    'https://github.com/jeffkaufman/icdiff',
    'https://github.com/mbadry1/DeepLearning.ai-Summary',
    'https://github.com/raspberrypi/documentation',
    'https://github.com/vaexio/vaex',
    'https://github.com/lektor/lektor',
    'https://github.com/dabeaz/curio',
    'https://github.com/ClusterHQ/flocker',
    'https://github.com/corna/me_cleaner',
    'https://github.com/pyca/cryptography',
    'https://github.com/yuanxiaosc/DeepNude-an-Image-to-Image-technology',
    'https://github.com/apachecn/sklearn-doc-zh',
    'https://github.com/kootenpv/whereami',
    'https://github.com/Blizzard/s2client-proto',
    'https://github.com/felixonmars/dnsmasq-china-list',
    'https://github.com/tensorflow/skflow',
    'https://github.com/snipsco/snips-nlu',
    'https://github.com/sphinx-doc/sphinx',
    'https://github.com/Newmu/dcgan_code',
    'https://github.com/tckmn/mkcast',
    'https://github.com/Tribler/tribler',
    'https://github.com/jpadilla/pyjwt',
    'https://github.com/gnemoug/distribute_crawler',
    'https://github.com/MrGemy95/Tensorflow-Project-Template',
    'https://github.com/lutris/lutris',
    'https://github.com/santinic/pampy',
    'https://github.com/shobrook/rebound',
    'https://github.com/aziz/PlainTasks',
    'https://github.com/cookiecutter-flask/cookiecutter-flask',
    'https://github.com/hunkim/PyTorchZeroToAll',
    'https://github.com/spadgos/sublime-jsdocs',
    'https://github.com/benedekrozemberczki/awesome-graph-classification',
    'https://github.com/SpiderLabs/Responder',
    'https://github.com/STVIR/pysot',
    'https://github.com/zalando/patroni',
    'https://github.com/timofurrer/maya',
    'https://github.com/guardicore/monkey',
    'https://github.com/drivendata/cookiecutter-data-science',
    'https://github.com/livid/v2ex-gae',
    'https://github.com/andresriancho/w3af',
    'https://github.com/Kaggle/kaggle-api',
    'https://github.com/facebookresearch/pythia',
    'https://github.com/miyakogi/pyppeteer',
    'https://github.com/donnemartin/haxor-news',
    'https://github.com/orakaro/rainbowstream',
    'https://github.com/Netflix/metaflow',
    'https://github.com/CSAILVision/semantic-segmentation-pytorch',
    'https://github.com/not-kennethreitz/osx-gcc-installer',
    'https://github.com/nteract/papermill',
    'https://github.com/tlbootcamp/tlroadmap',
    'https://github.com/MongoEngine/mongoengine',
    'https://github.com/ildoonet/tf-pose-estimation',
    'https://github.com/msracver/Deformable-ConvNets',
    'https://github.com/mantl/mantl',
    'https://github.com/cowrie/cowrie',
    'https://github.com/wal-e/wal-e',
    'https://github.com/python-trio/trio',
    'https://github.com/andabi/deep-voice-conversion',
    'https://github.com/navdeep-G/samplemod',
    'https://github.com/PaddlePaddle/ERNIE',
    'https://github.com/SmirkCao/Lihang',
    'https://github.com/pallets/flask-sqlalchemy',
    'https://github.com/trustedsec/ptf',
    'https://github.com/mstamy2/PyPDF2',
    'https://github.com/astorfi/Deep-Learning-Roadmap',
    'https://github.com/midgetspy/Sick-Beard',
    'https://github.com/espressif/esptool',
    'https://github.com/zalando/connexion',
    'https://github.com/drathier/stack-overflow-import',
    'https://github.com/shenweichen/DeepCTR',
    'https://github.com/christabor/flask_jsondash',
    'https://github.com/jackzhenguo/python-small-examples',
    'https://github.com/wistbean/learn_python3_spider',
    'https://github.com/DanMcInerney/wifijammer',
    'https://github.com/skorch-dev/skorch',
    'https://github.com/python-attrs/attrs',
    'https://github.com/tyiannak/pyAudioAnalysis',
    'https://github.com/gaojiuli/toapi',
    'https://github.com/mongodb/mongo-python-driver',
    'https://github.com/CharlesShang/FastMaskRCNN',
    'https://github.com/yzhao062/pyod',
    'https://github.com/QingdaoU/OnlineJudge',
    'https://github.com/cloudflare/flan',
    'https://github.com/jinfagang/tensorflow_poems',
    'https://github.com/eon01/kubernetes-workshop',
    'https://github.com/Kyubyong/transformer',
    'https://github.com/kstenerud/iOS-Universal-Framework',
    'https://github.com/farizrahman4u/seq2seq',
    'https://github.com/JuanPotato/Legofy',
    'https://github.com/coala/coala',
    'https://github.com/kachayev/fn.py',
    'https://github.com/what-studio/profiling',
    'https://github.com/brython-dev/brython',
    'https://github.com/NTMC-Community/MatchZoo',
    'https://github.com/deepmind/trfl',
    'https://github.com/google/diff-match-patch',
    'https://github.com/Sentdex/pygta5',
    'https://github.com/androguard/androguard',
    'https://github.com/byt3bl33d3r/MITMf',
    'https://github.com/LiuXingMing/SinaSpider',
    'https://github.com/carltongibson/django-filter',
    'https://github.com/Kr1s77/Python-crawler-tutorial-starts-from-zero',
    'https://github.com/run-youngjoo/SC-FEGAN',
    'https://github.com/janeczku/calibre-web',
    'https://github.com/idealo/imagededup',
    'https://github.com/django-haystack/django-haystack',
    'https://github.com/billryan/algorithm-exercise',
    'https://github.com/jaungiers/LSTM-Neural-Network-for-Time-Series-Prediction',
    'https://github.com/joestump/python-oauth2',
    'https://github.com/instantbox/instantbox',
    'https://github.com/jpadilla/django-rest-framework-jwt',
    'https://github.com/yasoob/intermediatePython',
    'https://github.com/llSourcell/learn_math_fast',
    'https://github.com/anishathalye/dotbot',
    'https://github.com/nficano/pytube',
    'https://github.com/ubuntu/microk8s',
    'https://github.com/bear/python-twitter',
    'https://github.com/Avik-Jain/100-Days-of-ML-Code-Chinese-Version',
    'https://github.com/mooz/percol',
    'https://github.com/P0cL4bs/WiFi-Pumpkin',
    'https://github.com/rembo10/headphones',
    'https://github.com/rwightman/pytorch-image-models',
    'https://github.com/theskumar/python-dotenv',
    'https://github.com/jrosebr1/imutils',
    'https://github.com/imWildCat/scylla',
    'https://github.com/scrapinghub/splash',
    'https://github.com/fivesheep/chnroutes',
    'https://github.com/nryoung/algorithms',
    'https://github.com/miguelgrinberg/microblog',
    'https://github.com/coleifer/huey',
    'https://github.com/pytransitions/transitions',
    'https://github.com/bijection/sistine',
    'https://github.com/docker-archive/docker-registry',
    'https://github.com/gaussic/text-classification-cnn-rnn',
    'https://github.com/pypa/pipfile',
    'https://github.com/golemfactory/golem',
    'https://github.com/AKSHAYUBHAT/DeepVideoAnalytics',
    'https://github.com/freedomofpress/securedrop',
    'https://github.com/Instagram/MonkeyType',
    'https://github.com/plasma-disassembler/plasma',
    'https://github.com/blaze/blaze',
    'https://github.com/ryankiros/neural-storyteller',
    'https://github.com/rtqichen/torchdiffeq',
    'https://github.com/rasbt/mlxtend',
    'https://github.com/gbeced/pyalgotrade',
    'https://github.com/kemayo/sublime-text-git',
    'https://github.com/chrissimpkins/Crunch',
    'https://github.com/ownthink/KnowledgeGraphData',
    'https://github.com/easy-tensorflow/easy-tensorflow',
    'https://github.com/thearn/webcam-pulse-detector',
    'https://github.com/elastic/elasticsearch-dsl-py',
    'https://github.com/RocketMap/RocketMap',
    'https://github.com/lawlite19/MachineLearning_Python',
    'https://github.com/Mckinsey666/bullet',
    'https://github.com/SublimeText-Markdown/MarkdownEditing',
    'https://github.com/huyingxi/Synonyms',
    'https://github.com/taki0112/Tensorflow-Cookbook',
    'https://github.com/listen1/listen1',
    'https://github.com/RoganDawes/P4wnP1',
    'https://github.com/omab/python-social-auth',
    'https://github.com/ActivityWatch/activitywatch',
    'https://github.com/hephaest0s/usbkill',
    'https://github.com/ethereon/caffe-tensorflow',
    'https://github.com/r0oth3x49/udemy-dl',
    'https://github.com/joshua-wu/deepfakes_faceswap',
    'https://github.com/pyinvoke/invoke',
    'https://github.com/pypa/sampleproject',
    'https://github.com/caronc/apprise',
    'https://github.com/eragonruan/text-detection-ctpn',
    'https://github.com/madhavanmalolan/awesome-reactnative-ui',
    'https://github.com/eternnoir/pyTelegramBotAPI',
    'https://github.com/hugsy/gef',
    'https://github.com/geopy/geopy',
    'https://github.com/noamraph/tqdm',
    'https://github.com/pybrain/pybrain',
    'https://github.com/qiwsir/algorithm',
    'https://github.com/cloud-custodian/cloud-custodian',
    'https://github.com/jeanphix/Ghost.py',
    'https://github.com/brennerm/PyTricks',
    'https://github.com/madmaze/pytesseract',
    'https://github.com/graphql-python/graphene-django',
    'https://github.com/Qiskit/qiskit-terra',
    'https://github.com/rbgirshick/fast-rcnn',
    'https://github.com/mherrmann/fbs',
    'https://github.com/healthchecks/healthchecks',
    'https://github.com/Luolc/AdaBound',
    'https://github.com/elastic/elasticsearch-py',
    'https://github.com/IDSIA/sacred',
    'https://github.com/goodfeli/adversarial',
    'https://github.com/chineseocr/chineseocr',
    'https://github.com/atlanhq/camelot',
    'https://github.com/shelhamer/fcn.berkeleyvision.org',
    'https://github.com/Greenwolf/social_mapper',
    'https://github.com/bndr/pipreqs',
    'https://github.com/dpgaspar/Flask-AppBuilder',
    'https://github.com/quark0/darts',
    'https://github.com/Julian/jsonschema',
    'https://github.com/cemoody/lda2vec',
    'https://github.com/telepresenceio/telepresence',
    'https://github.com/Wookai/paper-tips-and-tricks',
    'https://github.com/sloria/doitlive',
    'https://github.com/lisa-lab/pylearn2',
    'https://github.com/tmux-python/tmuxp',
    'https://github.com/phodal/awesome-iot',
    'https://github.com/evhub/coconut',
    'https://github.com/0xInfection/Awesome-WAF',
    'https://github.com/kuangliu/pytorch-cifar',
    'https://github.com/timothycrosley/isort',
    'https://github.com/getsentry/responses',
    'https://github.com/OUCMachineLearning/OUCML',
    'https://github.com/roytseng-tw/Detectron.pytorch',
    'https://github.com/PyCQA/pylint',
    'https://github.com/the0demiurge/ShadowSocksShare',
    'https://github.com/LuminosoInsight/python-ftfy',
    'https://github.com/nl8590687/ASRT_SpeechRecognition',
    'https://github.com/Conchylicultor/DeepQA',
    'https://github.com/lk-geimfari/mimesis',
    'https://github.com/geex-arts/django-jet',
    'https://github.com/pwndbg/pwndbg',
    'https://github.com/dabeaz/python-cookbook',
    'https://github.com/ansible-community/molecule',
    'https://github.com/pytorch/ignite',
    'https://github.com/DistrictDataLabs/yellowbrick',
    'https://github.com/xmendez/wfuzz',
    'https://github.com/ecthros/uncaptcha',
    'https://github.com/gitpython-developers/GitPython',
    'https://github.com/pytoolz/toolz',
    'https://github.com/dbolya/yolact',
    'https://github.com/facebookarchive/python-instagram',
    'https://github.com/zzw922cn/Automatic_Speech_Recognition',
    'https://github.com/Nuitka/Nuitka',
    'https://github.com/liangliangyy/DjangoBlog',
    'https://github.com/ysrc/xunfeng',
    'https://github.com/saulpw/visidata',
    'https://github.com/datawire/ambassador',
    'https://github.com/ymcui/Chinese-BERT-wwm',
    'https://github.com/ayooshkathuria/pytorch-yolo-v3',
    'https://github.com/tensorforce/tensorforce',
    'https://github.com/Tencent/tencent-ml-images',
    'https://github.com/soumith/convnet-benchmarks',
    'https://github.com/OpenDroneMap/ODM',
    'https://github.com/kylemcdonald/FreeWifi',
    'https://github.com/CCOSTAN/Home-AssistantConfig',
    'https://github.com/asciimoo/drawille',
    'https://github.com/weskerfoot/DeleteFB',
    'https://github.com/martinarjovsky/WassersteinGAN',
    'https://github.com/geerlingguy/ansible-for-devops',
    'https://github.com/doccano/doccano',
    'https://github.com/anishathalye/git-remote-dropbox',
    'https://github.com/mingrammer/diagrams',
    'https://github.com/googlemaps/google-maps-services-python',
    'https://github.com/elastic/curator',
    'https://github.com/openstack/nova',
    'https://github.com/baowenbo/DAIN',
    'https://github.com/google/gif-for-cli',
    'https://github.com/formspree/formspree',
    'https://github.com/agermanidis/autosub',
    'https://github.com/pritunl/pritunl',
    'https://github.com/0rpc/zerorpc-python',
    'https://github.com/aaugustin/websockets',
    'https://github.com/sherjilozair/char-rnn-tensorflow',
    'https://github.com/mesonbuild/meson',
    'https://github.com/vyperlang/vyper',
    'https://github.com/samuelcolvin/pydantic',
    'https://github.com/ab77/netflix-proxy',
    'https://github.com/ckan/ckan',
    'https://github.com/meetshah1995/pytorch-semseg',
    'https://github.com/slackapi/python-slackclient',
    'https://github.com/douban/dpark',
    'https://github.com/rootphantomer/Blasting_dictionary',
    'https://github.com/freqtrade/freqtrade',
    'https://github.com/facebookresearch/pytorch3d',
    'https://github.com/django-guardian/django-guardian',
    'https://github.com/cysmith/neural-style-tf',
    'https://github.com/LionSec/katoolin',
    'https://github.com/dedupeio/dedupe',
    'https://github.com/x0rz/tweets_analyzer',
    'https://github.com/jisungk/deepjazz',
    'https://github.com/google/nogotofail'
]

for x in range(size):
    repo_path = '/Repos/{}'.format(x)
    if path.exists(repo_path):
        try:
            sbprs = subprocess.Popen("pygount {} --format=summary".format(repo_path),stdout=subprocess.PIPE)
            result = str(sbprs.stdout.read())
            results = result.split("total")
            loc = getTotal(results[1])
            locs.append(loc)
            urls_repo.append(urls[x])
            print("Repositorio {} deu bom!".format(x))
        except:
            locs.append(str(0))
            urls_repo.append(urls[x])
            print("Repositorio {} deu ruim!".format(x))
            continue

createCsv(urls_repo,locs)
print('Repositorios analisados com sucesso')