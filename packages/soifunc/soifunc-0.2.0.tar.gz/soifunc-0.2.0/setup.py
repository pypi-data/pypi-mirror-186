# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['soifunc']

package_data = \
{'': ['*']}

install_requires = \
['vapoursynth>=60', 'vsdeband>=0.7.2', 'vsutil>=0.8.0,<0.9.0']

setup_kwargs = {
    'name': 'soifunc',
    'version': '0.2.0',
    'description': "Soichiro's VapourSynth Functions Collection",
    'long_description': "## soifunc\n\nVapoursynth scripts that might be useful to someone\n\n### Installation\n\n#### Arch Linux\n\nInstall from [AUR](https://aur.archlinux.org/packages/vapoursynth-plugin-soifunc-git)\n\n#### Other\n\nFirst install the required plugins which are not available in pip:\n\n- [neo_f3kdb](https://github.com/HomeOfAviSynthPlusEvolution/neo_f3kdb)\n- [kagefunc](https://github.com/Irrational-Encoding-Wizardry/kagefunc)\n- [muvsfunc](https://github.com/WolframRhodium/muvsfunc)\n- [havsfunc](https://github.com/WolframRhodium/havsfunc)\n- [mvsfunc](https://github.com/HomeOfVapourSynthEvolution/mvsfunc)\n- [znedi3](https://github.com/sekrit-twc/znedi3)\n- [nnedi3_resample](https://github.com/HomeOfVapourSynthEvolution/nnedi3_resample)\n- [BM3DCUDA](https://github.com/WolframRhodium/VapourSynth-BM3DCUDA)\n\nInstall from pip:\n\n```bash\npip install soifunc\n```\n\nOr the latest git version:\n\n```bash\npip install git+https://github.com/shssoichiro/soifunc.git\n```\n\n### Usage\n\nAny of the functions will require an `import soifunc` prior to where they are used.\n\n#### GoodResize\n\n`clip = soifunc.GoodResize(clip, 1920, 1080)`\n\nResizes a clip to the specified dimensions using a high quality method.\n\nFor upscaling, luma is resized using `nnedi3_resample`.\n\nFor downscaling, luma is resized using `SSIM_downsample`.\n\nChroma is always resized using `Spline36`.\n\n**If this filter causes your video to produce a blank output**, see this issue: https://github.com/HomeOfVapourSynthEvolution/VapourSynth-TCanny/issues/14\n\n#### RetinexDeband\n\n`clip = soifunc.RetinexDeband(clip, threshold = 16 [, showmask = False])`\n\nHigh quality debanding using a retinex mask, designed to preserve details in both light and dark areas.\n\n`threshold` controls debanding strength. `16` is a reasonable starting point. Increase as needed until satisfied.\n\n`showmask` is an optional debugging parameter, setting this to `True` will output the mask that will be used to preserve edges.\n\nNote that this debander does not automatically add grain.\nIf you need to add grain before encoding, use `kagefunc.adaptive_grain`.\nIf you're using AV1 grain synthesis, you _do not_ need to add grain before encoding.\n\n#### ClipLimited\n\n`clip = soifunc.ClipLimited(clip)`\n\nCompression introduces rounding errors and whatnot that can lead\nto some pixels in your source being outside the range of\nvalid Limited range values. These are clamped to the valid\nrange by the player on playback, but that means we can save\na small amount of bitrate if we clamp them at encode time.\nThis function does that.\n\nRecommended to use at the very end of your filter chain,\nin the final encode bit depth.\n\n#### BM3DCUDA Wrappers\n\nSee [BM3DCUDA](https://github.com/WolframRhodium/VapourSynth-BM3DCUDA) for list of args.\n\n`clip = soifunc.BM3DCPU(clip, ...args)`\n\n`clip = soifunc.BM3DCuda(clip, ...args)`\n\n`clip = soifunc.BM3DCuda_RTC(clip, ...args)`\n\nProvides wrappers around the accelerated BM3D functions in BM3DCUDA, similar to the wrapper provided for the base BM3D plugin in mvsfunc.\nThese functions perform all necessary colorspace conversion, so they are considerably simpler to use than manually calling BM3DCuda.\n\n#### MCDenoise\n\nApplies motion compensation to a denoised clip to improve detail preservation.\nCredit to Clybius for creating this code.\n\nExample usage:\n\n```python\nimport soifunc\nimport dfttest2\nimport functools    # functools is built in to python\ndenoiser = functools.partial(dfttest2.DFTTest, sigma=1.5, backend=dfttest2.Backend.CPU)\nclip = soifunc.MCDenoise(clip, denoiser)\n```\n\nParams:\n\n- `denoiser`: A function defining how to denoise the motion-compensated frames.\n  Denoiser params can be added using `functools.partial`.\n- `prefilter`: An optional prefiltered input clip to enable better searching for motion vectors\n",
    'author': 'Josh Holmer',
    'author_email': 'jholmer.in@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
