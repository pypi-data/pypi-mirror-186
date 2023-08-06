# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['soccertrack',
 'soccertrack.camera',
 'soccertrack.dataframe',
 'soccertrack.datasets',
 'soccertrack.detection_model',
 'soccertrack.image_model',
 'soccertrack.io',
 'soccertrack.metrics',
 'soccertrack.tracking_model',
 'soccertrack.utils']

package_data = \
{'': ['*']}

install_requires = \
['ffmpeg-python>=0.2.0,<0.3.0',
 'furo>=2022.6.21,<2023.0.0',
 'ipython>=8.5.0,<9.0.0',
 'ipywidgets>=8.0.4,<9.0.0',
 'jupyter>=1.0.0,<2.0.0',
 'kaggle>=1.5.12,<2.0.0',
 'loguru>=0.6.0,<0.7.0',
 'mplsoccer>=1.1.10,<2.0.0',
 'nbsphinx>=0.8.9,<0.9.0',
 'numpy>=1.22.4,<2.0.0',
 'omegaconf>=2.2.2,<3.0.0',
 'opencv-contrib-python>=4.6.0,<5.0.0',
 'pandas>=1.4.2,<2.0.0',
 'poetry[seedir]>=1.3.1,<2.0.0',
 'pytest>=7.1.2,<8.0.0',
 'rich>=12.5.1,<13.0.0',
 'scikit-video>=1.1.11,<2.0.0',
 'scipy>=1.8.1,<2.0.0',
 'seedir>=0.4.2,<0.5.0',
 'sphinx-autodoc-typehints>=1.20.1,<2.0.0',
 'vidgear>=0.2.6,<0.3.0']

setup_kwargs = {
    'name': 'soccertrack',
    'version': '0.1.0',
    'description': 'A dataset and algorithm for multi-object tracking in sports',
    'long_description': '# SoccerTrack\n\n![](https://raw.githubusercontent.com/AtomScott/SoccerTrack/gh-pages/img/title-banner.png)\n\n[![Documentation Status](https://readthedocs.org/projects/soccertrack/badge/?version=latest)](https://soccertrack.readthedocs.io/en/latest/?badge=latest) \n[![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/datasets/atomscott/soccertrack)\n[![PWC](https://img.shields.io/badge/%7C-Papers%20with%20Code-lightblue)](https://paperswithcode.com/dataset/soccertrack-dataset)\n\n[![DeepSource](https://deepsource.io/gh/AtomScott/SoccerTrack.svg/?label=active+issues&show_trend=true&token=TIxJg8BLzszYnWeVDMHr6pMU)](https://deepsource.io/gh/AtomScott/SoccerTrack/?ref=repository-badge)\n[![DeepSource](https://deepsource.io/gh/AtomScott/SoccerTrack.svg/?label=resolved+issues&show_trend=true&token=TIxJg8BLzszYnWeVDMHr6pMU)](https://deepsource.io/gh/AtomScott/SoccerTrack/?ref=repository-badge)\n\n**[IMPORTANT (2022/11/03)]**\n\nAfter receving reports of erroneous  data, we have fixed and reuploaded a majority of SoccerTrack. We are also adding videos with visualized bounding boxes so that you can be sure that the data is good. The visualizations can be found in the viz_results directory under Top-view/Wide-view (see [Kaggle](https://www.kaggle.com/datasets/atomscott/soccertrack)).\n\nHowever, there is still work to do. In the meantime, we have created a spreadsheet to keep everyone updated on our progress.\n[Spreadsheet Link](https://docs.google.com/spreadsheets/d/1V4TF84nIZWtYBrT6oNhAc3tp01QCBn41aadp96vfWww/edit#gid=208157415)\n\n---\nA Dataset and Tracking Algorithm for Soccer with Fish-eye and Drone Videos.\n\n\n* [Project page](https://atomscott.github.io/SoccerTrack/)\n* [Paper](https://openaccess.thecvf.com/content/CVPR2022W/CVSports/papers/Scott_SoccerTrack_A_Dataset_and_Tracking_Algorithm_for_Soccer_With_Fish-Eye_CVPRW_2022_paper.pdf)\n* [Dataset Download](https://atomscott.github.io/SoccerTrack/#download) 🌟 NEW\n* [Tracking Algorithm](https://github.com/AtomScott/SoccerTrack) (Work In Progress)\n* [Documentation](https://soccertrack.readthedocs.io/) (Work In Progress)\n\n\n## Dataset Details\n\n -/- | **Wide-View Camera** | **Top-View Camera** | **GNSS** \n---|---|---|---\n Device | Z CAM E2-F8 | DJI Mavic 3 | STATSPORTS APEX 10 Hz \n Resolution | 8K (7,680 × 4,320 pixel) | 4K (3,840 × 2,160 pixesl) | Abs. err. in 20-m run: 0.22 ± 0.20 m  \n FPS | 30 | 30 | 10 \n Player tracking | ✅ | ✅ | ✅ \n Ball tracking | ✅ | ✅ | - \n Bounding box | ✅ | ✅ | - \n Location data | ✅ | ✅ | ✅ \n Player ID | ✅ | ✅ | ✅\n\nAll data in SoccerTrack was obtained from 11-vs-11 soccer games between college-aged athletes. Measurements were conducted after we received the approval of Tsukuba university’s ethics committee, and all participants provided signed informed permission. After recording several soccer matches, the videos were semi-automatically annotated based on the GNSS coordinates of each player.\n\nBelow are low resolution samples from the soccertrack dataset we plan to release. The actual dataset will contains (drone) and 8K (fisheye) footage!\n\n### Drone Video\n\n<video style=\'max-width:640px\' controls>\n  <source src="https://user-images.githubusercontent.com/22371492/178085041-a8a2de85-bcd3-4c81-8b81-5ca93dbd4336.mp4" type="video/mp4">\n</video>\n\nhttps://user-images.githubusercontent.com/22371492/178085041-a8a2de85-bcd3-4c81-8b81-5ca93dbd4336.mp4\n\n### Fisheye Video\n<video style=\'max-width:640px\' controls>\n  <source src="https://user-images.githubusercontent.com/22371492/178085027-5d25781d-e3ed-4791-ad14-141b58187dcf.mp4" type="video/mp4">\n</video>\n\nhttps://user-images.githubusercontent.com/22371492/178085027-5d25781d-e3ed-4791-ad14-141b58187dcf.mp4\n\n\n> **Note** The resolution for the fisheye camera may change after calibration.\n\n## Dataset Download\n\nThe SoccerTrack Dataset is available to download from the links below!\n\n* [Top-view](https://drive.google.com/drive/folders/12rasAk-52YSAwReJNIlTZIa794UhRU4J?usp=sharing)\n* [Wide-view](https://drive.google.com/drive/folders/1XgrPHBYnz-LOB2vZsB4koVUMgjl_gwqF?usp=sharing)\n* [GNSS data](https://drive.google.com/drive/folders/15i4GJ1Rl5rwnOOuHv34Ar1K8wxKifnIJ?usp=sharing)\n\nFor more details on how to use the dataset, please see the section "[Dataset Preparation](https://soccertrack.readthedocs.io/en/latest/01_get_started/dataset_preparation.html)".\n\n## Docker\n\n[Dockerhub](https://hub.docker.com/repository/docker/atomscott/soccertrack)\n\n## Contributing\n\nSee the [Contributing Guide](https://soccertrack.readthedocs.io/en/latest/contributing.html) for more information.\n\n## Papers\n\n<table>\n<td width=30% style=\'padding: 20px;\'>\n<a href="https://openaccess.thecvf.com/content/CVPR2022W/CVSports/papers/Scott_SoccerTrack_A_Dataset_and_Tracking_Algorithm_for_Soccer_With_Fish-Eye_CVPRW_2022_paper.pdf">\n<img src=\'https://raw.githubusercontent.com/AtomScott/SoccerTrack/feature/major_refactor/docs/_static/paper_preview.jpg\'/>\n</a>\n</td>\n<td width=70%>\n  <p>\n    <b>SoccerTrack:</b><br>\n    A Dataset and Tracking Algorithm for Soccer with Fish-eye and Drone Videos\n  </p>\n  <p>\n    Atom Scott*, Ikuma Uchida*, Masaki Onishi, Yoshinari Kameda, Kazuhiro Fukui, Keisuke Fujii\n  </p>\n  <p>\n    <i> Presented at CVPR Workshop on Computer Vision for Sports (CVSports\'22). *Authors contributed equally. </i>\n  </p>\n  <div>\n    <a href=\'https://openaccess.thecvf.com/content/CVPR2022W/CVSports/papers/Scott_SoccerTrack_A_Dataset_and_Tracking_Algorithm_for_Soccer_With_Fish-Eye_CVPRW_2022_paper.pdf\'>\n      <img src=\'https://img.shields.io/badge/Paper-PDF-red?style=for-the-badge&logo=adobe-acrobat-reader\'/>\n    </a>\n    <a href=\'https://github.com/AtomScott/SoccerTrack\'>\n      <img src=\'https://img.shields.io/badge/Code-Page-blue?style=for-the-badge&logo=github\'/>\n    </a>\n    <a href=\'https://soccertrack.readthedocs.io/\'>\n      <img src=\'https://img.shields.io/badge/Documentation-Page-blue?style=for-the-badge&logo=read-the-docs\'/>\n    </a>\n  </div>\n</td>\n</table>\n\n## Citation\n```\n@inproceedings{scott2022soccertrack,\n  title={SoccerTrack: A Dataset and Tracking Algorithm for Soccer With Fish-Eye and Drone Videos},\n  author={Scott, Atom and Uchida, Ikuma and Onishi, Masaki and Kameda, Yoshinari and Fukui, Kazuhiro and Fujii, Keisuke},\n  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},\n  pages={3569--3579},\n  year={2022}\n}\n```\n\n## Acknowledgements\n\nPart of the tracking module has been adapted from [motpy](https://github.com/wmuron/motpy). We would like to thank the authors for their work.\n\n## Star History\n\n[![Star History Chart](https://api.star-history.com/svg?repos=atomscott/soccertrack&type=Date)](https://star-history.com/#atomscott/soccertrack&Date)\n',
    'author': 'Atom Scott',
    'author_email': 'atom.james.scott@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
