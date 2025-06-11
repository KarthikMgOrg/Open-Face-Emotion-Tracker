
```
Open-Face-DRF-Api
├─ core
│  ├─ __init__.py
│  ├─ __pycache__
│  │  ├─ __init__.cpython-311.pyc
│  │  └─ settings.cpython-311.pyc
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ kafka
│  ├─ consumer
│  ├─ docker-compose.yml
│  └─ producer
├─ manage.py
├─ openface
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  ├─ utils
│  │  ├─ feature_extraction.py
│  │  └─ kafka
│  │     ├─ consumer.py
│  │     └─ producer.py
│  └─ views.py
├─ requirements.txt
└─ venv
   ├─ bin
   │  ├─ Activate.ps1
   │  ├─ activate
   │  ├─ activate.csh
   │  ├─ activate.fish
   │  ├─ django-admin
   │  ├─ f2py
   │  ├─ jsonschema
   │  ├─ normalizer
   │  ├─ numpy-config
   │  ├─ pip
   │  ├─ pip3
   │  ├─ pip3.11
   │  ├─ python
   │  ├─ python3
   │  ├─ python3.11
   │  ├─ sqlformat
   │  ├─ streamlit
   │  └─ streamlit.cmd
   ├─ etc
   │  └─ jupyter
   │     └─ nbconfig
   │        └─ notebook.d
   │           └─ pydeck.json
   ├─ include
   │  └─ python3.11
   ├─ lib
   │  └─ python3.11
   │     └─ site-packages
   │        ├─ .DS_Store
   │        ├─ GitPython-3.1.44.dist-info
   │        │  ├─ AUTHORS
   │        │  ├─ INSTALLER
   │        │  ├─ LICENSE
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  └─ top_level.txt
   │        ├─ MarkupSafe-3.0.2.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ LICENSE.txt
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  └─ top_level.txt
   │        ├─ PIL
   │        │  ├─ .dylibs
   │        │  │  ├─ libXau.6.dylib
   │        │  │  ├─ libbrotlicommon.1.1.0.dylib
   │        │  │  ├─ libbrotlidec.1.1.0.dylib
   │        │  │  ├─ libfreetype.6.dylib
   │        │  │  ├─ libharfbuzz.0.dylib
   │        │  │  ├─ libjpeg.62.4.0.dylib
   │        │  │  ├─ liblcms2.2.dylib
   │        │  │  ├─ liblzma.5.dylib
   │        │  │  ├─ libopenjp2.2.5.3.dylib
   │        │  │  ├─ libpng16.16.dylib
   │        │  │  ├─ libsharpyuv.0.dylib
   │        │  │  ├─ libtiff.6.dylib
   │        │  │  ├─ libwebp.7.dylib
   │        │  │  ├─ libwebpdemux.2.dylib
   │        │  │  ├─ libwebpmux.3.dylib
   │        │  │  ├─ libxcb.1.1.0.dylib
   │        │  │  └─ libz.1.3.1.zlib-ng.dylib
   │        │  ├─ AvifImagePlugin.py
   │        │  ├─ BdfFontFile.py
   │        │  ├─ BlpImagePlugin.py
   │        │  ├─ BmpImagePlugin.py
   │        │  ├─ BufrStubImagePlugin.py
   │        │  ├─ ContainerIO.py
   │        │  ├─ CurImagePlugin.py
   │        │  ├─ DcxImagePlugin.py
   │        │  ├─ DdsImagePlugin.py
   │        │  ├─ EpsImagePlugin.py
   │        │  ├─ ExifTags.py
   │        │  ├─ FitsImagePlugin.py
   │        │  ├─ FliImagePlugin.py
   │        │  ├─ FontFile.py
   │        │  ├─ FpxImagePlugin.py
   │        │  ├─ FtexImagePlugin.py
   │        │  ├─ GbrImagePlugin.py
   │        │  ├─ GdImageFile.py
   │        │  ├─ GifImagePlugin.py
   │        │  ├─ GimpGradientFile.py
   │        │  ├─ GimpPaletteFile.py
   │        │  ├─ GribStubImagePlugin.py
   │        │  ├─ Hdf5StubImagePlugin.py
   │        │  ├─ IcnsImagePlugin.py
   │        │  ├─ IcoImagePlugin.py
   │        │  ├─ ImImagePlugin.py
   │        │  ├─ Image.py
   │        │  ├─ ImageChops.py
   │        │  ├─ ImageCms.py
   │        │  ├─ ImageColor.py
   │        │  ├─ ImageDraw.py
   │        │  ├─ ImageDraw2.py
   │        │  ├─ ImageEnhance.py
   │        │  ├─ ImageFile.py
   │        │  ├─ ImageFilter.py
   │        │  ├─ ImageFont.py
   │        │  ├─ ImageGrab.py
   │        │  ├─ ImageMath.py
   │        │  ├─ ImageMode.py
   │        │  ├─ ImageMorph.py
   │        │  ├─ ImageOps.py
   │        │  ├─ ImagePalette.py
   │        │  ├─ ImagePath.py
   │        │  ├─ ImageQt.py
   │        │  ├─ ImageSequence.py
   │        │  ├─ ImageShow.py
   │        │  ├─ ImageStat.py
   │        │  ├─ ImageTk.py
   │        │  ├─ ImageTransform.py
   │        │  ├─ ImageWin.py
   │        │  ├─ ImtImagePlugin.py
   │        │  ├─ IptcImagePlugin.py
   │        │  ├─ Jpeg2KImagePlugin.py
   │        │  ├─ JpegImagePlugin.py
   │        │  ├─ JpegPresets.py
   │        │  ├─ McIdasImagePlugin.py
   │        │  ├─ MicImagePlugin.py
   │        │  ├─ MpegImagePlugin.py
   │        │  ├─ MpoImagePlugin.py
   │        │  ├─ MspImagePlugin.py
   │        │  ├─ PSDraw.py
   │        │  ├─ PaletteFile.py
   │        │  ├─ PalmImagePlugin.py
   │        │  ├─ PcdImagePlugin.py
   │        │  ├─ PcfFontFile.py
   │        │  ├─ PcxImagePlugin.py
   │        │  ├─ PdfImagePlugin.py
   │        │  ├─ PdfParser.py
   │        │  ├─ PixarImagePlugin.py
   │        │  ├─ PngImagePlugin.py
   │        │  ├─ PpmImagePlugin.py
   │        │  ├─ PsdImagePlugin.py
   │        │  ├─ QoiImagePlugin.py
   │        │  ├─ SgiImagePlugin.py
   │        │  ├─ SpiderImagePlugin.py
   │        │  ├─ SunImagePlugin.py
   │        │  ├─ TarIO.py
   │        │  ├─ TgaImagePlugin.py
   │        │  ├─ TiffImagePlugin.py
   │        │  ├─ TiffTags.py
   │        │  ├─ WalImageFile.py
   │        │  ├─ WebPImagePlugin.py
   │        │  ├─ WmfImagePlugin.py
   │        │  ├─ XVThumbImagePlugin.py
   │        │  ├─ XbmImagePlugin.py
   │        │  ├─ XpmImagePlugin.py
   │        │  ├─ __init__.py
   │        │  ├─ __main__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ AvifImagePlugin.cpython-311.pyc
   │        │  │  ├─ BdfFontFile.cpython-311.pyc
   │        │  │  ├─ BlpImagePlugin.cpython-311.pyc
   │        │  │  ├─ BmpImagePlugin.cpython-311.pyc
   │        │  │  ├─ BufrStubImagePlugin.cpython-311.pyc
   │        │  │  ├─ ContainerIO.cpython-311.pyc
   │        │  │  ├─ CurImagePlugin.cpython-311.pyc
   │        │  │  ├─ DcxImagePlugin.cpython-311.pyc
   │        │  │  ├─ DdsImagePlugin.cpython-311.pyc
   │        │  │  ├─ EpsImagePlugin.cpython-311.pyc
   │        │  │  ├─ ExifTags.cpython-311.pyc
   │        │  │  ├─ FitsImagePlugin.cpython-311.pyc
   │        │  │  ├─ FliImagePlugin.cpython-311.pyc
   │        │  │  ├─ FontFile.cpython-311.pyc
   │        │  │  ├─ FpxImagePlugin.cpython-311.pyc
   │        │  │  ├─ FtexImagePlugin.cpython-311.pyc
   │        │  │  ├─ GbrImagePlugin.cpython-311.pyc
   │        │  │  ├─ GdImageFile.cpython-311.pyc
   │        │  │  ├─ GifImagePlugin.cpython-311.pyc
   │        │  │  ├─ GimpGradientFile.cpython-311.pyc
   │        │  │  ├─ GimpPaletteFile.cpython-311.pyc
   │        │  │  ├─ GribStubImagePlugin.cpython-311.pyc
   │        │  │  ├─ Hdf5StubImagePlugin.cpython-311.pyc
   │        │  │  ├─ IcnsImagePlugin.cpython-311.pyc
   │        │  │  ├─ IcoImagePlugin.cpython-311.pyc
   │        │  │  ├─ ImImagePlugin.cpython-311.pyc
   │        │  │  ├─ Image.cpython-311.pyc
   │        │  │  ├─ ImageChops.cpython-311.pyc
   │        │  │  ├─ ImageCms.cpython-311.pyc
   │        │  │  ├─ ImageColor.cpython-311.pyc
   │        │  │  ├─ ImageDraw.cpython-311.pyc
   │        │  │  ├─ ImageDraw2.cpython-311.pyc
   │        │  │  ├─ ImageEnhance.cpython-311.pyc
   │        │  │  ├─ ImageFile.cpython-311.pyc
   │        │  │  ├─ ImageFilter.cpython-311.pyc
   │        │  │  ├─ ImageFont.cpython-311.pyc
   │        │  │  ├─ ImageGrab.cpython-311.pyc
   │        │  │  ├─ ImageMath.cpython-311.pyc
   │        │  │  ├─ ImageMode.cpython-311.pyc
   │        │  │  ├─ ImageMorph.cpython-311.pyc
   │        │  │  ├─ ImageOps.cpython-311.pyc
   │        │  │  ├─ ImagePalette.cpython-311.pyc
   │        │  │  ├─ ImagePath.cpython-311.pyc
   │        │  │  ├─ ImageQt.cpython-311.pyc
   │        │  │  ├─ ImageSequence.cpython-311.pyc
   │        │  │  ├─ ImageShow.cpython-311.pyc
   │        │  │  ├─ ImageStat.cpython-311.pyc
   │        │  │  ├─ ImageTk.cpython-311.pyc
   │        │  │  ├─ ImageTransform.cpython-311.pyc
   │        │  │  ├─ ImageWin.cpython-311.pyc
   │        │  │  ├─ ImtImagePlugin.cpython-311.pyc
   │        │  │  ├─ IptcImagePlugin.cpython-311.pyc
   │        │  │  ├─ Jpeg2KImagePlugin.cpython-311.pyc
   │        │  │  ├─ JpegImagePlugin.cpython-311.pyc
   │        │  │  ├─ JpegPresets.cpython-311.pyc
   │        │  │  ├─ McIdasImagePlugin.cpython-311.pyc
   │        │  │  ├─ MicImagePlugin.cpython-311.pyc
   │        │  │  ├─ MpegImagePlugin.cpython-311.pyc
   │        │  │  ├─ MpoImagePlugin.cpython-311.pyc
   │        │  │  ├─ MspImagePlugin.cpython-311.pyc
   │        │  │  ├─ PSDraw.cpython-311.pyc
   │        │  │  ├─ PaletteFile.cpython-311.pyc
   │        │  │  ├─ PalmImagePlugin.cpython-311.pyc
   │        │  │  ├─ PcdImagePlugin.cpython-311.pyc
   │        │  │  ├─ PcfFontFile.cpython-311.pyc
   │        │  │  ├─ PcxImagePlugin.cpython-311.pyc
   │        │  │  ├─ PdfImagePlugin.cpython-311.pyc
   │        │  │  ├─ PdfParser.cpython-311.pyc
   │        │  │  ├─ PixarImagePlugin.cpython-311.pyc
   │        │  │  ├─ PngImagePlugin.cpython-311.pyc
   │        │  │  ├─ PpmImagePlugin.cpython-311.pyc
   │        │  │  ├─ PsdImagePlugin.cpython-311.pyc
   │        │  │  ├─ QoiImagePlugin.cpython-311.pyc
   │        │  │  ├─ SgiImagePlugin.cpython-311.pyc
   │        │  │  ├─ SpiderImagePlugin.cpython-311.pyc
   │        │  │  ├─ SunImagePlugin.cpython-311.pyc
   │        │  │  ├─ TarIO.cpython-311.pyc
   │        │  │  ├─ TgaImagePlugin.cpython-311.pyc
   │        │  │  ├─ TiffImagePlugin.cpython-311.pyc
   │        │  │  ├─ TiffTags.cpython-311.pyc
   │        │  │  ├─ WalImageFile.cpython-311.pyc
   │        │  │  ├─ WebPImagePlugin.cpython-311.pyc
   │        │  │  ├─ WmfImagePlugin.cpython-311.pyc
   │        │  │  ├─ XVThumbImagePlugin.cpython-311.pyc
   │        │  │  ├─ XbmImagePlugin.cpython-311.pyc
   │        │  │  ├─ XpmImagePlugin.cpython-311.pyc
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ __main__.cpython-311.pyc
   │        │  │  ├─ _binary.cpython-311.pyc
   │        │  │  ├─ _deprecate.cpython-311.pyc
   │        │  │  ├─ _tkinter_finder.cpython-311.pyc
   │        │  │  ├─ _typing.cpython-311.pyc
   │        │  │  ├─ _util.cpython-311.pyc
   │        │  │  ├─ _version.cpython-311.pyc
   │        │  │  ├─ features.cpython-311.pyc
   │        │  │  └─ report.cpython-311.pyc
   │        │  ├─ _avif.pyi
   │        │  ├─ _binary.py
   │        │  ├─ _deprecate.py
   │        │  ├─ _imaging.cpython-311-darwin.so
   │        │  ├─ _imaging.pyi
   │        │  ├─ _imagingcms.cpython-311-darwin.so
   │        │  ├─ _imagingcms.pyi
   │        │  ├─ _imagingft.cpython-311-darwin.so
   │        │  ├─ _imagingft.pyi
   │        │  ├─ _imagingmath.cpython-311-darwin.so
   │        │  ├─ _imagingmath.pyi
   │        │  ├─ _imagingmorph.cpython-311-darwin.so
   │        │  ├─ _imagingmorph.pyi
   │        │  ├─ _imagingtk.cpython-311-darwin.so
   │        │  ├─ _imagingtk.pyi
   │        │  ├─ _tkinter_finder.py
   │        │  ├─ _typing.py
   │        │  ├─ _util.py
   │        │  ├─ _version.py
   │        │  ├─ _webp.cpython-311-darwin.so
   │        │  ├─ _webp.pyi
   │        │  ├─ features.py
   │        │  ├─ py.typed
   │        │  └─ report.py
   │        ├─ __pycache__
   │        │  ├─ six.cpython-311.pyc
   │        │  └─ typing_extensions.cpython-311.pyc
   │        ├─ _distutils_hack
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  └─ override.cpython-311.pyc
   │        │  └─ override.py
   │        ├─ altair
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ _magics.cpython-311.pyc
   │        │  │  └─ theme.cpython-311.pyc
   │        │  ├─ _magics.py
   │        │  ├─ expr
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ consts.cpython-311.pyc
   │        │  │  │  ├─ core.cpython-311.pyc
   │        │  │  │  └─ funcs.cpython-311.pyc
   │        │  │  ├─ consts.py
   │        │  │  ├─ core.py
   │        │  │  └─ funcs.py
   │        │  ├─ jupyter
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  └─ jupyter_chart.cpython-311.pyc
   │        │  │  ├─ js
   │        │  │  │  ├─ README.md
   │        │  │  │  └─ index.js
   │        │  │  └─ jupyter_chart.py
   │        │  ├─ py.typed
   │        │  ├─ theme.py
   │        │  ├─ typing
   │        │  │  ├─ __init__.py
   │        │  │  └─ __pycache__
   │        │  │     └─ __init__.cpython-311.pyc
   │        │  ├─ utils
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _dfi_types.cpython-311.pyc
   │        │  │  │  ├─ _importers.cpython-311.pyc
   │        │  │  │  ├─ _show.cpython-311.pyc
   │        │  │  │  ├─ _transformed_data.cpython-311.pyc
   │        │  │  │  ├─ _vegafusion_data.cpython-311.pyc
   │        │  │  │  ├─ compiler.cpython-311.pyc
   │        │  │  │  ├─ core.cpython-311.pyc
   │        │  │  │  ├─ data.cpython-311.pyc
   │        │  │  │  ├─ deprecation.cpython-311.pyc
   │        │  │  │  ├─ display.cpython-311.pyc
   │        │  │  │  ├─ execeval.cpython-311.pyc
   │        │  │  │  ├─ html.cpython-311.pyc
   │        │  │  │  ├─ mimebundle.cpython-311.pyc
   │        │  │  │  ├─ plugin_registry.cpython-311.pyc
   │        │  │  │  ├─ save.cpython-311.pyc
   │        │  │  │  ├─ schemapi.cpython-311.pyc
   │        │  │  │  ├─ selection.cpython-311.pyc
   │        │  │  │  └─ server.cpython-311.pyc
   │        │  │  ├─ _dfi_types.py
   │        │  │  ├─ _importers.py
   │        │  │  ├─ _show.py
   │        │  │  ├─ _transformed_data.py
   │        │  │  ├─ _vegafusion_data.py
   │        │  │  ├─ compiler.py
   │        │  │  ├─ core.py
   │        │  │  ├─ data.py
   │        │  │  ├─ deprecation.py
   │        │  │  ├─ display.py
   │        │  │  ├─ execeval.py
   │        │  │  ├─ html.py
   │        │  │  ├─ mimebundle.py
   │        │  │  ├─ plugin_registry.py
   │        │  │  ├─ save.py
   │        │  │  ├─ schemapi.py
   │        │  │  ├─ selection.py
   │        │  │  └─ server.py
   │        │  └─ vegalite
   │        │     ├─ __init__.py
   │        │     ├─ __pycache__
   │        │     │  ├─ __init__.cpython-311.pyc
   │        │     │  ├─ api.cpython-311.pyc
   │        │     │  ├─ data.cpython-311.pyc
   │        │     │  ├─ display.cpython-311.pyc
   │        │     │  └─ schema.cpython-311.pyc
   │        │     ├─ api.py
   │        │     ├─ data.py
   │        │     ├─ display.py
   │        │     ├─ schema.py
   │        │     └─ v5
   │        │        ├─ __init__.py
   │        │        ├─ __pycache__
   │        │        │  ├─ __init__.cpython-311.pyc
   │        │        │  ├─ api.cpython-311.pyc
   │        │        │  ├─ compiler.cpython-311.pyc
   │        │        │  ├─ data.cpython-311.pyc
   │        │        │  ├─ display.cpython-311.pyc
   │        │        │  └─ theme.cpython-311.pyc
   │        │        ├─ api.py
   │        │        ├─ compiler.py
   │        │        ├─ data.py
   │        │        ├─ display.py
   │        │        ├─ schema
   │        │        │  ├─ __init__.py
   │        │        │  ├─ __pycache__
   │        │        │  │  ├─ __init__.cpython-311.pyc
   │        │        │  │  ├─ _config.cpython-311.pyc
   │        │        │  │  ├─ _typing.cpython-311.pyc
   │        │        │  │  ├─ channels.cpython-311.pyc
   │        │        │  │  ├─ core.cpython-311.pyc
   │        │        │  │  └─ mixins.cpython-311.pyc
   │        │        │  ├─ _config.py
   │        │        │  ├─ _typing.py
   │        │        │  ├─ channels.py
   │        │        │  ├─ core.py
   │        │        │  ├─ mixins.py
   │        │        │  ├─ vega-lite-schema.json
   │        │        │  └─ vega-themes.json
   │        │        └─ theme.py
   │        ├─ altair-5.5.0.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  └─ licenses
   │        │     └─ LICENSE
   │        ├─ asgiref
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ compatibility.cpython-311.pyc
   │        │  │  ├─ current_thread_executor.cpython-311.pyc
   │        │  │  ├─ local.cpython-311.pyc
   │        │  │  ├─ server.cpython-311.pyc
   │        │  │  ├─ sync.cpython-311.pyc
   │        │  │  ├─ testing.cpython-311.pyc
   │        │  │  ├─ timeout.cpython-311.pyc
   │        │  │  ├─ typing.cpython-311.pyc
   │        │  │  └─ wsgi.cpython-311.pyc
   │        │  ├─ compatibility.py
   │        │  ├─ current_thread_executor.py
   │        │  ├─ local.py
   │        │  ├─ py.typed
   │        │  ├─ server.py
   │        │  ├─ sync.py
   │        │  ├─ testing.py
   │        │  ├─ timeout.py
   │        │  ├─ typing.py
   │        │  └─ wsgi.py
   │        ├─ asgiref-3.8.1.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ LICENSE
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ WHEEL
   │        │  └─ top_level.txt
   │        ├─ attr
   │        │  ├─ __init__.py
   │        │  ├─ __init__.pyi
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ _cmp.cpython-311.pyc
   │        │  │  ├─ _compat.cpython-311.pyc
   │        │  │  ├─ _config.cpython-311.pyc
   │        │  │  ├─ _funcs.cpython-311.pyc
   │        │  │  ├─ _make.cpython-311.pyc
   │        │  │  ├─ _next_gen.cpython-311.pyc
   │        │  │  ├─ _version_info.cpython-311.pyc
   │        │  │  ├─ converters.cpython-311.pyc
   │        │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  ├─ filters.cpython-311.pyc
   │        │  │  ├─ setters.cpython-311.pyc
   │        │  │  └─ validators.cpython-311.pyc
   │        │  ├─ _cmp.py
   │        │  ├─ _cmp.pyi
   │        │  ├─ _compat.py
   │        │  ├─ _config.py
   │        │  ├─ _funcs.py
   │        │  ├─ _make.py
   │        │  ├─ _next_gen.py
   │        │  ├─ _typing_compat.pyi
   │        │  ├─ _version_info.py
   │        │  ├─ _version_info.pyi
   │        │  ├─ converters.py
   │        │  ├─ converters.pyi
   │        │  ├─ exceptions.py
   │        │  ├─ exceptions.pyi
   │        │  ├─ filters.py
   │        │  ├─ filters.pyi
   │        │  ├─ py.typed
   │        │  ├─ setters.py
   │        │  ├─ setters.pyi
   │        │  ├─ validators.py
   │        │  └─ validators.pyi
   │        ├─ attrs
   │        │  ├─ __init__.py
   │        │  ├─ __init__.pyi
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ converters.cpython-311.pyc
   │        │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  ├─ filters.cpython-311.pyc
   │        │  │  ├─ setters.cpython-311.pyc
   │        │  │  └─ validators.cpython-311.pyc
   │        │  ├─ converters.py
   │        │  ├─ exceptions.py
   │        │  ├─ filters.py
   │        │  ├─ py.typed
   │        │  ├─ setters.py
   │        │  └─ validators.py
   │        ├─ attrs-25.3.0.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  └─ licenses
   │        │     └─ LICENSE
   │        ├─ blinker
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ _utilities.cpython-311.pyc
   │        │  │  └─ base.cpython-311.pyc
   │        │  ├─ _utilities.py
   │        │  ├─ base.py
   │        │  └─ py.typed
   │        ├─ blinker-1.9.0.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ LICENSE.txt
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  └─ WHEEL
   │        ├─ cachetools
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ _decorators.cpython-311.pyc
   │        │  │  ├─ func.cpython-311.pyc
   │        │  │  └─ keys.cpython-311.pyc
   │        │  ├─ _decorators.py
   │        │  ├─ func.py
   │        │  └─ keys.py
   │        ├─ cachetools-5.5.2.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ LICENSE
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  └─ top_level.txt
   │        ├─ certifi
   │        │  ├─ __init__.py
   │        │  ├─ __main__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ __main__.cpython-311.pyc
   │        │  │  └─ core.cpython-311.pyc
   │        │  ├─ cacert.pem
   │        │  ├─ core.py
   │        │  └─ py.typed
   │        ├─ certifi-2025.4.26.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  ├─ licenses
   │        │  │  └─ LICENSE
   │        │  └─ top_level.txt
   │        ├─ charset_normalizer
   │        │  ├─ __init__.py
   │        │  ├─ __main__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ __main__.cpython-311.pyc
   │        │  │  ├─ api.cpython-311.pyc
   │        │  │  ├─ cd.cpython-311.pyc
   │        │  │  ├─ constant.cpython-311.pyc
   │        │  │  ├─ legacy.cpython-311.pyc
   │        │  │  ├─ md.cpython-311.pyc
   │        │  │  ├─ models.cpython-311.pyc
   │        │  │  ├─ utils.cpython-311.pyc
   │        │  │  └─ version.cpython-311.pyc
   │        │  ├─ api.py
   │        │  ├─ cd.py
   │        │  ├─ cli
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __main__.py
   │        │  │  └─ __pycache__
   │        │  │     ├─ __init__.cpython-311.pyc
   │        │  │     └─ __main__.cpython-311.pyc
   │        │  ├─ constant.py
   │        │  ├─ legacy.py
   │        │  ├─ md.cpython-311-darwin.so
   │        │  ├─ md.py
   │        │  ├─ md__mypyc.cpython-311-darwin.so
   │        │  ├─ models.py
   │        │  ├─ py.typed
   │        │  ├─ utils.py
   │        │  └─ version.py
   │        ├─ charset_normalizer-3.4.2.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  ├─ entry_points.txt
   │        │  ├─ licenses
   │        │  │  └─ LICENSE
   │        │  └─ top_level.txt
   │        ├─ click
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ _compat.cpython-311.pyc
   │        │  │  ├─ _termui_impl.cpython-311.pyc
   │        │  │  ├─ _textwrap.cpython-311.pyc
   │        │  │  ├─ _winconsole.cpython-311.pyc
   │        │  │  ├─ core.cpython-311.pyc
   │        │  │  ├─ decorators.cpython-311.pyc
   │        │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  ├─ formatting.cpython-311.pyc
   │        │  │  ├─ globals.cpython-311.pyc
   │        │  │  ├─ parser.cpython-311.pyc
   │        │  │  ├─ shell_completion.cpython-311.pyc
   │        │  │  ├─ termui.cpython-311.pyc
   │        │  │  ├─ testing.cpython-311.pyc
   │        │  │  ├─ types.cpython-311.pyc
   │        │  │  └─ utils.cpython-311.pyc
   │        │  ├─ _compat.py
   │        │  ├─ _termui_impl.py
   │        │  ├─ _textwrap.py
   │        │  ├─ _winconsole.py
   │        │  ├─ core.py
   │        │  ├─ decorators.py
   │        │  ├─ exceptions.py
   │        │  ├─ formatting.py
   │        │  ├─ globals.py
   │        │  ├─ parser.py
   │        │  ├─ py.typed
   │        │  ├─ shell_completion.py
   │        │  ├─ termui.py
   │        │  ├─ testing.py
   │        │  ├─ types.py
   │        │  └─ utils.py
   │        ├─ click-8.2.1.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  └─ licenses
   │        │     └─ LICENSE.txt
   │        ├─ dateutil
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ _common.cpython-311.pyc
   │        │  │  ├─ _version.cpython-311.pyc
   │        │  │  ├─ easter.cpython-311.pyc
   │        │  │  ├─ relativedelta.cpython-311.pyc
   │        │  │  ├─ rrule.cpython-311.pyc
   │        │  │  ├─ tzwin.cpython-311.pyc
   │        │  │  └─ utils.cpython-311.pyc
   │        │  ├─ _common.py
   │        │  ├─ _version.py
   │        │  ├─ easter.py
   │        │  ├─ parser
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _parser.cpython-311.pyc
   │        │  │  │  └─ isoparser.cpython-311.pyc
   │        │  │  ├─ _parser.py
   │        │  │  └─ isoparser.py
   │        │  ├─ relativedelta.py
   │        │  ├─ rrule.py
   │        │  ├─ tz
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _common.cpython-311.pyc
   │        │  │  │  ├─ _factories.cpython-311.pyc
   │        │  │  │  ├─ tz.cpython-311.pyc
   │        │  │  │  └─ win.cpython-311.pyc
   │        │  │  ├─ _common.py
   │        │  │  ├─ _factories.py
   │        │  │  ├─ tz.py
   │        │  │  └─ win.py
   │        │  ├─ tzwin.py
   │        │  ├─ utils.py
   │        │  └─ zoneinfo
   │        │     ├─ __init__.py
   │        │     ├─ __pycache__
   │        │     │  ├─ __init__.cpython-311.pyc
   │        │     │  └─ rebuild.cpython-311.pyc
   │        │     ├─ dateutil-zoneinfo.tar.gz
   │        │     └─ rebuild.py
   │        ├─ distutils-precedence.pth
   │        ├─ django
   │        │  ├─ __init__.py
   │        │  ├─ __main__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ __main__.cpython-311.pyc
   │        │  │  └─ shortcuts.cpython-311.pyc
   │        │  ├─ apps
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ config.cpython-311.pyc
   │        │  │  │  └─ registry.cpython-311.pyc
   │        │  │  ├─ config.py
   │        │  │  └─ registry.py
   │        │  ├─ conf
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  └─ global_settings.cpython-311.pyc
   │        │  │  ├─ app_template
   │        │  │  │  ├─ __init__.py-tpl
   │        │  │  │  ├─ admin.py-tpl
   │        │  │  │  ├─ apps.py-tpl
   │        │  │  │  ├─ migrations
   │        │  │  │  │  └─ __init__.py-tpl
   │        │  │  │  ├─ models.py-tpl
   │        │  │  │  ├─ tests.py-tpl
   │        │  │  │  └─ views.py-tpl
   │        │  │  ├─ global_settings.py
   │        │  │  ├─ locale
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  │  ├─ af
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ ar
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ ar_DZ
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ ast
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ az
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ be
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ bg
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ bn
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ br
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ bs
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ ca
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ ckb
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ cs
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ cy
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ da
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ de
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ de_CH
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ dsb
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ el
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ en
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ en_AU
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ en_CA
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ en_GB
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ en_IE
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ eo
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ es
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ es_AR
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ es_CO
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ es_MX
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ es_NI
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ es_PR
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ es_VE
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ et
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ eu
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ fa
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ fi
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ fr
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ fr_BE
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ fr_CA
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ fr_CH
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ fy
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ ga
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ gd
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ gl
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ he
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ hi
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ hr
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ hsb
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ hu
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ hy
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ ia
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ id
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ ig
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ io
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ is
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ it
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ ja
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ ka
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ kab
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ kk
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ km
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ kn
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ ko
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ ky
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ lb
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ lt
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ lv
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ mk
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ ml
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ mn
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ mr
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ ms
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ my
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ nb
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ ne
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ nl
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ nn
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ os
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ pa
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ pl
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ pt
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ pt_BR
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ ro
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ ru
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ sk
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ sl
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ sq
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ sr
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ sr_Latn
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ sv
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ sw
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ ta
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ te
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ tg
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ th
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ tk
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ tr
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ tt
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ udm
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ ug
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ uk
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ ur
   │        │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │     ├─ django.mo
   │        │  │  │  │     └─ django.po
   │        │  │  │  ├─ uz
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ vi
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  ├─ zh_Hans
   │        │  │  │  │  ├─ LC_MESSAGES
   │        │  │  │  │  │  ├─ django.mo
   │        │  │  │  │  │  └─ django.po
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  │  └─ formats.py
   │        │  │  │  └─ zh_Hant
   │        │  │  │     ├─ LC_MESSAGES
   │        │  │  │     │  ├─ django.mo
   │        │  │  │     │  └─ django.po
   │        │  │  │     ├─ __init__.py
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │     │  └─ formats.cpython-311.pyc
   │        │  │  │     └─ formats.py
   │        │  │  ├─ project_template
   │        │  │  │  ├─ manage.py-tpl
   │        │  │  │  └─ project_name
   │        │  │  │     ├─ __init__.py-tpl
   │        │  │  │     ├─ asgi.py-tpl
   │        │  │  │     ├─ settings.py-tpl
   │        │  │  │     ├─ urls.py-tpl
   │        │  │  │     └─ wsgi.py-tpl
   │        │  │  └─ urls
   │        │  │     ├─ __init__.py
   │        │  │     ├─ __pycache__
   │        │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │     │  ├─ i18n.cpython-311.pyc
   │        │  │     │  └─ static.cpython-311.pyc
   │        │  │     ├─ i18n.py
   │        │  │     └─ static.py
   │        │  ├─ contrib
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  ├─ admin
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ actions.cpython-311.pyc
   │        │  │  │  │  ├─ apps.cpython-311.pyc
   │        │  │  │  │  ├─ checks.cpython-311.pyc
   │        │  │  │  │  ├─ decorators.cpython-311.pyc
   │        │  │  │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  │  │  ├─ filters.cpython-311.pyc
   │        │  │  │  │  ├─ forms.cpython-311.pyc
   │        │  │  │  │  ├─ helpers.cpython-311.pyc
   │        │  │  │  │  ├─ models.cpython-311.pyc
   │        │  │  │  │  ├─ options.cpython-311.pyc
   │        │  │  │  │  ├─ sites.cpython-311.pyc
   │        │  │  │  │  ├─ tests.cpython-311.pyc
   │        │  │  │  │  ├─ utils.cpython-311.pyc
   │        │  │  │  │  └─ widgets.cpython-311.pyc
   │        │  │  │  ├─ actions.py
   │        │  │  │  ├─ apps.py
   │        │  │  │  ├─ checks.py
   │        │  │  │  ├─ decorators.py
   │        │  │  │  ├─ exceptions.py
   │        │  │  │  ├─ filters.py
   │        │  │  │  ├─ forms.py
   │        │  │  │  ├─ helpers.py
   │        │  │  │  ├─ locale
   │        │  │  │  │  ├─ af
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ am
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ ar_DZ
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ ast
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ az
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ be
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ bg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ bn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ br
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ bs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ ca
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ ckb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ cs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ cy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ da
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ de
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ dsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ el
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ en
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ en_AU
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ en_GB
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ eo
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ es
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ es_AR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ es_CO
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ es_MX
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ es_VE
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ et
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ eu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ fa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ fi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ fr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ fy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ ga
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ gd
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ gl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ he
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ hi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ hr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ hsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ hu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ hy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ ia
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ id
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ io
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ is
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ it
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ ja
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ ka
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ kab
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ kk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ km
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ kn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ ko
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ ky
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ lb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ lt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ lv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ mk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ ml
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ mn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ mr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ ms
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ my
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ nb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ ne
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ nl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ nn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ os
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ pa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ pl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ pt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ pt_BR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ ro
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ ru
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ sk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ sl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ sq
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ sr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ sr_Latn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ sv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ sw
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ ta
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ te
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ tg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ th
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ tk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ tt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ udm
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ ug
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ uk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ ur
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ uz
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ vi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  ├─ zh_Hans
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     ├─ django.po
   │        │  │  │  │  │     ├─ djangojs.mo
   │        │  │  │  │  │     └─ djangojs.po
   │        │  │  │  │  └─ zh_Hant
   │        │  │  │  │     └─ LC_MESSAGES
   │        │  │  │  │        ├─ django.mo
   │        │  │  │  │        ├─ django.po
   │        │  │  │  │        ├─ djangojs.mo
   │        │  │  │  │        └─ djangojs.po
   │        │  │  │  ├─ migrations
   │        │  │  │  │  ├─ 0001_initial.py
   │        │  │  │  │  ├─ 0002_logentry_remove_auto_add.py
   │        │  │  │  │  ├─ 0003_logentry_add_action_flag_choices.py
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  └─ __pycache__
   │        │  │  │  │     ├─ 0001_initial.cpython-311.pyc
   │        │  │  │  │     ├─ 0002_logentry_remove_auto_add.cpython-311.pyc
   │        │  │  │  │     ├─ 0003_logentry_add_action_flag_choices.cpython-311.pyc
   │        │  │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  │  ├─ models.py
   │        │  │  │  ├─ options.py
   │        │  │  │  ├─ sites.py
   │        │  │  │  ├─ static
   │        │  │  │  │  └─ admin
   │        │  │  │  │     ├─ css
   │        │  │  │  │     │  ├─ autocomplete.css
   │        │  │  │  │     │  ├─ base.css
   │        │  │  │  │     │  ├─ changelists.css
   │        │  │  │  │     │  ├─ dark_mode.css
   │        │  │  │  │     │  ├─ dashboard.css
   │        │  │  │  │     │  ├─ forms.css
   │        │  │  │  │     │  ├─ login.css
   │        │  │  │  │     │  ├─ nav_sidebar.css
   │        │  │  │  │     │  ├─ responsive.css
   │        │  │  │  │     │  ├─ responsive_rtl.css
   │        │  │  │  │     │  ├─ rtl.css
   │        │  │  │  │     │  ├─ unusable_password_field.css
   │        │  │  │  │     │  ├─ vendor
   │        │  │  │  │     │  │  └─ select2
   │        │  │  │  │     │  │     ├─ LICENSE-SELECT2.md
   │        │  │  │  │     │  │     ├─ select2.css
   │        │  │  │  │     │  │     └─ select2.min.css
   │        │  │  │  │     │  └─ widgets.css
   │        │  │  │  │     ├─ img
   │        │  │  │  │     │  ├─ LICENSE
   │        │  │  │  │     │  ├─ README.txt
   │        │  │  │  │     │  ├─ calendar-icons.svg
   │        │  │  │  │     │  ├─ gis
   │        │  │  │  │     │  │  ├─ move_vertex_off.svg
   │        │  │  │  │     │  │  └─ move_vertex_on.svg
   │        │  │  │  │     │  ├─ icon-addlink.svg
   │        │  │  │  │     │  ├─ icon-alert.svg
   │        │  │  │  │     │  ├─ icon-calendar.svg
   │        │  │  │  │     │  ├─ icon-changelink.svg
   │        │  │  │  │     │  ├─ icon-clock.svg
   │        │  │  │  │     │  ├─ icon-deletelink.svg
   │        │  │  │  │     │  ├─ icon-hidelink.svg
   │        │  │  │  │     │  ├─ icon-no.svg
   │        │  │  │  │     │  ├─ icon-unknown-alt.svg
   │        │  │  │  │     │  ├─ icon-unknown.svg
   │        │  │  │  │     │  ├─ icon-viewlink.svg
   │        │  │  │  │     │  ├─ icon-yes.svg
   │        │  │  │  │     │  ├─ inline-delete.svg
   │        │  │  │  │     │  ├─ search.svg
   │        │  │  │  │     │  ├─ selector-icons.svg
   │        │  │  │  │     │  ├─ sorting-icons.svg
   │        │  │  │  │     │  ├─ tooltag-add.svg
   │        │  │  │  │     │  └─ tooltag-arrowright.svg
   │        │  │  │  │     └─ js
   │        │  │  │  │        ├─ SelectBox.js
   │        │  │  │  │        ├─ SelectFilter2.js
   │        │  │  │  │        ├─ actions.js
   │        │  │  │  │        ├─ admin
   │        │  │  │  │        │  ├─ DateTimeShortcuts.js
   │        │  │  │  │        │  └─ RelatedObjectLookups.js
   │        │  │  │  │        ├─ autocomplete.js
   │        │  │  │  │        ├─ calendar.js
   │        │  │  │  │        ├─ cancel.js
   │        │  │  │  │        ├─ change_form.js
   │        │  │  │  │        ├─ core.js
   │        │  │  │  │        ├─ filters.js
   │        │  │  │  │        ├─ inlines.js
   │        │  │  │  │        ├─ jquery.init.js
   │        │  │  │  │        ├─ nav_sidebar.js
   │        │  │  │  │        ├─ popup_response.js
   │        │  │  │  │        ├─ prepopulate.js
   │        │  │  │  │        ├─ prepopulate_init.js
   │        │  │  │  │        ├─ theme.js
   │        │  │  │  │        ├─ unusable_password_field.js
   │        │  │  │  │        ├─ urlify.js
   │        │  │  │  │        └─ vendor
   │        │  │  │  │           ├─ jquery
   │        │  │  │  │           │  ├─ LICENSE.txt
   │        │  │  │  │           │  ├─ jquery.js
   │        │  │  │  │           │  └─ jquery.min.js
   │        │  │  │  │           ├─ select2
   │        │  │  │  │           │  ├─ LICENSE.md
   │        │  │  │  │           │  ├─ i18n
   │        │  │  │  │           │  │  ├─ af.js
   │        │  │  │  │           │  │  ├─ ar.js
   │        │  │  │  │           │  │  ├─ az.js
   │        │  │  │  │           │  │  ├─ bg.js
   │        │  │  │  │           │  │  ├─ bn.js
   │        │  │  │  │           │  │  ├─ bs.js
   │        │  │  │  │           │  │  ├─ ca.js
   │        │  │  │  │           │  │  ├─ cs.js
   │        │  │  │  │           │  │  ├─ da.js
   │        │  │  │  │           │  │  ├─ de.js
   │        │  │  │  │           │  │  ├─ dsb.js
   │        │  │  │  │           │  │  ├─ el.js
   │        │  │  │  │           │  │  ├─ en.js
   │        │  │  │  │           │  │  ├─ es.js
   │        │  │  │  │           │  │  ├─ et.js
   │        │  │  │  │           │  │  ├─ eu.js
   │        │  │  │  │           │  │  ├─ fa.js
   │        │  │  │  │           │  │  ├─ fi.js
   │        │  │  │  │           │  │  ├─ fr.js
   │        │  │  │  │           │  │  ├─ gl.js
   │        │  │  │  │           │  │  ├─ he.js
   │        │  │  │  │           │  │  ├─ hi.js
   │        │  │  │  │           │  │  ├─ hr.js
   │        │  │  │  │           │  │  ├─ hsb.js
   │        │  │  │  │           │  │  ├─ hu.js
   │        │  │  │  │           │  │  ├─ hy.js
   │        │  │  │  │           │  │  ├─ id.js
   │        │  │  │  │           │  │  ├─ is.js
   │        │  │  │  │           │  │  ├─ it.js
   │        │  │  │  │           │  │  ├─ ja.js
   │        │  │  │  │           │  │  ├─ ka.js
   │        │  │  │  │           │  │  ├─ km.js
   │        │  │  │  │           │  │  ├─ ko.js
   │        │  │  │  │           │  │  ├─ lt.js
   │        │  │  │  │           │  │  ├─ lv.js
   │        │  │  │  │           │  │  ├─ mk.js
   │        │  │  │  │           │  │  ├─ ms.js
   │        │  │  │  │           │  │  ├─ nb.js
   │        │  │  │  │           │  │  ├─ ne.js
   │        │  │  │  │           │  │  ├─ nl.js
   │        │  │  │  │           │  │  ├─ pl.js
   │        │  │  │  │           │  │  ├─ ps.js
   │        │  │  │  │           │  │  ├─ pt-BR.js
   │        │  │  │  │           │  │  ├─ pt.js
   │        │  │  │  │           │  │  ├─ ro.js
   │        │  │  │  │           │  │  ├─ ru.js
   │        │  │  │  │           │  │  ├─ sk.js
   │        │  │  │  │           │  │  ├─ sl.js
   │        │  │  │  │           │  │  ├─ sq.js
   │        │  │  │  │           │  │  ├─ sr-Cyrl.js
   │        │  │  │  │           │  │  ├─ sr.js
   │        │  │  │  │           │  │  ├─ sv.js
   │        │  │  │  │           │  │  ├─ th.js
   │        │  │  │  │           │  │  ├─ tk.js
   │        │  │  │  │           │  │  ├─ tr.js
   │        │  │  │  │           │  │  ├─ uk.js
   │        │  │  │  │           │  │  ├─ vi.js
   │        │  │  │  │           │  │  ├─ zh-CN.js
   │        │  │  │  │           │  │  └─ zh-TW.js
   │        │  │  │  │           │  ├─ select2.full.js
   │        │  │  │  │           │  └─ select2.full.min.js
   │        │  │  │  │           └─ xregexp
   │        │  │  │  │              ├─ LICENSE.txt
   │        │  │  │  │              ├─ xregexp.js
   │        │  │  │  │              └─ xregexp.min.js
   │        │  │  │  ├─ templates
   │        │  │  │  │  ├─ admin
   │        │  │  │  │  │  ├─ 404.html
   │        │  │  │  │  │  ├─ 500.html
   │        │  │  │  │  │  ├─ actions.html
   │        │  │  │  │  │  ├─ app_index.html
   │        │  │  │  │  │  ├─ app_list.html
   │        │  │  │  │  │  ├─ auth
   │        │  │  │  │  │  │  └─ user
   │        │  │  │  │  │  │     ├─ add_form.html
   │        │  │  │  │  │  │     └─ change_password.html
   │        │  │  │  │  │  ├─ base.html
   │        │  │  │  │  │  ├─ base_site.html
   │        │  │  │  │  │  ├─ change_form.html
   │        │  │  │  │  │  ├─ change_form_object_tools.html
   │        │  │  │  │  │  ├─ change_list.html
   │        │  │  │  │  │  ├─ change_list_object_tools.html
   │        │  │  │  │  │  ├─ change_list_results.html
   │        │  │  │  │  │  ├─ color_theme_toggle.html
   │        │  │  │  │  │  ├─ date_hierarchy.html
   │        │  │  │  │  │  ├─ delete_confirmation.html
   │        │  │  │  │  │  ├─ delete_selected_confirmation.html
   │        │  │  │  │  │  ├─ edit_inline
   │        │  │  │  │  │  │  ├─ stacked.html
   │        │  │  │  │  │  │  └─ tabular.html
   │        │  │  │  │  │  ├─ filter.html
   │        │  │  │  │  │  ├─ includes
   │        │  │  │  │  │  │  ├─ fieldset.html
   │        │  │  │  │  │  │  └─ object_delete_summary.html
   │        │  │  │  │  │  ├─ index.html
   │        │  │  │  │  │  ├─ invalid_setup.html
   │        │  │  │  │  │  ├─ login.html
   │        │  │  │  │  │  ├─ nav_sidebar.html
   │        │  │  │  │  │  ├─ object_history.html
   │        │  │  │  │  │  ├─ pagination.html
   │        │  │  │  │  │  ├─ popup_response.html
   │        │  │  │  │  │  ├─ prepopulated_fields_js.html
   │        │  │  │  │  │  ├─ search_form.html
   │        │  │  │  │  │  ├─ submit_line.html
   │        │  │  │  │  │  └─ widgets
   │        │  │  │  │  │     ├─ clearable_file_input.html
   │        │  │  │  │  │     ├─ date.html
   │        │  │  │  │  │     ├─ foreign_key_raw_id.html
   │        │  │  │  │  │     ├─ many_to_many_raw_id.html
   │        │  │  │  │  │     ├─ radio.html
   │        │  │  │  │  │     ├─ related_widget_wrapper.html
   │        │  │  │  │  │     ├─ split_datetime.html
   │        │  │  │  │  │     ├─ time.html
   │        │  │  │  │  │     └─ url.html
   │        │  │  │  │  └─ registration
   │        │  │  │  │     ├─ logged_out.html
   │        │  │  │  │     ├─ password_change_done.html
   │        │  │  │  │     ├─ password_change_form.html
   │        │  │  │  │     ├─ password_reset_complete.html
   │        │  │  │  │     ├─ password_reset_confirm.html
   │        │  │  │  │     ├─ password_reset_done.html
   │        │  │  │  │     ├─ password_reset_email.html
   │        │  │  │  │     └─ password_reset_form.html
   │        │  │  │  ├─ templatetags
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ admin_list.cpython-311.pyc
   │        │  │  │  │  │  ├─ admin_modify.cpython-311.pyc
   │        │  │  │  │  │  ├─ admin_urls.cpython-311.pyc
   │        │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  └─ log.cpython-311.pyc
   │        │  │  │  │  ├─ admin_list.py
   │        │  │  │  │  ├─ admin_modify.py
   │        │  │  │  │  ├─ admin_urls.py
   │        │  │  │  │  ├─ base.py
   │        │  │  │  │  └─ log.py
   │        │  │  │  ├─ tests.py
   │        │  │  │  ├─ utils.py
   │        │  │  │  ├─ views
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ autocomplete.cpython-311.pyc
   │        │  │  │  │  │  ├─ decorators.cpython-311.pyc
   │        │  │  │  │  │  └─ main.cpython-311.pyc
   │        │  │  │  │  ├─ autocomplete.py
   │        │  │  │  │  ├─ decorators.py
   │        │  │  │  │  └─ main.py
   │        │  │  │  └─ widgets.py
   │        │  │  ├─ admindocs
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ apps.cpython-311.pyc
   │        │  │  │  │  ├─ middleware.cpython-311.pyc
   │        │  │  │  │  ├─ urls.cpython-311.pyc
   │        │  │  │  │  ├─ utils.cpython-311.pyc
   │        │  │  │  │  └─ views.cpython-311.pyc
   │        │  │  │  ├─ apps.py
   │        │  │  │  ├─ locale
   │        │  │  │  │  ├─ af
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar_DZ
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ast
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ az
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ be
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ br
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ca
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ckb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ cs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ cy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ da
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ de
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ dsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ el
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en_AU
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en_GB
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ eo
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_AR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_CO
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_MX
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_VE
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ et
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ eu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ga
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ gd
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ gl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ he
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ia
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ id
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ io
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ is
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ it
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ja
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ka
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kab
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ km
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ko
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ky
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ml
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ms
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ my
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ne
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ os
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pt_BR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ro
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ru
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sq
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sr_Latn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sw
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ta
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ te
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ th
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ udm
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ug
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ uk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ur
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ vi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ zh_Hans
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  └─ zh_Hant
   │        │  │  │  │     └─ LC_MESSAGES
   │        │  │  │  │        ├─ django.mo
   │        │  │  │  │        └─ django.po
   │        │  │  │  ├─ middleware.py
   │        │  │  │  ├─ templates
   │        │  │  │  │  └─ admin_doc
   │        │  │  │  │     ├─ bookmarklets.html
   │        │  │  │  │     ├─ index.html
   │        │  │  │  │     ├─ missing_docutils.html
   │        │  │  │  │     ├─ model_detail.html
   │        │  │  │  │     ├─ model_index.html
   │        │  │  │  │     ├─ template_detail.html
   │        │  │  │  │     ├─ template_filter_index.html
   │        │  │  │  │     ├─ template_tag_index.html
   │        │  │  │  │     ├─ view_detail.html
   │        │  │  │  │     └─ view_index.html
   │        │  │  │  ├─ urls.py
   │        │  │  │  ├─ utils.py
   │        │  │  │  └─ views.py
   │        │  │  ├─ auth
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ admin.cpython-311.pyc
   │        │  │  │  │  ├─ apps.cpython-311.pyc
   │        │  │  │  │  ├─ backends.cpython-311.pyc
   │        │  │  │  │  ├─ base_user.cpython-311.pyc
   │        │  │  │  │  ├─ checks.cpython-311.pyc
   │        │  │  │  │  ├─ context_processors.cpython-311.pyc
   │        │  │  │  │  ├─ decorators.cpython-311.pyc
   │        │  │  │  │  ├─ forms.cpython-311.pyc
   │        │  │  │  │  ├─ hashers.cpython-311.pyc
   │        │  │  │  │  ├─ middleware.cpython-311.pyc
   │        │  │  │  │  ├─ mixins.cpython-311.pyc
   │        │  │  │  │  ├─ models.cpython-311.pyc
   │        │  │  │  │  ├─ password_validation.cpython-311.pyc
   │        │  │  │  │  ├─ signals.cpython-311.pyc
   │        │  │  │  │  ├─ tokens.cpython-311.pyc
   │        │  │  │  │  ├─ urls.cpython-311.pyc
   │        │  │  │  │  ├─ validators.cpython-311.pyc
   │        │  │  │  │  └─ views.cpython-311.pyc
   │        │  │  │  ├─ admin.py
   │        │  │  │  ├─ apps.py
   │        │  │  │  ├─ backends.py
   │        │  │  │  ├─ base_user.py
   │        │  │  │  ├─ checks.py
   │        │  │  │  ├─ common-passwords.txt.gz
   │        │  │  │  ├─ context_processors.py
   │        │  │  │  ├─ decorators.py
   │        │  │  │  ├─ forms.py
   │        │  │  │  ├─ handlers
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ modwsgi.cpython-311.pyc
   │        │  │  │  │  └─ modwsgi.py
   │        │  │  │  ├─ hashers.py
   │        │  │  │  ├─ locale
   │        │  │  │  │  ├─ af
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar_DZ
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ast
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ az
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ be
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ br
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ca
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ckb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ cs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ cy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ da
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ de
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ dsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ el
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en_AU
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en_GB
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ eo
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_AR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_CO
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_MX
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_VE
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ et
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ eu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ga
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ gd
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ gl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ he
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ia
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ id
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ io
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ is
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ it
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ja
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ka
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kab
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ km
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ko
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ky
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ml
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ms
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ my
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ne
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ os
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pt_BR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ro
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ru
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sq
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sr_Latn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sw
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ta
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ te
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ th
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ udm
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ug
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ uk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ur
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ uz
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ vi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ zh_Hans
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  └─ zh_Hant
   │        │  │  │  │     └─ LC_MESSAGES
   │        │  │  │  │        ├─ django.mo
   │        │  │  │  │        └─ django.po
   │        │  │  │  ├─ management
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  │  │  └─ commands
   │        │  │  │  │     ├─ __init__.py
   │        │  │  │  │     ├─ __pycache__
   │        │  │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │     │  ├─ changepassword.cpython-311.pyc
   │        │  │  │  │     │  └─ createsuperuser.cpython-311.pyc
   │        │  │  │  │     ├─ changepassword.py
   │        │  │  │  │     └─ createsuperuser.py
   │        │  │  │  ├─ middleware.py
   │        │  │  │  ├─ migrations
   │        │  │  │  │  ├─ 0001_initial.py
   │        │  │  │  │  ├─ 0002_alter_permission_name_max_length.py
   │        │  │  │  │  ├─ 0003_alter_user_email_max_length.py
   │        │  │  │  │  ├─ 0004_alter_user_username_opts.py
   │        │  │  │  │  ├─ 0005_alter_user_last_login_null.py
   │        │  │  │  │  ├─ 0006_require_contenttypes_0002.py
   │        │  │  │  │  ├─ 0007_alter_validators_add_error_messages.py
   │        │  │  │  │  ├─ 0008_alter_user_username_max_length.py
   │        │  │  │  │  ├─ 0009_alter_user_last_name_max_length.py
   │        │  │  │  │  ├─ 0010_alter_group_name_max_length.py
   │        │  │  │  │  ├─ 0011_update_proxy_permissions.py
   │        │  │  │  │  ├─ 0012_alter_user_first_name_max_length.py
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  └─ __pycache__
   │        │  │  │  │     ├─ 0001_initial.cpython-311.pyc
   │        │  │  │  │     ├─ 0002_alter_permission_name_max_length.cpython-311.pyc
   │        │  │  │  │     ├─ 0003_alter_user_email_max_length.cpython-311.pyc
   │        │  │  │  │     ├─ 0004_alter_user_username_opts.cpython-311.pyc
   │        │  │  │  │     ├─ 0005_alter_user_last_login_null.cpython-311.pyc
   │        │  │  │  │     ├─ 0006_require_contenttypes_0002.cpython-311.pyc
   │        │  │  │  │     ├─ 0007_alter_validators_add_error_messages.cpython-311.pyc
   │        │  │  │  │     ├─ 0008_alter_user_username_max_length.cpython-311.pyc
   │        │  │  │  │     ├─ 0009_alter_user_last_name_max_length.cpython-311.pyc
   │        │  │  │  │     ├─ 0010_alter_group_name_max_length.cpython-311.pyc
   │        │  │  │  │     ├─ 0011_update_proxy_permissions.cpython-311.pyc
   │        │  │  │  │     ├─ 0012_alter_user_first_name_max_length.cpython-311.pyc
   │        │  │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  │  ├─ mixins.py
   │        │  │  │  ├─ models.py
   │        │  │  │  ├─ password_validation.py
   │        │  │  │  ├─ signals.py
   │        │  │  │  ├─ templates
   │        │  │  │  │  ├─ auth
   │        │  │  │  │  │  └─ widgets
   │        │  │  │  │  │     └─ read_only_password_hash.html
   │        │  │  │  │  └─ registration
   │        │  │  │  │     └─ password_reset_subject.txt
   │        │  │  │  ├─ tokens.py
   │        │  │  │  ├─ urls.py
   │        │  │  │  ├─ validators.py
   │        │  │  │  └─ views.py
   │        │  │  ├─ contenttypes
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ admin.cpython-311.pyc
   │        │  │  │  │  ├─ apps.cpython-311.pyc
   │        │  │  │  │  ├─ checks.cpython-311.pyc
   │        │  │  │  │  ├─ fields.cpython-311.pyc
   │        │  │  │  │  ├─ forms.cpython-311.pyc
   │        │  │  │  │  ├─ models.cpython-311.pyc
   │        │  │  │  │  ├─ prefetch.cpython-311.pyc
   │        │  │  │  │  └─ views.cpython-311.pyc
   │        │  │  │  ├─ admin.py
   │        │  │  │  ├─ apps.py
   │        │  │  │  ├─ checks.py
   │        │  │  │  ├─ fields.py
   │        │  │  │  ├─ forms.py
   │        │  │  │  ├─ locale
   │        │  │  │  │  ├─ af
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar_DZ
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ast
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ az
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ be
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ br
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ca
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ckb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ cs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ cy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ da
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ de
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ dsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ el
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en_AU
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en_GB
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ eo
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_AR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_CO
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_MX
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_VE
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ et
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ eu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ga
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ gd
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ gl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ he
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ia
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ id
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ io
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ is
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ it
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ja
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ka
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ km
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ko
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ky
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ml
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ms
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ my
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ne
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ os
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pt_BR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ro
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ru
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sq
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sr_Latn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sw
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ta
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ te
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ th
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ udm
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ug
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ uk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ur
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ vi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ zh_Hans
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  └─ zh_Hant
   │        │  │  │  │     └─ LC_MESSAGES
   │        │  │  │  │        ├─ django.mo
   │        │  │  │  │        └─ django.po
   │        │  │  │  ├─ management
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  │  │  └─ commands
   │        │  │  │  │     ├─ __init__.py
   │        │  │  │  │     ├─ __pycache__
   │        │  │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │     │  └─ remove_stale_contenttypes.cpython-311.pyc
   │        │  │  │  │     └─ remove_stale_contenttypes.py
   │        │  │  │  ├─ migrations
   │        │  │  │  │  ├─ 0001_initial.py
   │        │  │  │  │  ├─ 0002_remove_content_type_name.py
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  └─ __pycache__
   │        │  │  │  │     ├─ 0001_initial.cpython-311.pyc
   │        │  │  │  │     ├─ 0002_remove_content_type_name.cpython-311.pyc
   │        │  │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  │  ├─ models.py
   │        │  │  │  ├─ prefetch.py
   │        │  │  │  └─ views.py
   │        │  │  ├─ flatpages
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ admin.cpython-311.pyc
   │        │  │  │  │  ├─ apps.cpython-311.pyc
   │        │  │  │  │  ├─ forms.cpython-311.pyc
   │        │  │  │  │  ├─ middleware.cpython-311.pyc
   │        │  │  │  │  ├─ models.cpython-311.pyc
   │        │  │  │  │  ├─ sitemaps.cpython-311.pyc
   │        │  │  │  │  ├─ urls.cpython-311.pyc
   │        │  │  │  │  └─ views.cpython-311.pyc
   │        │  │  │  ├─ admin.py
   │        │  │  │  ├─ apps.py
   │        │  │  │  ├─ forms.py
   │        │  │  │  ├─ locale
   │        │  │  │  │  ├─ af
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar_DZ
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ast
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ az
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ be
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ br
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ca
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ckb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ cs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ cy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ da
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ de
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ dsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ el
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en_AU
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en_GB
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ eo
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_AR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_CO
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_MX
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_VE
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ et
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ eu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ga
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ gd
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ gl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ he
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ia
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ id
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ io
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ is
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ it
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ja
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ka
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ km
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ko
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ky
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ml
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ms
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ my
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ne
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ os
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pt_BR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ro
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ru
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sq
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sr_Latn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sw
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ta
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ te
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ th
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ udm
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ug
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ uk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ur
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ vi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ zh_Hans
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  └─ zh_Hant
   │        │  │  │  │     └─ LC_MESSAGES
   │        │  │  │  │        ├─ django.mo
   │        │  │  │  │        └─ django.po
   │        │  │  │  ├─ middleware.py
   │        │  │  │  ├─ migrations
   │        │  │  │  │  ├─ 0001_initial.py
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  └─ __pycache__
   │        │  │  │  │     ├─ 0001_initial.cpython-311.pyc
   │        │  │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  │  ├─ models.py
   │        │  │  │  ├─ sitemaps.py
   │        │  │  │  ├─ templatetags
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ flatpages.cpython-311.pyc
   │        │  │  │  │  └─ flatpages.py
   │        │  │  │  ├─ urls.py
   │        │  │  │  └─ views.py
   │        │  │  ├─ gis
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ apps.cpython-311.pyc
   │        │  │  │  │  ├─ feeds.cpython-311.pyc
   │        │  │  │  │  ├─ geoip2.cpython-311.pyc
   │        │  │  │  │  ├─ geometry.cpython-311.pyc
   │        │  │  │  │  ├─ measure.cpython-311.pyc
   │        │  │  │  │  ├─ ptr.cpython-311.pyc
   │        │  │  │  │  ├─ shortcuts.cpython-311.pyc
   │        │  │  │  │  └─ views.cpython-311.pyc
   │        │  │  │  ├─ admin
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ options.cpython-311.pyc
   │        │  │  │  │  └─ options.py
   │        │  │  │  ├─ apps.py
   │        │  │  │  ├─ db
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ backends
   │        │  │  │  │  │  ├─ __init__.py
   │        │  │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  │  └─ utils.cpython-311.pyc
   │        │  │  │  │  │  ├─ base
   │        │  │  │  │  │  │  ├─ __init__.py
   │        │  │  │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ adapter.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ features.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ models.cpython-311.pyc
   │        │  │  │  │  │  │  │  └─ operations.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ adapter.py
   │        │  │  │  │  │  │  ├─ features.py
   │        │  │  │  │  │  │  ├─ models.py
   │        │  │  │  │  │  │  └─ operations.py
   │        │  │  │  │  │  ├─ mysql
   │        │  │  │  │  │  │  ├─ __init__.py
   │        │  │  │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ features.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ introspection.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ operations.cpython-311.pyc
   │        │  │  │  │  │  │  │  └─ schema.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ base.py
   │        │  │  │  │  │  │  ├─ features.py
   │        │  │  │  │  │  │  ├─ introspection.py
   │        │  │  │  │  │  │  ├─ operations.py
   │        │  │  │  │  │  │  └─ schema.py
   │        │  │  │  │  │  ├─ oracle
   │        │  │  │  │  │  │  ├─ __init__.py
   │        │  │  │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ adapter.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ features.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ introspection.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ models.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ operations.cpython-311.pyc
   │        │  │  │  │  │  │  │  └─ schema.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ adapter.py
   │        │  │  │  │  │  │  ├─ base.py
   │        │  │  │  │  │  │  ├─ features.py
   │        │  │  │  │  │  │  ├─ introspection.py
   │        │  │  │  │  │  │  ├─ models.py
   │        │  │  │  │  │  │  ├─ operations.py
   │        │  │  │  │  │  │  └─ schema.py
   │        │  │  │  │  │  ├─ postgis
   │        │  │  │  │  │  │  ├─ __init__.py
   │        │  │  │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ adapter.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ const.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ features.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ introspection.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ models.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ operations.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ pgraster.cpython-311.pyc
   │        │  │  │  │  │  │  │  └─ schema.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ adapter.py
   │        │  │  │  │  │  │  ├─ base.py
   │        │  │  │  │  │  │  ├─ const.py
   │        │  │  │  │  │  │  ├─ features.py
   │        │  │  │  │  │  │  ├─ introspection.py
   │        │  │  │  │  │  │  ├─ models.py
   │        │  │  │  │  │  │  ├─ operations.py
   │        │  │  │  │  │  │  ├─ pgraster.py
   │        │  │  │  │  │  │  └─ schema.py
   │        │  │  │  │  │  ├─ spatialite
   │        │  │  │  │  │  │  ├─ __init__.py
   │        │  │  │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ adapter.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ client.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ features.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ introspection.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ models.cpython-311.pyc
   │        │  │  │  │  │  │  │  ├─ operations.cpython-311.pyc
   │        │  │  │  │  │  │  │  └─ schema.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ adapter.py
   │        │  │  │  │  │  │  ├─ base.py
   │        │  │  │  │  │  │  ├─ client.py
   │        │  │  │  │  │  │  ├─ features.py
   │        │  │  │  │  │  │  ├─ introspection.py
   │        │  │  │  │  │  │  ├─ models.py
   │        │  │  │  │  │  │  ├─ operations.py
   │        │  │  │  │  │  │  └─ schema.py
   │        │  │  │  │  │  └─ utils.py
   │        │  │  │  │  └─ models
   │        │  │  │  │     ├─ __init__.py
   │        │  │  │  │     ├─ __pycache__
   │        │  │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │     │  ├─ aggregates.cpython-311.pyc
   │        │  │  │  │     │  ├─ fields.cpython-311.pyc
   │        │  │  │  │     │  ├─ functions.cpython-311.pyc
   │        │  │  │  │     │  ├─ lookups.cpython-311.pyc
   │        │  │  │  │     │  └─ proxy.cpython-311.pyc
   │        │  │  │  │     ├─ aggregates.py
   │        │  │  │  │     ├─ fields.py
   │        │  │  │  │     ├─ functions.py
   │        │  │  │  │     ├─ lookups.py
   │        │  │  │  │     ├─ proxy.py
   │        │  │  │  │     └─ sql
   │        │  │  │  │        ├─ __init__.py
   │        │  │  │  │        ├─ __pycache__
   │        │  │  │  │        │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │        │  └─ conversion.cpython-311.pyc
   │        │  │  │  │        └─ conversion.py
   │        │  │  │  ├─ feeds.py
   │        │  │  │  ├─ forms
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ fields.cpython-311.pyc
   │        │  │  │  │  │  └─ widgets.cpython-311.pyc
   │        │  │  │  │  ├─ fields.py
   │        │  │  │  │  └─ widgets.py
   │        │  │  │  ├─ gdal
   │        │  │  │  │  ├─ LICENSE
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  ├─ datasource.cpython-311.pyc
   │        │  │  │  │  │  ├─ driver.cpython-311.pyc
   │        │  │  │  │  │  ├─ envelope.cpython-311.pyc
   │        │  │  │  │  │  ├─ error.cpython-311.pyc
   │        │  │  │  │  │  ├─ feature.cpython-311.pyc
   │        │  │  │  │  │  ├─ field.cpython-311.pyc
   │        │  │  │  │  │  ├─ geometries.cpython-311.pyc
   │        │  │  │  │  │  ├─ geomtype.cpython-311.pyc
   │        │  │  │  │  │  ├─ layer.cpython-311.pyc
   │        │  │  │  │  │  ├─ libgdal.cpython-311.pyc
   │        │  │  │  │  │  └─ srs.cpython-311.pyc
   │        │  │  │  │  ├─ base.py
   │        │  │  │  │  ├─ datasource.py
   │        │  │  │  │  ├─ driver.py
   │        │  │  │  │  ├─ envelope.py
   │        │  │  │  │  ├─ error.py
   │        │  │  │  │  ├─ feature.py
   │        │  │  │  │  ├─ field.py
   │        │  │  │  │  ├─ geometries.py
   │        │  │  │  │  ├─ geomtype.py
   │        │  │  │  │  ├─ layer.py
   │        │  │  │  │  ├─ libgdal.py
   │        │  │  │  │  ├─ prototypes
   │        │  │  │  │  │  ├─ __init__.py
   │        │  │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ ds.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ errcheck.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ generation.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ geom.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ raster.cpython-311.pyc
   │        │  │  │  │  │  │  └─ srs.cpython-311.pyc
   │        │  │  │  │  │  ├─ ds.py
   │        │  │  │  │  │  ├─ errcheck.py
   │        │  │  │  │  │  ├─ generation.py
   │        │  │  │  │  │  ├─ geom.py
   │        │  │  │  │  │  ├─ raster.py
   │        │  │  │  │  │  └─ srs.py
   │        │  │  │  │  ├─ raster
   │        │  │  │  │  │  ├─ __init__.py
   │        │  │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ band.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ const.cpython-311.pyc
   │        │  │  │  │  │  │  └─ source.cpython-311.pyc
   │        │  │  │  │  │  ├─ band.py
   │        │  │  │  │  │  ├─ base.py
   │        │  │  │  │  │  ├─ const.py
   │        │  │  │  │  │  └─ source.py
   │        │  │  │  │  └─ srs.py
   │        │  │  │  ├─ geoip2.py
   │        │  │  │  ├─ geometry.py
   │        │  │  │  ├─ geos
   │        │  │  │  │  ├─ LICENSE
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  ├─ collections.cpython-311.pyc
   │        │  │  │  │  │  ├─ coordseq.cpython-311.pyc
   │        │  │  │  │  │  ├─ error.cpython-311.pyc
   │        │  │  │  │  │  ├─ factory.cpython-311.pyc
   │        │  │  │  │  │  ├─ geometry.cpython-311.pyc
   │        │  │  │  │  │  ├─ io.cpython-311.pyc
   │        │  │  │  │  │  ├─ libgeos.cpython-311.pyc
   │        │  │  │  │  │  ├─ linestring.cpython-311.pyc
   │        │  │  │  │  │  ├─ mutable_list.cpython-311.pyc
   │        │  │  │  │  │  ├─ point.cpython-311.pyc
   │        │  │  │  │  │  ├─ polygon.cpython-311.pyc
   │        │  │  │  │  │  └─ prepared.cpython-311.pyc
   │        │  │  │  │  ├─ base.py
   │        │  │  │  │  ├─ collections.py
   │        │  │  │  │  ├─ coordseq.py
   │        │  │  │  │  ├─ error.py
   │        │  │  │  │  ├─ factory.py
   │        │  │  │  │  ├─ geometry.py
   │        │  │  │  │  ├─ io.py
   │        │  │  │  │  ├─ libgeos.py
   │        │  │  │  │  ├─ linestring.py
   │        │  │  │  │  ├─ mutable_list.py
   │        │  │  │  │  ├─ point.py
   │        │  │  │  │  ├─ polygon.py
   │        │  │  │  │  ├─ prepared.py
   │        │  │  │  │  └─ prototypes
   │        │  │  │  │     ├─ __init__.py
   │        │  │  │  │     ├─ __pycache__
   │        │  │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │     │  ├─ coordseq.cpython-311.pyc
   │        │  │  │  │     │  ├─ errcheck.cpython-311.pyc
   │        │  │  │  │     │  ├─ geom.cpython-311.pyc
   │        │  │  │  │     │  ├─ io.cpython-311.pyc
   │        │  │  │  │     │  ├─ misc.cpython-311.pyc
   │        │  │  │  │     │  ├─ predicates.cpython-311.pyc
   │        │  │  │  │     │  ├─ prepared.cpython-311.pyc
   │        │  │  │  │     │  ├─ threadsafe.cpython-311.pyc
   │        │  │  │  │     │  └─ topology.cpython-311.pyc
   │        │  │  │  │     ├─ coordseq.py
   │        │  │  │  │     ├─ errcheck.py
   │        │  │  │  │     ├─ geom.py
   │        │  │  │  │     ├─ io.py
   │        │  │  │  │     ├─ misc.py
   │        │  │  │  │     ├─ predicates.py
   │        │  │  │  │     ├─ prepared.py
   │        │  │  │  │     ├─ threadsafe.py
   │        │  │  │  │     └─ topology.py
   │        │  │  │  ├─ locale
   │        │  │  │  │  ├─ af
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar_DZ
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ast
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ az
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ be
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ br
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ca
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ckb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ cs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ cy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ da
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ de
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ dsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ el
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en_AU
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en_GB
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ eo
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_AR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_CO
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_MX
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_VE
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ et
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ eu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ga
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ gd
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ gl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ he
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ia
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ id
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ io
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ is
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ it
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ja
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ka
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ km
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ko
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ky
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ml
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ms
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ my
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ne
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ os
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pt_BR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ro
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ru
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sq
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sr_Latn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sw
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ta
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ te
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ th
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ udm
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ug
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ uk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ur
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ vi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ zh_Hans
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  └─ zh_Hant
   │        │  │  │  │     └─ LC_MESSAGES
   │        │  │  │  │        ├─ django.mo
   │        │  │  │  │        └─ django.po
   │        │  │  │  ├─ management
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  │  │  └─ commands
   │        │  │  │  │     ├─ __init__.py
   │        │  │  │  │     ├─ __pycache__
   │        │  │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │     │  ├─ inspectdb.cpython-311.pyc
   │        │  │  │  │     │  └─ ogrinspect.cpython-311.pyc
   │        │  │  │  │     ├─ inspectdb.py
   │        │  │  │  │     └─ ogrinspect.py
   │        │  │  │  ├─ measure.py
   │        │  │  │  ├─ ptr.py
   │        │  │  │  ├─ serializers
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ geojson.cpython-311.pyc
   │        │  │  │  │  └─ geojson.py
   │        │  │  │  ├─ shortcuts.py
   │        │  │  │  ├─ sitemaps
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ kml.cpython-311.pyc
   │        │  │  │  │  │  └─ views.cpython-311.pyc
   │        │  │  │  │  ├─ kml.py
   │        │  │  │  │  └─ views.py
   │        │  │  │  ├─ static
   │        │  │  │  │  └─ gis
   │        │  │  │  │     ├─ css
   │        │  │  │  │     │  └─ ol3.css
   │        │  │  │  │     ├─ img
   │        │  │  │  │     │  ├─ draw_line_off.svg
   │        │  │  │  │     │  ├─ draw_line_on.svg
   │        │  │  │  │     │  ├─ draw_point_off.svg
   │        │  │  │  │     │  ├─ draw_point_on.svg
   │        │  │  │  │     │  ├─ draw_polygon_off.svg
   │        │  │  │  │     │  └─ draw_polygon_on.svg
   │        │  │  │  │     └─ js
   │        │  │  │  │        └─ OLMapWidget.js
   │        │  │  │  ├─ templates
   │        │  │  │  │  └─ gis
   │        │  │  │  │     ├─ kml
   │        │  │  │  │     │  ├─ base.kml
   │        │  │  │  │     │  └─ placemarks.kml
   │        │  │  │  │     ├─ openlayers-osm.html
   │        │  │  │  │     └─ openlayers.html
   │        │  │  │  ├─ utils
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ layermapping.cpython-311.pyc
   │        │  │  │  │  │  ├─ ogrinfo.cpython-311.pyc
   │        │  │  │  │  │  ├─ ogrinspect.cpython-311.pyc
   │        │  │  │  │  │  └─ srs.cpython-311.pyc
   │        │  │  │  │  ├─ layermapping.py
   │        │  │  │  │  ├─ ogrinfo.py
   │        │  │  │  │  ├─ ogrinspect.py
   │        │  │  │  │  └─ srs.py
   │        │  │  │  └─ views.py
   │        │  │  ├─ humanize
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  └─ apps.cpython-311.pyc
   │        │  │  │  ├─ apps.py
   │        │  │  │  ├─ locale
   │        │  │  │  │  ├─ af
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar_DZ
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ast
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ az
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ be
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ br
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ca
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ckb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ cs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ cy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ da
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ de
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ dsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ el
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en_AU
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en_GB
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ eo
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_AR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_CO
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_MX
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_VE
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ et
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ eu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ga
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ gd
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ gl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ he
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ia
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ id
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ io
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ is
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ it
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ja
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ka
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ km
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ko
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ky
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ml
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ms
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ my
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ne
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ os
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pt_BR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ro
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ru
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sq
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sr_Latn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sw
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ta
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ te
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ th
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ udm
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ug
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ uk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ur
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ uz
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ vi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ zh_Hans
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  └─ zh_Hant
   │        │  │  │  │     └─ LC_MESSAGES
   │        │  │  │  │        ├─ django.mo
   │        │  │  │  │        └─ django.po
   │        │  │  │  └─ templatetags
   │        │  │  │     ├─ __init__.py
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │     │  └─ humanize.cpython-311.pyc
   │        │  │  │     └─ humanize.py
   │        │  │  ├─ messages
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ api.cpython-311.pyc
   │        │  │  │  │  ├─ apps.cpython-311.pyc
   │        │  │  │  │  ├─ constants.cpython-311.pyc
   │        │  │  │  │  ├─ context_processors.cpython-311.pyc
   │        │  │  │  │  ├─ middleware.cpython-311.pyc
   │        │  │  │  │  ├─ test.cpython-311.pyc
   │        │  │  │  │  ├─ utils.cpython-311.pyc
   │        │  │  │  │  └─ views.cpython-311.pyc
   │        │  │  │  ├─ api.py
   │        │  │  │  ├─ apps.py
   │        │  │  │  ├─ constants.py
   │        │  │  │  ├─ context_processors.py
   │        │  │  │  ├─ middleware.py
   │        │  │  │  ├─ storage
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  ├─ cookie.cpython-311.pyc
   │        │  │  │  │  │  ├─ fallback.cpython-311.pyc
   │        │  │  │  │  │  └─ session.cpython-311.pyc
   │        │  │  │  │  ├─ base.py
   │        │  │  │  │  ├─ cookie.py
   │        │  │  │  │  ├─ fallback.py
   │        │  │  │  │  └─ session.py
   │        │  │  │  ├─ test.py
   │        │  │  │  ├─ utils.py
   │        │  │  │  └─ views.py
   │        │  │  ├─ postgres
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ apps.cpython-311.pyc
   │        │  │  │  │  ├─ constraints.cpython-311.pyc
   │        │  │  │  │  ├─ expressions.cpython-311.pyc
   │        │  │  │  │  ├─ functions.cpython-311.pyc
   │        │  │  │  │  ├─ indexes.cpython-311.pyc
   │        │  │  │  │  ├─ lookups.cpython-311.pyc
   │        │  │  │  │  ├─ operations.cpython-311.pyc
   │        │  │  │  │  ├─ search.cpython-311.pyc
   │        │  │  │  │  ├─ serializers.cpython-311.pyc
   │        │  │  │  │  ├─ signals.cpython-311.pyc
   │        │  │  │  │  ├─ utils.cpython-311.pyc
   │        │  │  │  │  └─ validators.cpython-311.pyc
   │        │  │  │  ├─ aggregates
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ general.cpython-311.pyc
   │        │  │  │  │  │  ├─ mixins.cpython-311.pyc
   │        │  │  │  │  │  └─ statistics.cpython-311.pyc
   │        │  │  │  │  ├─ general.py
   │        │  │  │  │  ├─ mixins.py
   │        │  │  │  │  └─ statistics.py
   │        │  │  │  ├─ apps.py
   │        │  │  │  ├─ constraints.py
   │        │  │  │  ├─ expressions.py
   │        │  │  │  ├─ fields
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ array.cpython-311.pyc
   │        │  │  │  │  │  ├─ citext.cpython-311.pyc
   │        │  │  │  │  │  ├─ hstore.cpython-311.pyc
   │        │  │  │  │  │  ├─ jsonb.cpython-311.pyc
   │        │  │  │  │  │  ├─ ranges.cpython-311.pyc
   │        │  │  │  │  │  └─ utils.cpython-311.pyc
   │        │  │  │  │  ├─ array.py
   │        │  │  │  │  ├─ citext.py
   │        │  │  │  │  ├─ hstore.py
   │        │  │  │  │  ├─ jsonb.py
   │        │  │  │  │  ├─ ranges.py
   │        │  │  │  │  └─ utils.py
   │        │  │  │  ├─ forms
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ array.cpython-311.pyc
   │        │  │  │  │  │  ├─ hstore.cpython-311.pyc
   │        │  │  │  │  │  └─ ranges.cpython-311.pyc
   │        │  │  │  │  ├─ array.py
   │        │  │  │  │  ├─ hstore.py
   │        │  │  │  │  └─ ranges.py
   │        │  │  │  ├─ functions.py
   │        │  │  │  ├─ indexes.py
   │        │  │  │  ├─ jinja2
   │        │  │  │  │  └─ postgres
   │        │  │  │  │     └─ widgets
   │        │  │  │  │        └─ split_array.html
   │        │  │  │  ├─ locale
   │        │  │  │  │  ├─ af
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar_DZ
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ az
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ be
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ca
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ckb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ cs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ da
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ de
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ dsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ el
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en_AU
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ eo
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_AR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_CO
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_MX
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ et
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ eu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ga
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ gd
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ gl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ he
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ia
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ id
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ is
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ it
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ja
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ka
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ko
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ky
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ml
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ms
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ne
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pt_BR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ro
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ru
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sq
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sr_Latn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ug
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ uk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ uz
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ zh_Hans
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  └─ zh_Hant
   │        │  │  │  │     └─ LC_MESSAGES
   │        │  │  │  │        ├─ django.mo
   │        │  │  │  │        └─ django.po
   │        │  │  │  ├─ lookups.py
   │        │  │  │  ├─ operations.py
   │        │  │  │  ├─ search.py
   │        │  │  │  ├─ serializers.py
   │        │  │  │  ├─ signals.py
   │        │  │  │  ├─ templates
   │        │  │  │  │  └─ postgres
   │        │  │  │  │     └─ widgets
   │        │  │  │  │        └─ split_array.html
   │        │  │  │  ├─ utils.py
   │        │  │  │  └─ validators.py
   │        │  │  ├─ redirects
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ admin.cpython-311.pyc
   │        │  │  │  │  ├─ apps.cpython-311.pyc
   │        │  │  │  │  ├─ middleware.cpython-311.pyc
   │        │  │  │  │  └─ models.cpython-311.pyc
   │        │  │  │  ├─ admin.py
   │        │  │  │  ├─ apps.py
   │        │  │  │  ├─ locale
   │        │  │  │  │  ├─ af
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar_DZ
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ast
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ az
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ be
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ br
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ca
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ckb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ cs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ cy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ da
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ de
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ dsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ el
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en_AU
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en_GB
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ eo
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_AR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_CO
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_MX
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_VE
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ et
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ eu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ga
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ gd
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ gl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ he
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ia
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ id
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ io
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ is
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ it
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ja
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ka
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kab
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ km
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ko
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ky
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ml
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ms
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ my
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ne
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ os
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pt_BR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ro
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ru
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sq
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sr_Latn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sw
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ta
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ te
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ th
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ udm
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ug
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ uk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ur
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ uz
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ vi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ zh_Hans
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  └─ zh_Hant
   │        │  │  │  │     └─ LC_MESSAGES
   │        │  │  │  │        ├─ django.mo
   │        │  │  │  │        └─ django.po
   │        │  │  │  ├─ middleware.py
   │        │  │  │  ├─ migrations
   │        │  │  │  │  ├─ 0001_initial.py
   │        │  │  │  │  ├─ 0002_alter_redirect_new_path_help_text.py
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  └─ __pycache__
   │        │  │  │  │     ├─ 0001_initial.cpython-311.pyc
   │        │  │  │  │     ├─ 0002_alter_redirect_new_path_help_text.cpython-311.pyc
   │        │  │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  │  └─ models.py
   │        │  │  ├─ sessions
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ apps.cpython-311.pyc
   │        │  │  │  │  ├─ base_session.cpython-311.pyc
   │        │  │  │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  │  │  ├─ middleware.cpython-311.pyc
   │        │  │  │  │  ├─ models.cpython-311.pyc
   │        │  │  │  │  └─ serializers.cpython-311.pyc
   │        │  │  │  ├─ apps.py
   │        │  │  │  ├─ backends
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  ├─ cache.cpython-311.pyc
   │        │  │  │  │  │  ├─ cached_db.cpython-311.pyc
   │        │  │  │  │  │  ├─ db.cpython-311.pyc
   │        │  │  │  │  │  ├─ file.cpython-311.pyc
   │        │  │  │  │  │  └─ signed_cookies.cpython-311.pyc
   │        │  │  │  │  ├─ base.py
   │        │  │  │  │  ├─ cache.py
   │        │  │  │  │  ├─ cached_db.py
   │        │  │  │  │  ├─ db.py
   │        │  │  │  │  ├─ file.py
   │        │  │  │  │  └─ signed_cookies.py
   │        │  │  │  ├─ base_session.py
   │        │  │  │  ├─ exceptions.py
   │        │  │  │  ├─ locale
   │        │  │  │  │  ├─ af
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar_DZ
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ast
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ az
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ be
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ br
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ca
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ckb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ cs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ cy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ da
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ de
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ dsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ el
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en_AU
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en_GB
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ eo
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_AR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_CO
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_MX
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_VE
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ et
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ eu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ga
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ gd
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ gl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ he
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ia
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ id
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ io
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ is
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ it
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ja
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ka
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kab
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ km
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ko
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ky
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ml
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ms
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ my
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ne
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ os
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pt_BR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ro
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ru
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sq
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sr_Latn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sw
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ta
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ te
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ th
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ udm
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ug
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ uk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ur
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ uz
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ vi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ zh_Hans
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  └─ zh_Hant
   │        │  │  │  │     └─ LC_MESSAGES
   │        │  │  │  │        ├─ django.mo
   │        │  │  │  │        └─ django.po
   │        │  │  │  ├─ management
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  │  │  └─ commands
   │        │  │  │  │     ├─ __init__.py
   │        │  │  │  │     ├─ __pycache__
   │        │  │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │     │  └─ clearsessions.cpython-311.pyc
   │        │  │  │  │     └─ clearsessions.py
   │        │  │  │  ├─ middleware.py
   │        │  │  │  ├─ migrations
   │        │  │  │  │  ├─ 0001_initial.py
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  └─ __pycache__
   │        │  │  │  │     ├─ 0001_initial.cpython-311.pyc
   │        │  │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  │  ├─ models.py
   │        │  │  │  └─ serializers.py
   │        │  │  ├─ sitemaps
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ apps.cpython-311.pyc
   │        │  │  │  │  └─ views.cpython-311.pyc
   │        │  │  │  ├─ apps.py
   │        │  │  │  ├─ templates
   │        │  │  │  │  ├─ sitemap.xml
   │        │  │  │  │  └─ sitemap_index.xml
   │        │  │  │  └─ views.py
   │        │  │  ├─ sites
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ admin.cpython-311.pyc
   │        │  │  │  │  ├─ apps.cpython-311.pyc
   │        │  │  │  │  ├─ checks.cpython-311.pyc
   │        │  │  │  │  ├─ management.cpython-311.pyc
   │        │  │  │  │  ├─ managers.cpython-311.pyc
   │        │  │  │  │  ├─ middleware.cpython-311.pyc
   │        │  │  │  │  ├─ models.cpython-311.pyc
   │        │  │  │  │  ├─ requests.cpython-311.pyc
   │        │  │  │  │  └─ shortcuts.cpython-311.pyc
   │        │  │  │  ├─ admin.py
   │        │  │  │  ├─ apps.py
   │        │  │  │  ├─ checks.py
   │        │  │  │  ├─ locale
   │        │  │  │  │  ├─ af
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ar_DZ
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ast
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ az
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ be
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ br
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ bs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ca
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ckb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ cs
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ cy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ da
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ de
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ dsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ el
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en_AU
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ en_GB
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ eo
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_AR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_CO
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_MX
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ es_VE
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ et
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ eu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ fy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ga
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ gd
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ gl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ he
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hsb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hu
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ hy
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ia
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ id
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ io
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ is
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ it
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ja
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ka
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kab
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ km
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ kn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ko
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ky
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ lv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ml
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ mr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ms
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ my
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nb
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ne
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ nn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ os
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pa
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ pt_BR
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ro
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ru
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sl
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sq
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sr_Latn
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sv
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ sw
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ta
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ te
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tg
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ th
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tr
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ tt
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ udm
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ug
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ uk
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ ur
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ uz
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ vi
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  ├─ zh_Hans
   │        │  │  │  │  │  └─ LC_MESSAGES
   │        │  │  │  │  │     ├─ django.mo
   │        │  │  │  │  │     └─ django.po
   │        │  │  │  │  └─ zh_Hant
   │        │  │  │  │     └─ LC_MESSAGES
   │        │  │  │  │        ├─ django.mo
   │        │  │  │  │        └─ django.po
   │        │  │  │  ├─ management.py
   │        │  │  │  ├─ managers.py
   │        │  │  │  ├─ middleware.py
   │        │  │  │  ├─ migrations
   │        │  │  │  │  ├─ 0001_initial.py
   │        │  │  │  │  ├─ 0002_alter_domain_unique.py
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  └─ __pycache__
   │        │  │  │  │     ├─ 0001_initial.cpython-311.pyc
   │        │  │  │  │     ├─ 0002_alter_domain_unique.cpython-311.pyc
   │        │  │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  │  ├─ models.py
   │        │  │  │  ├─ requests.py
   │        │  │  │  └─ shortcuts.py
   │        │  │  ├─ staticfiles
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ apps.cpython-311.pyc
   │        │  │  │  │  ├─ checks.cpython-311.pyc
   │        │  │  │  │  ├─ finders.cpython-311.pyc
   │        │  │  │  │  ├─ handlers.cpython-311.pyc
   │        │  │  │  │  ├─ storage.cpython-311.pyc
   │        │  │  │  │  ├─ testing.cpython-311.pyc
   │        │  │  │  │  ├─ urls.cpython-311.pyc
   │        │  │  │  │  ├─ utils.cpython-311.pyc
   │        │  │  │  │  └─ views.cpython-311.pyc
   │        │  │  │  ├─ apps.py
   │        │  │  │  ├─ checks.py
   │        │  │  │  ├─ finders.py
   │        │  │  │  ├─ handlers.py
   │        │  │  │  ├─ management
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  │  │  └─ commands
   │        │  │  │  │     ├─ __init__.py
   │        │  │  │  │     ├─ __pycache__
   │        │  │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │     │  ├─ collectstatic.cpython-311.pyc
   │        │  │  │  │     │  ├─ findstatic.cpython-311.pyc
   │        │  │  │  │     │  └─ runserver.cpython-311.pyc
   │        │  │  │  │     ├─ collectstatic.py
   │        │  │  │  │     ├─ findstatic.py
   │        │  │  │  │     └─ runserver.py
   │        │  │  │  ├─ storage.py
   │        │  │  │  ├─ testing.py
   │        │  │  │  ├─ urls.py
   │        │  │  │  ├─ utils.py
   │        │  │  │  └─ views.py
   │        │  │  └─ syndication
   │        │  │     ├─ __init__.py
   │        │  │     ├─ __pycache__
   │        │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │     │  ├─ apps.cpython-311.pyc
   │        │  │     │  └─ views.cpython-311.pyc
   │        │  │     ├─ apps.py
   │        │  │     └─ views.py
   │        │  ├─ core
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ asgi.cpython-311.pyc
   │        │  │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  │  ├─ paginator.cpython-311.pyc
   │        │  │  │  ├─ signals.cpython-311.pyc
   │        │  │  │  ├─ signing.cpython-311.pyc
   │        │  │  │  ├─ validators.cpython-311.pyc
   │        │  │  │  └─ wsgi.cpython-311.pyc
   │        │  │  ├─ asgi.py
   │        │  │  ├─ cache
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  └─ utils.cpython-311.pyc
   │        │  │  │  ├─ backends
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  ├─ db.cpython-311.pyc
   │        │  │  │  │  │  ├─ dummy.cpython-311.pyc
   │        │  │  │  │  │  ├─ filebased.cpython-311.pyc
   │        │  │  │  │  │  ├─ locmem.cpython-311.pyc
   │        │  │  │  │  │  ├─ memcached.cpython-311.pyc
   │        │  │  │  │  │  └─ redis.cpython-311.pyc
   │        │  │  │  │  ├─ base.py
   │        │  │  │  │  ├─ db.py
   │        │  │  │  │  ├─ dummy.py
   │        │  │  │  │  ├─ filebased.py
   │        │  │  │  │  ├─ locmem.py
   │        │  │  │  │  ├─ memcached.py
   │        │  │  │  │  └─ redis.py
   │        │  │  │  └─ utils.py
   │        │  │  ├─ checks
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ async_checks.cpython-311.pyc
   │        │  │  │  │  ├─ caches.cpython-311.pyc
   │        │  │  │  │  ├─ commands.cpython-311.pyc
   │        │  │  │  │  ├─ database.cpython-311.pyc
   │        │  │  │  │  ├─ files.cpython-311.pyc
   │        │  │  │  │  ├─ messages.cpython-311.pyc
   │        │  │  │  │  ├─ model_checks.cpython-311.pyc
   │        │  │  │  │  ├─ registry.cpython-311.pyc
   │        │  │  │  │  ├─ templates.cpython-311.pyc
   │        │  │  │  │  ├─ translation.cpython-311.pyc
   │        │  │  │  │  └─ urls.cpython-311.pyc
   │        │  │  │  ├─ async_checks.py
   │        │  │  │  ├─ caches.py
   │        │  │  │  ├─ commands.py
   │        │  │  │  ├─ compatibility
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ django_4_0.cpython-311.pyc
   │        │  │  │  │  └─ django_4_0.py
   │        │  │  │  ├─ database.py
   │        │  │  │  ├─ files.py
   │        │  │  │  ├─ messages.py
   │        │  │  │  ├─ model_checks.py
   │        │  │  │  ├─ registry.py
   │        │  │  │  ├─ security
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  ├─ csrf.cpython-311.pyc
   │        │  │  │  │  │  └─ sessions.cpython-311.pyc
   │        │  │  │  │  ├─ base.py
   │        │  │  │  │  ├─ csrf.py
   │        │  │  │  │  └─ sessions.py
   │        │  │  │  ├─ templates.py
   │        │  │  │  ├─ translation.py
   │        │  │  │  └─ urls.py
   │        │  │  ├─ exceptions.py
   │        │  │  ├─ files
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  ├─ images.cpython-311.pyc
   │        │  │  │  │  ├─ locks.cpython-311.pyc
   │        │  │  │  │  ├─ move.cpython-311.pyc
   │        │  │  │  │  ├─ temp.cpython-311.pyc
   │        │  │  │  │  ├─ uploadedfile.cpython-311.pyc
   │        │  │  │  │  ├─ uploadhandler.cpython-311.pyc
   │        │  │  │  │  └─ utils.cpython-311.pyc
   │        │  │  │  ├─ base.py
   │        │  │  │  ├─ images.py
   │        │  │  │  ├─ locks.py
   │        │  │  │  ├─ move.py
   │        │  │  │  ├─ storage
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  ├─ filesystem.cpython-311.pyc
   │        │  │  │  │  │  ├─ handler.cpython-311.pyc
   │        │  │  │  │  │  ├─ memory.cpython-311.pyc
   │        │  │  │  │  │  └─ mixins.cpython-311.pyc
   │        │  │  │  │  ├─ base.py
   │        │  │  │  │  ├─ filesystem.py
   │        │  │  │  │  ├─ handler.py
   │        │  │  │  │  ├─ memory.py
   │        │  │  │  │  └─ mixins.py
   │        │  │  │  ├─ temp.py
   │        │  │  │  ├─ uploadedfile.py
   │        │  │  │  ├─ uploadhandler.py
   │        │  │  │  └─ utils.py
   │        │  │  ├─ handlers
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ asgi.cpython-311.pyc
   │        │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  ├─ exception.cpython-311.pyc
   │        │  │  │  │  └─ wsgi.cpython-311.pyc
   │        │  │  │  ├─ asgi.py
   │        │  │  │  ├─ base.py
   │        │  │  │  ├─ exception.py
   │        │  │  │  └─ wsgi.py
   │        │  │  ├─ mail
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ message.cpython-311.pyc
   │        │  │  │  │  └─ utils.cpython-311.pyc
   │        │  │  │  ├─ backends
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  ├─ console.cpython-311.pyc
   │        │  │  │  │  │  ├─ dummy.cpython-311.pyc
   │        │  │  │  │  │  ├─ filebased.cpython-311.pyc
   │        │  │  │  │  │  ├─ locmem.cpython-311.pyc
   │        │  │  │  │  │  └─ smtp.cpython-311.pyc
   │        │  │  │  │  ├─ base.py
   │        │  │  │  │  ├─ console.py
   │        │  │  │  │  ├─ dummy.py
   │        │  │  │  │  ├─ filebased.py
   │        │  │  │  │  ├─ locmem.py
   │        │  │  │  │  └─ smtp.py
   │        │  │  │  ├─ message.py
   │        │  │  │  └─ utils.py
   │        │  │  ├─ management
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  ├─ color.cpython-311.pyc
   │        │  │  │  │  ├─ sql.cpython-311.pyc
   │        │  │  │  │  ├─ templates.cpython-311.pyc
   │        │  │  │  │  └─ utils.cpython-311.pyc
   │        │  │  │  ├─ base.py
   │        │  │  │  ├─ color.py
   │        │  │  │  ├─ commands
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ check.cpython-311.pyc
   │        │  │  │  │  │  ├─ compilemessages.cpython-311.pyc
   │        │  │  │  │  │  ├─ createcachetable.cpython-311.pyc
   │        │  │  │  │  │  ├─ dbshell.cpython-311.pyc
   │        │  │  │  │  │  ├─ diffsettings.cpython-311.pyc
   │        │  │  │  │  │  ├─ dumpdata.cpython-311.pyc
   │        │  │  │  │  │  ├─ flush.cpython-311.pyc
   │        │  │  │  │  │  ├─ inspectdb.cpython-311.pyc
   │        │  │  │  │  │  ├─ loaddata.cpython-311.pyc
   │        │  │  │  │  │  ├─ makemessages.cpython-311.pyc
   │        │  │  │  │  │  ├─ makemigrations.cpython-311.pyc
   │        │  │  │  │  │  ├─ migrate.cpython-311.pyc
   │        │  │  │  │  │  ├─ optimizemigration.cpython-311.pyc
   │        │  │  │  │  │  ├─ runserver.cpython-311.pyc
   │        │  │  │  │  │  ├─ sendtestemail.cpython-311.pyc
   │        │  │  │  │  │  ├─ shell.cpython-311.pyc
   │        │  │  │  │  │  ├─ showmigrations.cpython-311.pyc
   │        │  │  │  │  │  ├─ sqlflush.cpython-311.pyc
   │        │  │  │  │  │  ├─ sqlmigrate.cpython-311.pyc
   │        │  │  │  │  │  ├─ sqlsequencereset.cpython-311.pyc
   │        │  │  │  │  │  ├─ squashmigrations.cpython-311.pyc
   │        │  │  │  │  │  ├─ startapp.cpython-311.pyc
   │        │  │  │  │  │  ├─ startproject.cpython-311.pyc
   │        │  │  │  │  │  ├─ test.cpython-311.pyc
   │        │  │  │  │  │  └─ testserver.cpython-311.pyc
   │        │  │  │  │  ├─ check.py
   │        │  │  │  │  ├─ compilemessages.py
   │        │  │  │  │  ├─ createcachetable.py
   │        │  │  │  │  ├─ dbshell.py
   │        │  │  │  │  ├─ diffsettings.py
   │        │  │  │  │  ├─ dumpdata.py
   │        │  │  │  │  ├─ flush.py
   │        │  │  │  │  ├─ inspectdb.py
   │        │  │  │  │  ├─ loaddata.py
   │        │  │  │  │  ├─ makemessages.py
   │        │  │  │  │  ├─ makemigrations.py
   │        │  │  │  │  ├─ migrate.py
   │        │  │  │  │  ├─ optimizemigration.py
   │        │  │  │  │  ├─ runserver.py
   │        │  │  │  │  ├─ sendtestemail.py
   │        │  │  │  │  ├─ shell.py
   │        │  │  │  │  ├─ showmigrations.py
   │        │  │  │  │  ├─ sqlflush.py
   │        │  │  │  │  ├─ sqlmigrate.py
   │        │  │  │  │  ├─ sqlsequencereset.py
   │        │  │  │  │  ├─ squashmigrations.py
   │        │  │  │  │  ├─ startapp.py
   │        │  │  │  │  ├─ startproject.py
   │        │  │  │  │  ├─ test.py
   │        │  │  │  │  └─ testserver.py
   │        │  │  │  ├─ sql.py
   │        │  │  │  ├─ templates.py
   │        │  │  │  └─ utils.py
   │        │  │  ├─ paginator.py
   │        │  │  ├─ serializers
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  ├─ json.cpython-311.pyc
   │        │  │  │  │  ├─ jsonl.cpython-311.pyc
   │        │  │  │  │  ├─ python.cpython-311.pyc
   │        │  │  │  │  ├─ pyyaml.cpython-311.pyc
   │        │  │  │  │  └─ xml_serializer.cpython-311.pyc
   │        │  │  │  ├─ base.py
   │        │  │  │  ├─ json.py
   │        │  │  │  ├─ jsonl.py
   │        │  │  │  ├─ python.py
   │        │  │  │  ├─ pyyaml.py
   │        │  │  │  └─ xml_serializer.py
   │        │  │  ├─ servers
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  └─ basehttp.cpython-311.pyc
   │        │  │  │  └─ basehttp.py
   │        │  │  ├─ signals.py
   │        │  │  ├─ signing.py
   │        │  │  ├─ validators.py
   │        │  │  └─ wsgi.py
   │        │  ├─ db
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ transaction.cpython-311.pyc
   │        │  │  │  └─ utils.cpython-311.pyc
   │        │  │  ├─ backends
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ ddl_references.cpython-311.pyc
   │        │  │  │  │  ├─ signals.cpython-311.pyc
   │        │  │  │  │  └─ utils.cpython-311.pyc
   │        │  │  │  ├─ base
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  ├─ client.cpython-311.pyc
   │        │  │  │  │  │  ├─ creation.cpython-311.pyc
   │        │  │  │  │  │  ├─ features.cpython-311.pyc
   │        │  │  │  │  │  ├─ introspection.cpython-311.pyc
   │        │  │  │  │  │  ├─ operations.cpython-311.pyc
   │        │  │  │  │  │  ├─ schema.cpython-311.pyc
   │        │  │  │  │  │  └─ validation.cpython-311.pyc
   │        │  │  │  │  ├─ base.py
   │        │  │  │  │  ├─ client.py
   │        │  │  │  │  ├─ creation.py
   │        │  │  │  │  ├─ features.py
   │        │  │  │  │  ├─ introspection.py
   │        │  │  │  │  ├─ operations.py
   │        │  │  │  │  ├─ schema.py
   │        │  │  │  │  └─ validation.py
   │        │  │  │  ├─ ddl_references.py
   │        │  │  │  ├─ dummy
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  └─ features.cpython-311.pyc
   │        │  │  │  │  ├─ base.py
   │        │  │  │  │  └─ features.py
   │        │  │  │  ├─ mysql
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  ├─ client.cpython-311.pyc
   │        │  │  │  │  │  ├─ compiler.cpython-311.pyc
   │        │  │  │  │  │  ├─ creation.cpython-311.pyc
   │        │  │  │  │  │  ├─ features.cpython-311.pyc
   │        │  │  │  │  │  ├─ introspection.cpython-311.pyc
   │        │  │  │  │  │  ├─ operations.cpython-311.pyc
   │        │  │  │  │  │  ├─ schema.cpython-311.pyc
   │        │  │  │  │  │  └─ validation.cpython-311.pyc
   │        │  │  │  │  ├─ base.py
   │        │  │  │  │  ├─ client.py
   │        │  │  │  │  ├─ compiler.py
   │        │  │  │  │  ├─ creation.py
   │        │  │  │  │  ├─ features.py
   │        │  │  │  │  ├─ introspection.py
   │        │  │  │  │  ├─ operations.py
   │        │  │  │  │  ├─ schema.py
   │        │  │  │  │  └─ validation.py
   │        │  │  │  ├─ oracle
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  ├─ client.cpython-311.pyc
   │        │  │  │  │  │  ├─ creation.cpython-311.pyc
   │        │  │  │  │  │  ├─ features.cpython-311.pyc
   │        │  │  │  │  │  ├─ functions.cpython-311.pyc
   │        │  │  │  │  │  ├─ introspection.cpython-311.pyc
   │        │  │  │  │  │  ├─ operations.cpython-311.pyc
   │        │  │  │  │  │  ├─ oracledb_any.cpython-311.pyc
   │        │  │  │  │  │  ├─ schema.cpython-311.pyc
   │        │  │  │  │  │  ├─ utils.cpython-311.pyc
   │        │  │  │  │  │  └─ validation.cpython-311.pyc
   │        │  │  │  │  ├─ base.py
   │        │  │  │  │  ├─ client.py
   │        │  │  │  │  ├─ creation.py
   │        │  │  │  │  ├─ features.py
   │        │  │  │  │  ├─ functions.py
   │        │  │  │  │  ├─ introspection.py
   │        │  │  │  │  ├─ operations.py
   │        │  │  │  │  ├─ oracledb_any.py
   │        │  │  │  │  ├─ schema.py
   │        │  │  │  │  ├─ utils.py
   │        │  │  │  │  └─ validation.py
   │        │  │  │  ├─ postgresql
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  ├─ client.cpython-311.pyc
   │        │  │  │  │  │  ├─ compiler.cpython-311.pyc
   │        │  │  │  │  │  ├─ creation.cpython-311.pyc
   │        │  │  │  │  │  ├─ features.cpython-311.pyc
   │        │  │  │  │  │  ├─ introspection.cpython-311.pyc
   │        │  │  │  │  │  ├─ operations.cpython-311.pyc
   │        │  │  │  │  │  ├─ psycopg_any.cpython-311.pyc
   │        │  │  │  │  │  └─ schema.cpython-311.pyc
   │        │  │  │  │  ├─ base.py
   │        │  │  │  │  ├─ client.py
   │        │  │  │  │  ├─ compiler.py
   │        │  │  │  │  ├─ creation.py
   │        │  │  │  │  ├─ features.py
   │        │  │  │  │  ├─ introspection.py
   │        │  │  │  │  ├─ operations.py
   │        │  │  │  │  ├─ psycopg_any.py
   │        │  │  │  │  └─ schema.py
   │        │  │  │  ├─ signals.py
   │        │  │  │  ├─ sqlite3
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ _functions.cpython-311.pyc
   │        │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  ├─ client.cpython-311.pyc
   │        │  │  │  │  │  ├─ creation.cpython-311.pyc
   │        │  │  │  │  │  ├─ features.cpython-311.pyc
   │        │  │  │  │  │  ├─ introspection.cpython-311.pyc
   │        │  │  │  │  │  ├─ operations.cpython-311.pyc
   │        │  │  │  │  │  └─ schema.cpython-311.pyc
   │        │  │  │  │  ├─ _functions.py
   │        │  │  │  │  ├─ base.py
   │        │  │  │  │  ├─ client.py
   │        │  │  │  │  ├─ creation.py
   │        │  │  │  │  ├─ features.py
   │        │  │  │  │  ├─ introspection.py
   │        │  │  │  │  ├─ operations.py
   │        │  │  │  │  └─ schema.py
   │        │  │  │  └─ utils.py
   │        │  │  ├─ migrations
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ autodetector.cpython-311.pyc
   │        │  │  │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  │  │  ├─ executor.cpython-311.pyc
   │        │  │  │  │  ├─ graph.cpython-311.pyc
   │        │  │  │  │  ├─ loader.cpython-311.pyc
   │        │  │  │  │  ├─ migration.cpython-311.pyc
   │        │  │  │  │  ├─ optimizer.cpython-311.pyc
   │        │  │  │  │  ├─ questioner.cpython-311.pyc
   │        │  │  │  │  ├─ recorder.cpython-311.pyc
   │        │  │  │  │  ├─ serializer.cpython-311.pyc
   │        │  │  │  │  ├─ state.cpython-311.pyc
   │        │  │  │  │  ├─ utils.cpython-311.pyc
   │        │  │  │  │  └─ writer.cpython-311.pyc
   │        │  │  │  ├─ autodetector.py
   │        │  │  │  ├─ exceptions.py
   │        │  │  │  ├─ executor.py
   │        │  │  │  ├─ graph.py
   │        │  │  │  ├─ loader.py
   │        │  │  │  ├─ migration.py
   │        │  │  │  ├─ operations
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  ├─ fields.cpython-311.pyc
   │        │  │  │  │  │  ├─ models.cpython-311.pyc
   │        │  │  │  │  │  └─ special.cpython-311.pyc
   │        │  │  │  │  ├─ base.py
   │        │  │  │  │  ├─ fields.py
   │        │  │  │  │  ├─ models.py
   │        │  │  │  │  └─ special.py
   │        │  │  │  ├─ optimizer.py
   │        │  │  │  ├─ questioner.py
   │        │  │  │  ├─ recorder.py
   │        │  │  │  ├─ serializer.py
   │        │  │  │  ├─ state.py
   │        │  │  │  ├─ utils.py
   │        │  │  │  └─ writer.py
   │        │  │  ├─ models
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ aggregates.cpython-311.pyc
   │        │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  ├─ constants.cpython-311.pyc
   │        │  │  │  │  ├─ constraints.cpython-311.pyc
   │        │  │  │  │  ├─ deletion.cpython-311.pyc
   │        │  │  │  │  ├─ enums.cpython-311.pyc
   │        │  │  │  │  ├─ expressions.cpython-311.pyc
   │        │  │  │  │  ├─ indexes.cpython-311.pyc
   │        │  │  │  │  ├─ lookups.cpython-311.pyc
   │        │  │  │  │  ├─ manager.cpython-311.pyc
   │        │  │  │  │  ├─ options.cpython-311.pyc
   │        │  │  │  │  ├─ query.cpython-311.pyc
   │        │  │  │  │  ├─ query_utils.cpython-311.pyc
   │        │  │  │  │  ├─ signals.cpython-311.pyc
   │        │  │  │  │  └─ utils.cpython-311.pyc
   │        │  │  │  ├─ aggregates.py
   │        │  │  │  ├─ base.py
   │        │  │  │  ├─ constants.py
   │        │  │  │  ├─ constraints.py
   │        │  │  │  ├─ deletion.py
   │        │  │  │  ├─ enums.py
   │        │  │  │  ├─ expressions.py
   │        │  │  │  ├─ fields
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ composite.cpython-311.pyc
   │        │  │  │  │  │  ├─ files.cpython-311.pyc
   │        │  │  │  │  │  ├─ generated.cpython-311.pyc
   │        │  │  │  │  │  ├─ json.cpython-311.pyc
   │        │  │  │  │  │  ├─ mixins.cpython-311.pyc
   │        │  │  │  │  │  ├─ proxy.cpython-311.pyc
   │        │  │  │  │  │  ├─ related.cpython-311.pyc
   │        │  │  │  │  │  ├─ related_descriptors.cpython-311.pyc
   │        │  │  │  │  │  ├─ related_lookups.cpython-311.pyc
   │        │  │  │  │  │  ├─ reverse_related.cpython-311.pyc
   │        │  │  │  │  │  └─ tuple_lookups.cpython-311.pyc
   │        │  │  │  │  ├─ composite.py
   │        │  │  │  │  ├─ files.py
   │        │  │  │  │  ├─ generated.py
   │        │  │  │  │  ├─ json.py
   │        │  │  │  │  ├─ mixins.py
   │        │  │  │  │  ├─ proxy.py
   │        │  │  │  │  ├─ related.py
   │        │  │  │  │  ├─ related_descriptors.py
   │        │  │  │  │  ├─ related_lookups.py
   │        │  │  │  │  ├─ reverse_related.py
   │        │  │  │  │  └─ tuple_lookups.py
   │        │  │  │  ├─ functions
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ comparison.cpython-311.pyc
   │        │  │  │  │  │  ├─ datetime.cpython-311.pyc
   │        │  │  │  │  │  ├─ json.cpython-311.pyc
   │        │  │  │  │  │  ├─ math.cpython-311.pyc
   │        │  │  │  │  │  ├─ mixins.cpython-311.pyc
   │        │  │  │  │  │  ├─ text.cpython-311.pyc
   │        │  │  │  │  │  └─ window.cpython-311.pyc
   │        │  │  │  │  ├─ comparison.py
   │        │  │  │  │  ├─ datetime.py
   │        │  │  │  │  ├─ json.py
   │        │  │  │  │  ├─ math.py
   │        │  │  │  │  ├─ mixins.py
   │        │  │  │  │  ├─ text.py
   │        │  │  │  │  └─ window.py
   │        │  │  │  ├─ indexes.py
   │        │  │  │  ├─ lookups.py
   │        │  │  │  ├─ manager.py
   │        │  │  │  ├─ options.py
   │        │  │  │  ├─ query.py
   │        │  │  │  ├─ query_utils.py
   │        │  │  │  ├─ signals.py
   │        │  │  │  ├─ sql
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ compiler.cpython-311.pyc
   │        │  │  │  │  │  ├─ constants.cpython-311.pyc
   │        │  │  │  │  │  ├─ datastructures.cpython-311.pyc
   │        │  │  │  │  │  ├─ query.cpython-311.pyc
   │        │  │  │  │  │  ├─ subqueries.cpython-311.pyc
   │        │  │  │  │  │  └─ where.cpython-311.pyc
   │        │  │  │  │  ├─ compiler.py
   │        │  │  │  │  ├─ constants.py
   │        │  │  │  │  ├─ datastructures.py
   │        │  │  │  │  ├─ query.py
   │        │  │  │  │  ├─ subqueries.py
   │        │  │  │  │  └─ where.py
   │        │  │  │  └─ utils.py
   │        │  │  ├─ transaction.py
   │        │  │  └─ utils.py
   │        │  ├─ dispatch
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  └─ dispatcher.cpython-311.pyc
   │        │  │  ├─ dispatcher.py
   │        │  │  └─ license.txt
   │        │  ├─ forms
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ boundfield.cpython-311.pyc
   │        │  │  │  ├─ fields.cpython-311.pyc
   │        │  │  │  ├─ forms.cpython-311.pyc
   │        │  │  │  ├─ formsets.cpython-311.pyc
   │        │  │  │  ├─ models.cpython-311.pyc
   │        │  │  │  ├─ renderers.cpython-311.pyc
   │        │  │  │  ├─ utils.cpython-311.pyc
   │        │  │  │  └─ widgets.cpython-311.pyc
   │        │  │  ├─ boundfield.py
   │        │  │  ├─ fields.py
   │        │  │  ├─ forms.py
   │        │  │  ├─ formsets.py
   │        │  │  ├─ jinja2
   │        │  │  │  └─ django
   │        │  │  │     └─ forms
   │        │  │  │        ├─ attrs.html
   │        │  │  │        ├─ div.html
   │        │  │  │        ├─ errors
   │        │  │  │        │  ├─ dict
   │        │  │  │        │  │  ├─ default.html
   │        │  │  │        │  │  ├─ text.txt
   │        │  │  │        │  │  └─ ul.html
   │        │  │  │        │  └─ list
   │        │  │  │        │     ├─ default.html
   │        │  │  │        │     ├─ text.txt
   │        │  │  │        │     └─ ul.html
   │        │  │  │        ├─ field.html
   │        │  │  │        ├─ formsets
   │        │  │  │        │  ├─ div.html
   │        │  │  │        │  ├─ p.html
   │        │  │  │        │  ├─ table.html
   │        │  │  │        │  └─ ul.html
   │        │  │  │        ├─ label.html
   │        │  │  │        ├─ p.html
   │        │  │  │        ├─ table.html
   │        │  │  │        ├─ ul.html
   │        │  │  │        └─ widgets
   │        │  │  │           ├─ attrs.html
   │        │  │  │           ├─ checkbox.html
   │        │  │  │           ├─ checkbox_option.html
   │        │  │  │           ├─ checkbox_select.html
   │        │  │  │           ├─ clearable_file_input.html
   │        │  │  │           ├─ color.html
   │        │  │  │           ├─ date.html
   │        │  │  │           ├─ datetime.html
   │        │  │  │           ├─ email.html
   │        │  │  │           ├─ file.html
   │        │  │  │           ├─ hidden.html
   │        │  │  │           ├─ input.html
   │        │  │  │           ├─ input_option.html
   │        │  │  │           ├─ multiple_hidden.html
   │        │  │  │           ├─ multiple_input.html
   │        │  │  │           ├─ multiwidget.html
   │        │  │  │           ├─ number.html
   │        │  │  │           ├─ password.html
   │        │  │  │           ├─ radio.html
   │        │  │  │           ├─ radio_option.html
   │        │  │  │           ├─ search.html
   │        │  │  │           ├─ select.html
   │        │  │  │           ├─ select_date.html
   │        │  │  │           ├─ select_option.html
   │        │  │  │           ├─ splitdatetime.html
   │        │  │  │           ├─ splithiddendatetime.html
   │        │  │  │           ├─ tel.html
   │        │  │  │           ├─ text.html
   │        │  │  │           ├─ textarea.html
   │        │  │  │           ├─ time.html
   │        │  │  │           └─ url.html
   │        │  │  ├─ models.py
   │        │  │  ├─ renderers.py
   │        │  │  ├─ templates
   │        │  │  │  └─ django
   │        │  │  │     └─ forms
   │        │  │  │        ├─ attrs.html
   │        │  │  │        ├─ div.html
   │        │  │  │        ├─ errors
   │        │  │  │        │  ├─ dict
   │        │  │  │        │  │  ├─ default.html
   │        │  │  │        │  │  ├─ text.txt
   │        │  │  │        │  │  └─ ul.html
   │        │  │  │        │  └─ list
   │        │  │  │        │     ├─ default.html
   │        │  │  │        │     ├─ text.txt
   │        │  │  │        │     └─ ul.html
   │        │  │  │        ├─ field.html
   │        │  │  │        ├─ formsets
   │        │  │  │        │  ├─ div.html
   │        │  │  │        │  ├─ p.html
   │        │  │  │        │  ├─ table.html
   │        │  │  │        │  └─ ul.html
   │        │  │  │        ├─ label.html
   │        │  │  │        ├─ p.html
   │        │  │  │        ├─ table.html
   │        │  │  │        ├─ ul.html
   │        │  │  │        └─ widgets
   │        │  │  │           ├─ attrs.html
   │        │  │  │           ├─ checkbox.html
   │        │  │  │           ├─ checkbox_option.html
   │        │  │  │           ├─ checkbox_select.html
   │        │  │  │           ├─ clearable_file_input.html
   │        │  │  │           ├─ color.html
   │        │  │  │           ├─ date.html
   │        │  │  │           ├─ datetime.html
   │        │  │  │           ├─ email.html
   │        │  │  │           ├─ file.html
   │        │  │  │           ├─ hidden.html
   │        │  │  │           ├─ input.html
   │        │  │  │           ├─ input_option.html
   │        │  │  │           ├─ multiple_hidden.html
   │        │  │  │           ├─ multiple_input.html
   │        │  │  │           ├─ multiwidget.html
   │        │  │  │           ├─ number.html
   │        │  │  │           ├─ password.html
   │        │  │  │           ├─ radio.html
   │        │  │  │           ├─ radio_option.html
   │        │  │  │           ├─ search.html
   │        │  │  │           ├─ select.html
   │        │  │  │           ├─ select_date.html
   │        │  │  │           ├─ select_option.html
   │        │  │  │           ├─ splitdatetime.html
   │        │  │  │           ├─ splithiddendatetime.html
   │        │  │  │           ├─ tel.html
   │        │  │  │           ├─ text.html
   │        │  │  │           ├─ textarea.html
   │        │  │  │           ├─ time.html
   │        │  │  │           └─ url.html
   │        │  │  ├─ utils.py
   │        │  │  └─ widgets.py
   │        │  ├─ http
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ cookie.cpython-311.pyc
   │        │  │  │  ├─ multipartparser.cpython-311.pyc
   │        │  │  │  ├─ request.cpython-311.pyc
   │        │  │  │  └─ response.cpython-311.pyc
   │        │  │  ├─ cookie.py
   │        │  │  ├─ multipartparser.py
   │        │  │  ├─ request.py
   │        │  │  └─ response.py
   │        │  ├─ middleware
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ cache.cpython-311.pyc
   │        │  │  │  ├─ clickjacking.cpython-311.pyc
   │        │  │  │  ├─ common.cpython-311.pyc
   │        │  │  │  ├─ csrf.cpython-311.pyc
   │        │  │  │  ├─ gzip.cpython-311.pyc
   │        │  │  │  ├─ http.cpython-311.pyc
   │        │  │  │  ├─ locale.cpython-311.pyc
   │        │  │  │  └─ security.cpython-311.pyc
   │        │  │  ├─ cache.py
   │        │  │  ├─ clickjacking.py
   │        │  │  ├─ common.py
   │        │  │  ├─ csrf.py
   │        │  │  ├─ gzip.py
   │        │  │  ├─ http.py
   │        │  │  ├─ locale.py
   │        │  │  └─ security.py
   │        │  ├─ shortcuts.py
   │        │  ├─ template
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ autoreload.cpython-311.pyc
   │        │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  ├─ context.cpython-311.pyc
   │        │  │  │  ├─ context_processors.cpython-311.pyc
   │        │  │  │  ├─ defaultfilters.cpython-311.pyc
   │        │  │  │  ├─ defaulttags.cpython-311.pyc
   │        │  │  │  ├─ engine.cpython-311.pyc
   │        │  │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  │  ├─ library.cpython-311.pyc
   │        │  │  │  ├─ loader.cpython-311.pyc
   │        │  │  │  ├─ loader_tags.cpython-311.pyc
   │        │  │  │  ├─ response.cpython-311.pyc
   │        │  │  │  ├─ smartif.cpython-311.pyc
   │        │  │  │  └─ utils.cpython-311.pyc
   │        │  │  ├─ autoreload.py
   │        │  │  ├─ backends
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  ├─ django.cpython-311.pyc
   │        │  │  │  │  ├─ dummy.cpython-311.pyc
   │        │  │  │  │  ├─ jinja2.cpython-311.pyc
   │        │  │  │  │  └─ utils.cpython-311.pyc
   │        │  │  │  ├─ base.py
   │        │  │  │  ├─ django.py
   │        │  │  │  ├─ dummy.py
   │        │  │  │  ├─ jinja2.py
   │        │  │  │  └─ utils.py
   │        │  │  ├─ base.py
   │        │  │  ├─ context.py
   │        │  │  ├─ context_processors.py
   │        │  │  ├─ defaultfilters.py
   │        │  │  ├─ defaulttags.py
   │        │  │  ├─ engine.py
   │        │  │  ├─ exceptions.py
   │        │  │  ├─ library.py
   │        │  │  ├─ loader.py
   │        │  │  ├─ loader_tags.py
   │        │  │  ├─ loaders
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ app_directories.cpython-311.pyc
   │        │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  ├─ cached.cpython-311.pyc
   │        │  │  │  │  ├─ filesystem.cpython-311.pyc
   │        │  │  │  │  └─ locmem.cpython-311.pyc
   │        │  │  │  ├─ app_directories.py
   │        │  │  │  ├─ base.py
   │        │  │  │  ├─ cached.py
   │        │  │  │  ├─ filesystem.py
   │        │  │  │  └─ locmem.py
   │        │  │  ├─ response.py
   │        │  │  ├─ smartif.py
   │        │  │  └─ utils.py
   │        │  ├─ templatetags
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ cache.cpython-311.pyc
   │        │  │  │  ├─ i18n.cpython-311.pyc
   │        │  │  │  ├─ l10n.cpython-311.pyc
   │        │  │  │  ├─ static.cpython-311.pyc
   │        │  │  │  └─ tz.cpython-311.pyc
   │        │  │  ├─ cache.py
   │        │  │  ├─ i18n.py
   │        │  │  ├─ l10n.py
   │        │  │  ├─ static.py
   │        │  │  └─ tz.py
   │        │  ├─ test
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ client.cpython-311.pyc
   │        │  │  │  ├─ html.cpython-311.pyc
   │        │  │  │  ├─ runner.cpython-311.pyc
   │        │  │  │  ├─ selenium.cpython-311.pyc
   │        │  │  │  ├─ signals.cpython-311.pyc
   │        │  │  │  ├─ testcases.cpython-311.pyc
   │        │  │  │  └─ utils.cpython-311.pyc
   │        │  │  ├─ client.py
   │        │  │  ├─ html.py
   │        │  │  ├─ runner.py
   │        │  │  ├─ selenium.py
   │        │  │  ├─ signals.py
   │        │  │  ├─ testcases.py
   │        │  │  └─ utils.py
   │        │  ├─ urls
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  ├─ conf.cpython-311.pyc
   │        │  │  │  ├─ converters.cpython-311.pyc
   │        │  │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  │  ├─ resolvers.cpython-311.pyc
   │        │  │  │  └─ utils.cpython-311.pyc
   │        │  │  ├─ base.py
   │        │  │  ├─ conf.py
   │        │  │  ├─ converters.py
   │        │  │  ├─ exceptions.py
   │        │  │  ├─ resolvers.py
   │        │  │  └─ utils.py
   │        │  ├─ utils
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _os.cpython-311.pyc
   │        │  │  │  ├─ archive.cpython-311.pyc
   │        │  │  │  ├─ asyncio.cpython-311.pyc
   │        │  │  │  ├─ autoreload.cpython-311.pyc
   │        │  │  │  ├─ cache.cpython-311.pyc
   │        │  │  │  ├─ choices.cpython-311.pyc
   │        │  │  │  ├─ connection.cpython-311.pyc
   │        │  │  │  ├─ crypto.cpython-311.pyc
   │        │  │  │  ├─ datastructures.cpython-311.pyc
   │        │  │  │  ├─ dateformat.cpython-311.pyc
   │        │  │  │  ├─ dateparse.cpython-311.pyc
   │        │  │  │  ├─ dates.cpython-311.pyc
   │        │  │  │  ├─ deconstruct.cpython-311.pyc
   │        │  │  │  ├─ decorators.cpython-311.pyc
   │        │  │  │  ├─ deprecation.cpython-311.pyc
   │        │  │  │  ├─ duration.cpython-311.pyc
   │        │  │  │  ├─ encoding.cpython-311.pyc
   │        │  │  │  ├─ feedgenerator.cpython-311.pyc
   │        │  │  │  ├─ formats.cpython-311.pyc
   │        │  │  │  ├─ functional.cpython-311.pyc
   │        │  │  │  ├─ hashable.cpython-311.pyc
   │        │  │  │  ├─ html.cpython-311.pyc
   │        │  │  │  ├─ http.cpython-311.pyc
   │        │  │  │  ├─ inspect.cpython-311.pyc
   │        │  │  │  ├─ ipv6.cpython-311.pyc
   │        │  │  │  ├─ itercompat.cpython-311.pyc
   │        │  │  │  ├─ log.cpython-311.pyc
   │        │  │  │  ├─ lorem_ipsum.cpython-311.pyc
   │        │  │  │  ├─ module_loading.cpython-311.pyc
   │        │  │  │  ├─ numberformat.cpython-311.pyc
   │        │  │  │  ├─ regex_helper.cpython-311.pyc
   │        │  │  │  ├─ safestring.cpython-311.pyc
   │        │  │  │  ├─ termcolors.cpython-311.pyc
   │        │  │  │  ├─ text.cpython-311.pyc
   │        │  │  │  ├─ timesince.cpython-311.pyc
   │        │  │  │  ├─ timezone.cpython-311.pyc
   │        │  │  │  ├─ tree.cpython-311.pyc
   │        │  │  │  ├─ version.cpython-311.pyc
   │        │  │  │  └─ xmlutils.cpython-311.pyc
   │        │  │  ├─ _os.py
   │        │  │  ├─ archive.py
   │        │  │  ├─ asyncio.py
   │        │  │  ├─ autoreload.py
   │        │  │  ├─ cache.py
   │        │  │  ├─ choices.py
   │        │  │  ├─ connection.py
   │        │  │  ├─ crypto.py
   │        │  │  ├─ datastructures.py
   │        │  │  ├─ dateformat.py
   │        │  │  ├─ dateparse.py
   │        │  │  ├─ dates.py
   │        │  │  ├─ deconstruct.py
   │        │  │  ├─ decorators.py
   │        │  │  ├─ deprecation.py
   │        │  │  ├─ duration.py
   │        │  │  ├─ encoding.py
   │        │  │  ├─ feedgenerator.py
   │        │  │  ├─ formats.py
   │        │  │  ├─ functional.py
   │        │  │  ├─ hashable.py
   │        │  │  ├─ html.py
   │        │  │  ├─ http.py
   │        │  │  ├─ inspect.py
   │        │  │  ├─ ipv6.py
   │        │  │  ├─ itercompat.py
   │        │  │  ├─ log.py
   │        │  │  ├─ lorem_ipsum.py
   │        │  │  ├─ module_loading.py
   │        │  │  ├─ numberformat.py
   │        │  │  ├─ regex_helper.py
   │        │  │  ├─ safestring.py
   │        │  │  ├─ termcolors.py
   │        │  │  ├─ text.py
   │        │  │  ├─ timesince.py
   │        │  │  ├─ timezone.py
   │        │  │  ├─ translation
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ reloader.cpython-311.pyc
   │        │  │  │  │  ├─ template.cpython-311.pyc
   │        │  │  │  │  ├─ trans_null.cpython-311.pyc
   │        │  │  │  │  └─ trans_real.cpython-311.pyc
   │        │  │  │  ├─ reloader.py
   │        │  │  │  ├─ template.py
   │        │  │  │  ├─ trans_null.py
   │        │  │  │  └─ trans_real.py
   │        │  │  ├─ tree.py
   │        │  │  ├─ version.py
   │        │  │  └─ xmlutils.py
   │        │  └─ views
   │        │     ├─ __init__.py
   │        │     ├─ __pycache__
   │        │     │  ├─ __init__.cpython-311.pyc
   │        │     │  ├─ csrf.cpython-311.pyc
   │        │     │  ├─ debug.cpython-311.pyc
   │        │     │  ├─ defaults.cpython-311.pyc
   │        │     │  ├─ i18n.cpython-311.pyc
   │        │     │  └─ static.cpython-311.pyc
   │        │     ├─ csrf.py
   │        │     ├─ debug.py
   │        │     ├─ decorators
   │        │     │  ├─ __init__.py
   │        │     │  ├─ __pycache__
   │        │     │  │  ├─ __init__.cpython-311.pyc
   │        │     │  │  ├─ cache.cpython-311.pyc
   │        │     │  │  ├─ clickjacking.cpython-311.pyc
   │        │     │  │  ├─ common.cpython-311.pyc
   │        │     │  │  ├─ csrf.cpython-311.pyc
   │        │     │  │  ├─ debug.cpython-311.pyc
   │        │     │  │  ├─ gzip.cpython-311.pyc
   │        │     │  │  ├─ http.cpython-311.pyc
   │        │     │  │  └─ vary.cpython-311.pyc
   │        │     │  ├─ cache.py
   │        │     │  ├─ clickjacking.py
   │        │     │  ├─ common.py
   │        │     │  ├─ csrf.py
   │        │     │  ├─ debug.py
   │        │     │  ├─ gzip.py
   │        │     │  ├─ http.py
   │        │     │  └─ vary.py
   │        │     ├─ defaults.py
   │        │     ├─ generic
   │        │     │  ├─ __init__.py
   │        │     │  ├─ __pycache__
   │        │     │  │  ├─ __init__.cpython-311.pyc
   │        │     │  │  ├─ base.cpython-311.pyc
   │        │     │  │  ├─ dates.cpython-311.pyc
   │        │     │  │  ├─ detail.cpython-311.pyc
   │        │     │  │  ├─ edit.cpython-311.pyc
   │        │     │  │  └─ list.cpython-311.pyc
   │        │     │  ├─ base.py
   │        │     │  ├─ dates.py
   │        │     │  ├─ detail.py
   │        │     │  ├─ edit.py
   │        │     │  └─ list.py
   │        │     ├─ i18n.py
   │        │     ├─ static.py
   │        │     └─ templates
   │        │        ├─ csrf_403.html
   │        │        ├─ default_urlconf.html
   │        │        ├─ directory_index.html
   │        │        ├─ i18n_catalog.js
   │        │        ├─ technical_404.html
   │        │        ├─ technical_500.html
   │        │        └─ technical_500.txt
   │        ├─ django-5.2.1.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  ├─ entry_points.txt
   │        │  ├─ licenses
   │        │  │  ├─ AUTHORS
   │        │  │  ├─ LICENSE
   │        │  │  └─ LICENSE.python
   │        │  └─ top_level.txt
   │        ├─ django_rest_framework-0.1.0.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  └─ top_level.txt
   │        ├─ djangorestframework-3.16.0.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ WHEEL
   │        │  ├─ licenses
   │        │  │  └─ LICENSE.md
   │        │  └─ top_level.txt
   │        ├─ empty
   │        │  ├─ __init__.py
   │        │  └─ __pycache__
   │        │     └─ __init__.cpython-311.pyc
   │        ├─ git
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ cmd.cpython-311.pyc
   │        │  │  ├─ compat.cpython-311.pyc
   │        │  │  ├─ config.cpython-311.pyc
   │        │  │  ├─ db.cpython-311.pyc
   │        │  │  ├─ diff.cpython-311.pyc
   │        │  │  ├─ exc.cpython-311.pyc
   │        │  │  ├─ remote.cpython-311.pyc
   │        │  │  ├─ types.cpython-311.pyc
   │        │  │  └─ util.cpython-311.pyc
   │        │  ├─ cmd.py
   │        │  ├─ compat.py
   │        │  ├─ config.py
   │        │  ├─ db.py
   │        │  ├─ diff.py
   │        │  ├─ exc.py
   │        │  ├─ index
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  ├─ fun.cpython-311.pyc
   │        │  │  │  ├─ typ.cpython-311.pyc
   │        │  │  │  └─ util.cpython-311.pyc
   │        │  │  ├─ base.py
   │        │  │  ├─ fun.py
   │        │  │  ├─ typ.py
   │        │  │  └─ util.py
   │        │  ├─ objects
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  ├─ blob.cpython-311.pyc
   │        │  │  │  ├─ commit.cpython-311.pyc
   │        │  │  │  ├─ fun.cpython-311.pyc
   │        │  │  │  ├─ tag.cpython-311.pyc
   │        │  │  │  ├─ tree.cpython-311.pyc
   │        │  │  │  └─ util.cpython-311.pyc
   │        │  │  ├─ base.py
   │        │  │  ├─ blob.py
   │        │  │  ├─ commit.py
   │        │  │  ├─ fun.py
   │        │  │  ├─ submodule
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  ├─ root.cpython-311.pyc
   │        │  │  │  │  └─ util.cpython-311.pyc
   │        │  │  │  ├─ base.py
   │        │  │  │  ├─ root.py
   │        │  │  │  └─ util.py
   │        │  │  ├─ tag.py
   │        │  │  ├─ tree.py
   │        │  │  └─ util.py
   │        │  ├─ py.typed
   │        │  ├─ refs
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ head.cpython-311.pyc
   │        │  │  │  ├─ log.cpython-311.pyc
   │        │  │  │  ├─ reference.cpython-311.pyc
   │        │  │  │  ├─ remote.cpython-311.pyc
   │        │  │  │  ├─ symbolic.cpython-311.pyc
   │        │  │  │  └─ tag.cpython-311.pyc
   │        │  │  ├─ head.py
   │        │  │  ├─ log.py
   │        │  │  ├─ reference.py
   │        │  │  ├─ remote.py
   │        │  │  ├─ symbolic.py
   │        │  │  └─ tag.py
   │        │  ├─ remote.py
   │        │  ├─ repo
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  └─ fun.cpython-311.pyc
   │        │  │  ├─ base.py
   │        │  │  └─ fun.py
   │        │  ├─ types.py
   │        │  └─ util.py
   │        ├─ gitdb
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ base.cpython-311.pyc
   │        │  │  ├─ const.cpython-311.pyc
   │        │  │  ├─ exc.cpython-311.pyc
   │        │  │  ├─ fun.cpython-311.pyc
   │        │  │  ├─ pack.cpython-311.pyc
   │        │  │  ├─ stream.cpython-311.pyc
   │        │  │  ├─ typ.cpython-311.pyc
   │        │  │  └─ util.cpython-311.pyc
   │        │  ├─ base.py
   │        │  ├─ const.py
   │        │  ├─ db
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  ├─ git.cpython-311.pyc
   │        │  │  │  ├─ loose.cpython-311.pyc
   │        │  │  │  ├─ mem.cpython-311.pyc
   │        │  │  │  ├─ pack.cpython-311.pyc
   │        │  │  │  └─ ref.cpython-311.pyc
   │        │  │  ├─ base.py
   │        │  │  ├─ git.py
   │        │  │  ├─ loose.py
   │        │  │  ├─ mem.py
   │        │  │  ├─ pack.py
   │        │  │  └─ ref.py
   │        │  ├─ exc.py
   │        │  ├─ fun.py
   │        │  ├─ pack.py
   │        │  ├─ stream.py
   │        │  ├─ test
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ lib.cpython-311.pyc
   │        │  │  │  ├─ test_base.cpython-311.pyc
   │        │  │  │  ├─ test_example.cpython-311.pyc
   │        │  │  │  ├─ test_pack.cpython-311.pyc
   │        │  │  │  ├─ test_stream.cpython-311.pyc
   │        │  │  │  └─ test_util.cpython-311.pyc
   │        │  │  ├─ lib.py
   │        │  │  ├─ test_base.py
   │        │  │  ├─ test_example.py
   │        │  │  ├─ test_pack.py
   │        │  │  ├─ test_stream.py
   │        │  │  └─ test_util.py
   │        │  ├─ typ.py
   │        │  ├─ util.py
   │        │  └─ utils
   │        │     ├─ __init__.py
   │        │     ├─ __pycache__
   │        │     │  ├─ __init__.cpython-311.pyc
   │        │     │  └─ encoding.cpython-311.pyc
   │        │     └─ encoding.py
   │        ├─ gitdb-4.0.12.dist-info
   │        │  ├─ AUTHORS
   │        │  ├─ INSTALLER
   │        │  ├─ LICENSE
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  └─ top_level.txt
   │        ├─ google
   │        │  ├─ _upb
   │        │  │  └─ _message.abi3.so
   │        │  └─ protobuf
   │        │     ├─ __init__.py
   │        │     ├─ __pycache__
   │        │     │  ├─ __init__.cpython-311.pyc
   │        │     │  ├─ any.cpython-311.pyc
   │        │     │  ├─ any_pb2.cpython-311.pyc
   │        │     │  ├─ api_pb2.cpython-311.pyc
   │        │     │  ├─ descriptor.cpython-311.pyc
   │        │     │  ├─ descriptor_database.cpython-311.pyc
   │        │     │  ├─ descriptor_pb2.cpython-311.pyc
   │        │     │  ├─ descriptor_pool.cpython-311.pyc
   │        │     │  ├─ duration.cpython-311.pyc
   │        │     │  ├─ duration_pb2.cpython-311.pyc
   │        │     │  ├─ empty_pb2.cpython-311.pyc
   │        │     │  ├─ field_mask_pb2.cpython-311.pyc
   │        │     │  ├─ json_format.cpython-311.pyc
   │        │     │  ├─ message.cpython-311.pyc
   │        │     │  ├─ message_factory.cpython-311.pyc
   │        │     │  ├─ proto.cpython-311.pyc
   │        │     │  ├─ proto_builder.cpython-311.pyc
   │        │     │  ├─ proto_json.cpython-311.pyc
   │        │     │  ├─ proto_text.cpython-311.pyc
   │        │     │  ├─ reflection.cpython-311.pyc
   │        │     │  ├─ runtime_version.cpython-311.pyc
   │        │     │  ├─ service_reflection.cpython-311.pyc
   │        │     │  ├─ source_context_pb2.cpython-311.pyc
   │        │     │  ├─ struct_pb2.cpython-311.pyc
   │        │     │  ├─ symbol_database.cpython-311.pyc
   │        │     │  ├─ text_encoding.cpython-311.pyc
   │        │     │  ├─ text_format.cpython-311.pyc
   │        │     │  ├─ timestamp.cpython-311.pyc
   │        │     │  ├─ timestamp_pb2.cpython-311.pyc
   │        │     │  ├─ type_pb2.cpython-311.pyc
   │        │     │  ├─ unknown_fields.cpython-311.pyc
   │        │     │  └─ wrappers_pb2.cpython-311.pyc
   │        │     ├─ any.py
   │        │     ├─ any_pb2.py
   │        │     ├─ api_pb2.py
   │        │     ├─ compiler
   │        │     │  ├─ __init__.py
   │        │     │  ├─ __pycache__
   │        │     │  │  ├─ __init__.cpython-311.pyc
   │        │     │  │  └─ plugin_pb2.cpython-311.pyc
   │        │     │  └─ plugin_pb2.py
   │        │     ├─ descriptor.py
   │        │     ├─ descriptor_database.py
   │        │     ├─ descriptor_pb2.py
   │        │     ├─ descriptor_pool.py
   │        │     ├─ duration.py
   │        │     ├─ duration_pb2.py
   │        │     ├─ empty_pb2.py
   │        │     ├─ field_mask_pb2.py
   │        │     ├─ internal
   │        │     │  ├─ __init__.py
   │        │     │  ├─ __pycache__
   │        │     │  │  ├─ __init__.cpython-311.pyc
   │        │     │  │  ├─ api_implementation.cpython-311.pyc
   │        │     │  │  ├─ builder.cpython-311.pyc
   │        │     │  │  ├─ containers.cpython-311.pyc
   │        │     │  │  ├─ decoder.cpython-311.pyc
   │        │     │  │  ├─ encoder.cpython-311.pyc
   │        │     │  │  ├─ enum_type_wrapper.cpython-311.pyc
   │        │     │  │  ├─ extension_dict.cpython-311.pyc
   │        │     │  │  ├─ field_mask.cpython-311.pyc
   │        │     │  │  ├─ message_listener.cpython-311.pyc
   │        │     │  │  ├─ python_edition_defaults.cpython-311.pyc
   │        │     │  │  ├─ python_message.cpython-311.pyc
   │        │     │  │  ├─ testing_refleaks.cpython-311.pyc
   │        │     │  │  ├─ type_checkers.cpython-311.pyc
   │        │     │  │  ├─ well_known_types.cpython-311.pyc
   │        │     │  │  └─ wire_format.cpython-311.pyc
   │        │     │  ├─ api_implementation.py
   │        │     │  ├─ builder.py
   │        │     │  ├─ containers.py
   │        │     │  ├─ decoder.py
   │        │     │  ├─ encoder.py
   │        │     │  ├─ enum_type_wrapper.py
   │        │     │  ├─ extension_dict.py
   │        │     │  ├─ field_mask.py
   │        │     │  ├─ message_listener.py
   │        │     │  ├─ python_edition_defaults.py
   │        │     │  ├─ python_message.py
   │        │     │  ├─ testing_refleaks.py
   │        │     │  ├─ type_checkers.py
   │        │     │  ├─ well_known_types.py
   │        │     │  └─ wire_format.py
   │        │     ├─ json_format.py
   │        │     ├─ message.py
   │        │     ├─ message_factory.py
   │        │     ├─ proto.py
   │        │     ├─ proto_builder.py
   │        │     ├─ proto_json.py
   │        │     ├─ proto_text.py
   │        │     ├─ pyext
   │        │     │  ├─ __init__.py
   │        │     │  ├─ __pycache__
   │        │     │  │  ├─ __init__.cpython-311.pyc
   │        │     │  │  └─ cpp_message.cpython-311.pyc
   │        │     │  └─ cpp_message.py
   │        │     ├─ reflection.py
   │        │     ├─ runtime_version.py
   │        │     ├─ service_reflection.py
   │        │     ├─ source_context_pb2.py
   │        │     ├─ struct_pb2.py
   │        │     ├─ symbol_database.py
   │        │     ├─ testdata
   │        │     │  ├─ __init__.py
   │        │     │  └─ __pycache__
   │        │     │     └─ __init__.cpython-311.pyc
   │        │     ├─ text_encoding.py
   │        │     ├─ text_format.py
   │        │     ├─ timestamp.py
   │        │     ├─ timestamp_pb2.py
   │        │     ├─ type_pb2.py
   │        │     ├─ unknown_fields.py
   │        │     ├─ util
   │        │     │  ├─ __init__.py
   │        │     │  └─ __pycache__
   │        │     │     └─ __init__.cpython-311.pyc
   │        │     └─ wrappers_pb2.py
   │        ├─ idna
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ codec.cpython-311.pyc
   │        │  │  ├─ compat.cpython-311.pyc
   │        │  │  ├─ core.cpython-311.pyc
   │        │  │  ├─ idnadata.cpython-311.pyc
   │        │  │  ├─ intranges.cpython-311.pyc
   │        │  │  ├─ package_data.cpython-311.pyc
   │        │  │  └─ uts46data.cpython-311.pyc
   │        │  ├─ codec.py
   │        │  ├─ compat.py
   │        │  ├─ core.py
   │        │  ├─ idnadata.py
   │        │  ├─ intranges.py
   │        │  ├─ package_data.py
   │        │  ├─ py.typed
   │        │  └─ uts46data.py
   │        ├─ idna-3.10.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ LICENSE.md
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  └─ WHEEL
   │        ├─ jinja2
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ _identifier.cpython-311.pyc
   │        │  │  ├─ async_utils.cpython-311.pyc
   │        │  │  ├─ bccache.cpython-311.pyc
   │        │  │  ├─ compiler.cpython-311.pyc
   │        │  │  ├─ constants.cpython-311.pyc
   │        │  │  ├─ debug.cpython-311.pyc
   │        │  │  ├─ defaults.cpython-311.pyc
   │        │  │  ├─ environment.cpython-311.pyc
   │        │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  ├─ ext.cpython-311.pyc
   │        │  │  ├─ filters.cpython-311.pyc
   │        │  │  ├─ idtracking.cpython-311.pyc
   │        │  │  ├─ lexer.cpython-311.pyc
   │        │  │  ├─ loaders.cpython-311.pyc
   │        │  │  ├─ meta.cpython-311.pyc
   │        │  │  ├─ nativetypes.cpython-311.pyc
   │        │  │  ├─ nodes.cpython-311.pyc
   │        │  │  ├─ optimizer.cpython-311.pyc
   │        │  │  ├─ parser.cpython-311.pyc
   │        │  │  ├─ runtime.cpython-311.pyc
   │        │  │  ├─ sandbox.cpython-311.pyc
   │        │  │  ├─ tests.cpython-311.pyc
   │        │  │  ├─ utils.cpython-311.pyc
   │        │  │  └─ visitor.cpython-311.pyc
   │        │  ├─ _identifier.py
   │        │  ├─ async_utils.py
   │        │  ├─ bccache.py
   │        │  ├─ compiler.py
   │        │  ├─ constants.py
   │        │  ├─ debug.py
   │        │  ├─ defaults.py
   │        │  ├─ environment.py
   │        │  ├─ exceptions.py
   │        │  ├─ ext.py
   │        │  ├─ filters.py
   │        │  ├─ idtracking.py
   │        │  ├─ lexer.py
   │        │  ├─ loaders.py
   │        │  ├─ meta.py
   │        │  ├─ nativetypes.py
   │        │  ├─ nodes.py
   │        │  ├─ optimizer.py
   │        │  ├─ parser.py
   │        │  ├─ py.typed
   │        │  ├─ runtime.py
   │        │  ├─ sandbox.py
   │        │  ├─ tests.py
   │        │  ├─ utils.py
   │        │  └─ visitor.py
   │        ├─ jinja2-3.1.6.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  ├─ entry_points.txt
   │        │  └─ licenses
   │        │     └─ LICENSE.txt
   │        ├─ jsonschema
   │        │  ├─ __init__.py
   │        │  ├─ __main__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ __main__.cpython-311.pyc
   │        │  │  ├─ _format.cpython-311.pyc
   │        │  │  ├─ _keywords.cpython-311.pyc
   │        │  │  ├─ _legacy_keywords.cpython-311.pyc
   │        │  │  ├─ _types.cpython-311.pyc
   │        │  │  ├─ _typing.cpython-311.pyc
   │        │  │  ├─ _utils.cpython-311.pyc
   │        │  │  ├─ cli.cpython-311.pyc
   │        │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  ├─ protocols.cpython-311.pyc
   │        │  │  └─ validators.cpython-311.pyc
   │        │  ├─ _format.py
   │        │  ├─ _keywords.py
   │        │  ├─ _legacy_keywords.py
   │        │  ├─ _types.py
   │        │  ├─ _typing.py
   │        │  ├─ _utils.py
   │        │  ├─ benchmarks
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ const_vs_enum.cpython-311.pyc
   │        │  │  │  ├─ contains.cpython-311.pyc
   │        │  │  │  ├─ issue232.cpython-311.pyc
   │        │  │  │  ├─ json_schema_test_suite.cpython-311.pyc
   │        │  │  │  ├─ nested_schemas.cpython-311.pyc
   │        │  │  │  ├─ subcomponents.cpython-311.pyc
   │        │  │  │  ├─ unused_registry.cpython-311.pyc
   │        │  │  │  ├─ useless_applicator_schemas.cpython-311.pyc
   │        │  │  │  ├─ useless_keywords.cpython-311.pyc
   │        │  │  │  └─ validator_creation.cpython-311.pyc
   │        │  │  ├─ const_vs_enum.py
   │        │  │  ├─ contains.py
   │        │  │  ├─ issue232
   │        │  │  │  └─ issue.json
   │        │  │  ├─ issue232.py
   │        │  │  ├─ json_schema_test_suite.py
   │        │  │  ├─ nested_schemas.py
   │        │  │  ├─ subcomponents.py
   │        │  │  ├─ unused_registry.py
   │        │  │  ├─ useless_applicator_schemas.py
   │        │  │  ├─ useless_keywords.py
   │        │  │  └─ validator_creation.py
   │        │  ├─ cli.py
   │        │  ├─ exceptions.py
   │        │  ├─ protocols.py
   │        │  ├─ tests
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _suite.cpython-311.pyc
   │        │  │  │  ├─ fuzz_validate.cpython-311.pyc
   │        │  │  │  ├─ test_cli.cpython-311.pyc
   │        │  │  │  ├─ test_deprecations.cpython-311.pyc
   │        │  │  │  ├─ test_exceptions.cpython-311.pyc
   │        │  │  │  ├─ test_format.cpython-311.pyc
   │        │  │  │  ├─ test_jsonschema_test_suite.cpython-311.pyc
   │        │  │  │  ├─ test_types.cpython-311.pyc
   │        │  │  │  ├─ test_utils.cpython-311.pyc
   │        │  │  │  └─ test_validators.cpython-311.pyc
   │        │  │  ├─ _suite.py
   │        │  │  ├─ fuzz_validate.py
   │        │  │  ├─ test_cli.py
   │        │  │  ├─ test_deprecations.py
   │        │  │  ├─ test_exceptions.py
   │        │  │  ├─ test_format.py
   │        │  │  ├─ test_jsonschema_test_suite.py
   │        │  │  ├─ test_types.py
   │        │  │  ├─ test_utils.py
   │        │  │  └─ test_validators.py
   │        │  └─ validators.py
   │        ├─ jsonschema-4.24.0.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  ├─ entry_points.txt
   │        │  └─ licenses
   │        │     └─ COPYING
   │        ├─ jsonschema_specifications
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  └─ _core.cpython-311.pyc
   │        │  ├─ _core.py
   │        │  ├─ schemas
   │        │  │  ├─ draft201909
   │        │  │  │  ├─ metaschema.json
   │        │  │  │  └─ vocabularies
   │        │  │  │     ├─ applicator
   │        │  │  │     ├─ content
   │        │  │  │     ├─ core
   │        │  │  │     ├─ meta-data
   │        │  │  │     └─ validation
   │        │  │  ├─ draft202012
   │        │  │  │  ├─ metaschema.json
   │        │  │  │  └─ vocabularies
   │        │  │  │     ├─ applicator
   │        │  │  │     ├─ content
   │        │  │  │     ├─ core
   │        │  │  │     ├─ format
   │        │  │  │     ├─ format-annotation
   │        │  │  │     ├─ format-assertion
   │        │  │  │     ├─ meta-data
   │        │  │  │     ├─ unevaluated
   │        │  │  │     └─ validation
   │        │  │  ├─ draft3
   │        │  │  │  └─ metaschema.json
   │        │  │  ├─ draft4
   │        │  │  │  └─ metaschema.json
   │        │  │  ├─ draft6
   │        │  │  │  └─ metaschema.json
   │        │  │  └─ draft7
   │        │  │     └─ metaschema.json
   │        │  └─ tests
   │        │     ├─ __init__.py
   │        │     ├─ __pycache__
   │        │     │  ├─ __init__.cpython-311.pyc
   │        │     │  └─ test_jsonschema_specifications.cpython-311.pyc
   │        │     └─ test_jsonschema_specifications.py
   │        ├─ jsonschema_specifications-2025.4.1.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  └─ licenses
   │        │     └─ COPYING
   │        ├─ kafka
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ client_async.cpython-311.pyc
   │        │  │  ├─ cluster.cpython-311.pyc
   │        │  │  ├─ codec.cpython-311.pyc
   │        │  │  ├─ conn.cpython-311.pyc
   │        │  │  ├─ errors.cpython-311.pyc
   │        │  │  ├─ future.cpython-311.pyc
   │        │  │  ├─ socks5_wrapper.cpython-311.pyc
   │        │  │  ├─ structs.cpython-311.pyc
   │        │  │  ├─ util.cpython-311.pyc
   │        │  │  └─ version.cpython-311.pyc
   │        │  ├─ admin
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ acl_resource.cpython-311.pyc
   │        │  │  │  ├─ client.cpython-311.pyc
   │        │  │  │  ├─ config_resource.cpython-311.pyc
   │        │  │  │  ├─ new_partitions.cpython-311.pyc
   │        │  │  │  └─ new_topic.cpython-311.pyc
   │        │  │  ├─ acl_resource.py
   │        │  │  ├─ client.py
   │        │  │  ├─ config_resource.py
   │        │  │  ├─ new_partitions.py
   │        │  │  └─ new_topic.py
   │        │  ├─ benchmarks
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ consumer_performance.cpython-311.pyc
   │        │  │  │  ├─ load_example.cpython-311.pyc
   │        │  │  │  ├─ producer_performance.cpython-311.pyc
   │        │  │  │  ├─ record_batch_compose.cpython-311.pyc
   │        │  │  │  ├─ record_batch_read.cpython-311.pyc
   │        │  │  │  └─ varint_speed.cpython-311.pyc
   │        │  │  ├─ consumer_performance.py
   │        │  │  ├─ load_example.py
   │        │  │  ├─ producer_performance.py
   │        │  │  ├─ record_batch_compose.py
   │        │  │  ├─ record_batch_read.py
   │        │  │  └─ varint_speed.py
   │        │  ├─ client_async.py
   │        │  ├─ cluster.py
   │        │  ├─ codec.py
   │        │  ├─ conn.py
   │        │  ├─ consumer
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ fetcher.cpython-311.pyc
   │        │  │  │  ├─ group.cpython-311.pyc
   │        │  │  │  └─ subscription_state.cpython-311.pyc
   │        │  │  ├─ fetcher.py
   │        │  │  ├─ group.py
   │        │  │  └─ subscription_state.py
   │        │  ├─ coordinator
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  ├─ consumer.cpython-311.pyc
   │        │  │  │  ├─ heartbeat.cpython-311.pyc
   │        │  │  │  └─ protocol.cpython-311.pyc
   │        │  │  ├─ assignors
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ abstract.cpython-311.pyc
   │        │  │  │  │  ├─ range.cpython-311.pyc
   │        │  │  │  │  └─ roundrobin.cpython-311.pyc
   │        │  │  │  ├─ abstract.py
   │        │  │  │  ├─ range.py
   │        │  │  │  ├─ roundrobin.py
   │        │  │  │  └─ sticky
   │        │  │  │     ├─ __init__.py
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │     │  ├─ partition_movements.cpython-311.pyc
   │        │  │  │     │  ├─ sorted_set.cpython-311.pyc
   │        │  │  │     │  └─ sticky_assignor.cpython-311.pyc
   │        │  │  │     ├─ partition_movements.py
   │        │  │  │     ├─ sorted_set.py
   │        │  │  │     └─ sticky_assignor.py
   │        │  │  ├─ base.py
   │        │  │  ├─ consumer.py
   │        │  │  ├─ heartbeat.py
   │        │  │  └─ protocol.py
   │        │  ├─ errors.py
   │        │  ├─ future.py
   │        │  ├─ metrics
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ compound_stat.cpython-311.pyc
   │        │  │  │  ├─ dict_reporter.cpython-311.pyc
   │        │  │  │  ├─ kafka_metric.cpython-311.pyc
   │        │  │  │  ├─ measurable.cpython-311.pyc
   │        │  │  │  ├─ measurable_stat.cpython-311.pyc
   │        │  │  │  ├─ metric_config.cpython-311.pyc
   │        │  │  │  ├─ metric_name.cpython-311.pyc
   │        │  │  │  ├─ metrics.cpython-311.pyc
   │        │  │  │  ├─ metrics_reporter.cpython-311.pyc
   │        │  │  │  ├─ quota.cpython-311.pyc
   │        │  │  │  └─ stat.cpython-311.pyc
   │        │  │  ├─ compound_stat.py
   │        │  │  ├─ dict_reporter.py
   │        │  │  ├─ kafka_metric.py
   │        │  │  ├─ measurable.py
   │        │  │  ├─ measurable_stat.py
   │        │  │  ├─ metric_config.py
   │        │  │  ├─ metric_name.py
   │        │  │  ├─ metrics.py
   │        │  │  ├─ metrics_reporter.py
   │        │  │  ├─ quota.py
   │        │  │  ├─ stat.py
   │        │  │  └─ stats
   │        │  │     ├─ __init__.py
   │        │  │     ├─ __pycache__
   │        │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │     │  ├─ avg.cpython-311.pyc
   │        │  │     │  ├─ count.cpython-311.pyc
   │        │  │     │  ├─ histogram.cpython-311.pyc
   │        │  │     │  ├─ max_stat.cpython-311.pyc
   │        │  │     │  ├─ min_stat.cpython-311.pyc
   │        │  │     │  ├─ percentile.cpython-311.pyc
   │        │  │     │  ├─ percentiles.cpython-311.pyc
   │        │  │     │  ├─ rate.cpython-311.pyc
   │        │  │     │  ├─ sampled_stat.cpython-311.pyc
   │        │  │     │  ├─ sensor.cpython-311.pyc
   │        │  │     │  └─ total.cpython-311.pyc
   │        │  │     ├─ avg.py
   │        │  │     ├─ count.py
   │        │  │     ├─ histogram.py
   │        │  │     ├─ max_stat.py
   │        │  │     ├─ min_stat.py
   │        │  │     ├─ percentile.py
   │        │  │     ├─ percentiles.py
   │        │  │     ├─ rate.py
   │        │  │     ├─ sampled_stat.py
   │        │  │     ├─ sensor.py
   │        │  │     └─ total.py
   │        │  ├─ partitioner
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  └─ default.cpython-311.pyc
   │        │  │  └─ default.py
   │        │  ├─ producer
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ future.cpython-311.pyc
   │        │  │  │  ├─ kafka.cpython-311.pyc
   │        │  │  │  ├─ record_accumulator.cpython-311.pyc
   │        │  │  │  ├─ sender.cpython-311.pyc
   │        │  │  │  └─ transaction_manager.cpython-311.pyc
   │        │  │  ├─ future.py
   │        │  │  ├─ kafka.py
   │        │  │  ├─ record_accumulator.py
   │        │  │  ├─ sender.py
   │        │  │  └─ transaction_manager.py
   │        │  ├─ protocol
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ abstract.cpython-311.pyc
   │        │  │  │  ├─ add_offsets_to_txn.cpython-311.pyc
   │        │  │  │  ├─ add_partitions_to_txn.cpython-311.pyc
   │        │  │  │  ├─ admin.cpython-311.pyc
   │        │  │  │  ├─ api.cpython-311.pyc
   │        │  │  │  ├─ api_versions.cpython-311.pyc
   │        │  │  │  ├─ broker_api_versions.cpython-311.pyc
   │        │  │  │  ├─ commit.cpython-311.pyc
   │        │  │  │  ├─ end_txn.cpython-311.pyc
   │        │  │  │  ├─ fetch.cpython-311.pyc
   │        │  │  │  ├─ find_coordinator.cpython-311.pyc
   │        │  │  │  ├─ frame.cpython-311.pyc
   │        │  │  │  ├─ group.cpython-311.pyc
   │        │  │  │  ├─ init_producer_id.cpython-311.pyc
   │        │  │  │  ├─ list_offsets.cpython-311.pyc
   │        │  │  │  ├─ message.cpython-311.pyc
   │        │  │  │  ├─ metadata.cpython-311.pyc
   │        │  │  │  ├─ offset_for_leader_epoch.cpython-311.pyc
   │        │  │  │  ├─ parser.cpython-311.pyc
   │        │  │  │  ├─ pickle.cpython-311.pyc
   │        │  │  │  ├─ produce.cpython-311.pyc
   │        │  │  │  ├─ sasl_authenticate.cpython-311.pyc
   │        │  │  │  ├─ sasl_handshake.cpython-311.pyc
   │        │  │  │  ├─ struct.cpython-311.pyc
   │        │  │  │  ├─ txn_offset_commit.cpython-311.pyc
   │        │  │  │  └─ types.cpython-311.pyc
   │        │  │  ├─ abstract.py
   │        │  │  ├─ add_offsets_to_txn.py
   │        │  │  ├─ add_partitions_to_txn.py
   │        │  │  ├─ admin.py
   │        │  │  ├─ api.py
   │        │  │  ├─ api_versions.py
   │        │  │  ├─ broker_api_versions.py
   │        │  │  ├─ commit.py
   │        │  │  ├─ end_txn.py
   │        │  │  ├─ fetch.py
   │        │  │  ├─ find_coordinator.py
   │        │  │  ├─ frame.py
   │        │  │  ├─ group.py
   │        │  │  ├─ init_producer_id.py
   │        │  │  ├─ list_offsets.py
   │        │  │  ├─ message.py
   │        │  │  ├─ metadata.py
   │        │  │  ├─ offset_for_leader_epoch.py
   │        │  │  ├─ parser.py
   │        │  │  ├─ pickle.py
   │        │  │  ├─ produce.py
   │        │  │  ├─ sasl_authenticate.py
   │        │  │  ├─ sasl_handshake.py
   │        │  │  ├─ struct.py
   │        │  │  ├─ txn_offset_commit.py
   │        │  │  └─ types.py
   │        │  ├─ record
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _crc32c.cpython-311.pyc
   │        │  │  │  ├─ abc.cpython-311.pyc
   │        │  │  │  ├─ default_records.cpython-311.pyc
   │        │  │  │  ├─ legacy_records.cpython-311.pyc
   │        │  │  │  ├─ memory_records.cpython-311.pyc
   │        │  │  │  └─ util.cpython-311.pyc
   │        │  │  ├─ _crc32c.py
   │        │  │  ├─ abc.py
   │        │  │  ├─ default_records.py
   │        │  │  ├─ legacy_records.py
   │        │  │  ├─ memory_records.py
   │        │  │  └─ util.py
   │        │  ├─ sasl
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ abc.cpython-311.pyc
   │        │  │  │  ├─ gssapi.cpython-311.pyc
   │        │  │  │  ├─ msk.cpython-311.pyc
   │        │  │  │  ├─ oauth.cpython-311.pyc
   │        │  │  │  ├─ plain.cpython-311.pyc
   │        │  │  │  ├─ scram.cpython-311.pyc
   │        │  │  │  └─ sspi.cpython-311.pyc
   │        │  │  ├─ abc.py
   │        │  │  ├─ gssapi.py
   │        │  │  ├─ msk.py
   │        │  │  ├─ oauth.py
   │        │  │  ├─ plain.py
   │        │  │  ├─ scram.py
   │        │  │  └─ sspi.py
   │        │  ├─ serializer
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  └─ abstract.cpython-311.pyc
   │        │  │  └─ abstract.py
   │        │  ├─ socks5_wrapper.py
   │        │  ├─ structs.py
   │        │  ├─ util.py
   │        │  ├─ vendor
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ enum34.cpython-311.pyc
   │        │  │  │  ├─ selectors34.cpython-311.pyc
   │        │  │  │  ├─ six.cpython-311.pyc
   │        │  │  │  └─ socketpair.cpython-311.pyc
   │        │  │  ├─ enum34.py
   │        │  │  ├─ selectors34.py
   │        │  │  ├─ six.py
   │        │  │  └─ socketpair.py
   │        │  └─ version.py
   │        ├─ kafka_python-2.2.10.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  └─ top_level.txt
   │        ├─ markupsafe
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  └─ _native.cpython-311.pyc
   │        │  ├─ _native.py
   │        │  ├─ _speedups.c
   │        │  ├─ _speedups.cpython-311-darwin.so
   │        │  ├─ _speedups.pyi
   │        │  └─ py.typed
   │        ├─ narwhals
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ _duration.cpython-311.pyc
   │        │  │  ├─ _enum.cpython-311.pyc
   │        │  │  ├─ _expression_parsing.cpython-311.pyc
   │        │  │  ├─ _namespace.cpython-311.pyc
   │        │  │  ├─ _translate.cpython-311.pyc
   │        │  │  ├─ _typing_compat.cpython-311.pyc
   │        │  │  ├─ dataframe.cpython-311.pyc
   │        │  │  ├─ dependencies.cpython-311.pyc
   │        │  │  ├─ dtypes.cpython-311.pyc
   │        │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  ├─ expr.cpython-311.pyc
   │        │  │  ├─ expr_cat.cpython-311.pyc
   │        │  │  ├─ expr_dt.cpython-311.pyc
   │        │  │  ├─ expr_list.cpython-311.pyc
   │        │  │  ├─ expr_name.cpython-311.pyc
   │        │  │  ├─ expr_str.cpython-311.pyc
   │        │  │  ├─ expr_struct.cpython-311.pyc
   │        │  │  ├─ functions.cpython-311.pyc
   │        │  │  ├─ group_by.cpython-311.pyc
   │        │  │  ├─ schema.cpython-311.pyc
   │        │  │  ├─ selectors.cpython-311.pyc
   │        │  │  ├─ series.cpython-311.pyc
   │        │  │  ├─ series_cat.cpython-311.pyc
   │        │  │  ├─ series_dt.cpython-311.pyc
   │        │  │  ├─ series_list.cpython-311.pyc
   │        │  │  ├─ series_str.cpython-311.pyc
   │        │  │  ├─ series_struct.cpython-311.pyc
   │        │  │  ├─ this.cpython-311.pyc
   │        │  │  ├─ translate.cpython-311.pyc
   │        │  │  ├─ typing.cpython-311.pyc
   │        │  │  └─ utils.cpython-311.pyc
   │        │  ├─ _arrow
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ dataframe.cpython-311.pyc
   │        │  │  │  ├─ expr.cpython-311.pyc
   │        │  │  │  ├─ group_by.cpython-311.pyc
   │        │  │  │  ├─ namespace.cpython-311.pyc
   │        │  │  │  ├─ selectors.cpython-311.pyc
   │        │  │  │  ├─ series.cpython-311.pyc
   │        │  │  │  ├─ series_cat.cpython-311.pyc
   │        │  │  │  ├─ series_dt.cpython-311.pyc
   │        │  │  │  ├─ series_list.cpython-311.pyc
   │        │  │  │  ├─ series_str.cpython-311.pyc
   │        │  │  │  ├─ series_struct.cpython-311.pyc
   │        │  │  │  ├─ typing.cpython-311.pyc
   │        │  │  │  └─ utils.cpython-311.pyc
   │        │  │  ├─ dataframe.py
   │        │  │  ├─ expr.py
   │        │  │  ├─ group_by.py
   │        │  │  ├─ namespace.py
   │        │  │  ├─ selectors.py
   │        │  │  ├─ series.py
   │        │  │  ├─ series_cat.py
   │        │  │  ├─ series_dt.py
   │        │  │  ├─ series_list.py
   │        │  │  ├─ series_str.py
   │        │  │  ├─ series_struct.py
   │        │  │  ├─ typing.py
   │        │  │  └─ utils.py
   │        │  ├─ _compliant
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ any_namespace.cpython-311.pyc
   │        │  │  │  ├─ dataframe.cpython-311.pyc
   │        │  │  │  ├─ expr.cpython-311.pyc
   │        │  │  │  ├─ group_by.cpython-311.pyc
   │        │  │  │  ├─ namespace.cpython-311.pyc
   │        │  │  │  ├─ selectors.cpython-311.pyc
   │        │  │  │  ├─ series.cpython-311.pyc
   │        │  │  │  ├─ typing.cpython-311.pyc
   │        │  │  │  ├─ when_then.cpython-311.pyc
   │        │  │  │  └─ window.cpython-311.pyc
   │        │  │  ├─ any_namespace.py
   │        │  │  ├─ dataframe.py
   │        │  │  ├─ expr.py
   │        │  │  ├─ group_by.py
   │        │  │  ├─ namespace.py
   │        │  │  ├─ selectors.py
   │        │  │  ├─ series.py
   │        │  │  ├─ typing.py
   │        │  │  ├─ when_then.py
   │        │  │  └─ window.py
   │        │  ├─ _dask
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ dataframe.cpython-311.pyc
   │        │  │  │  ├─ expr.cpython-311.pyc
   │        │  │  │  ├─ expr_dt.cpython-311.pyc
   │        │  │  │  ├─ expr_str.cpython-311.pyc
   │        │  │  │  ├─ group_by.cpython-311.pyc
   │        │  │  │  ├─ namespace.cpython-311.pyc
   │        │  │  │  ├─ selectors.cpython-311.pyc
   │        │  │  │  └─ utils.cpython-311.pyc
   │        │  │  ├─ dataframe.py
   │        │  │  ├─ expr.py
   │        │  │  ├─ expr_dt.py
   │        │  │  ├─ expr_str.py
   │        │  │  ├─ group_by.py
   │        │  │  ├─ namespace.py
   │        │  │  ├─ selectors.py
   │        │  │  └─ utils.py
   │        │  ├─ _duckdb
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ dataframe.cpython-311.pyc
   │        │  │  │  ├─ expr.cpython-311.pyc
   │        │  │  │  ├─ expr_dt.cpython-311.pyc
   │        │  │  │  ├─ expr_list.cpython-311.pyc
   │        │  │  │  ├─ expr_str.cpython-311.pyc
   │        │  │  │  ├─ expr_struct.cpython-311.pyc
   │        │  │  │  ├─ group_by.cpython-311.pyc
   │        │  │  │  ├─ namespace.cpython-311.pyc
   │        │  │  │  ├─ selectors.cpython-311.pyc
   │        │  │  │  ├─ series.cpython-311.pyc
   │        │  │  │  └─ utils.cpython-311.pyc
   │        │  │  ├─ dataframe.py
   │        │  │  ├─ expr.py
   │        │  │  ├─ expr_dt.py
   │        │  │  ├─ expr_list.py
   │        │  │  ├─ expr_str.py
   │        │  │  ├─ expr_struct.py
   │        │  │  ├─ group_by.py
   │        │  │  ├─ namespace.py
   │        │  │  ├─ selectors.py
   │        │  │  ├─ series.py
   │        │  │  └─ utils.py
   │        │  ├─ _duration.py
   │        │  ├─ _enum.py
   │        │  ├─ _expression_parsing.py
   │        │  ├─ _ibis
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ dataframe.cpython-311.pyc
   │        │  │  │  ├─ expr.cpython-311.pyc
   │        │  │  │  ├─ expr_dt.cpython-311.pyc
   │        │  │  │  ├─ expr_list.cpython-311.pyc
   │        │  │  │  ├─ expr_str.cpython-311.pyc
   │        │  │  │  ├─ expr_struct.cpython-311.pyc
   │        │  │  │  ├─ group_by.cpython-311.pyc
   │        │  │  │  ├─ namespace.cpython-311.pyc
   │        │  │  │  ├─ selectors.cpython-311.pyc
   │        │  │  │  ├─ series.cpython-311.pyc
   │        │  │  │  └─ utils.cpython-311.pyc
   │        │  │  ├─ dataframe.py
   │        │  │  ├─ expr.py
   │        │  │  ├─ expr_dt.py
   │        │  │  ├─ expr_list.py
   │        │  │  ├─ expr_str.py
   │        │  │  ├─ expr_struct.py
   │        │  │  ├─ group_by.py
   │        │  │  ├─ namespace.py
   │        │  │  ├─ selectors.py
   │        │  │  ├─ series.py
   │        │  │  └─ utils.py
   │        │  ├─ _interchange
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ dataframe.cpython-311.pyc
   │        │  │  │  └─ series.cpython-311.pyc
   │        │  │  ├─ dataframe.py
   │        │  │  └─ series.py
   │        │  ├─ _namespace.py
   │        │  ├─ _pandas_like
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ dataframe.cpython-311.pyc
   │        │  │  │  ├─ expr.cpython-311.pyc
   │        │  │  │  ├─ group_by.cpython-311.pyc
   │        │  │  │  ├─ namespace.cpython-311.pyc
   │        │  │  │  ├─ selectors.cpython-311.pyc
   │        │  │  │  ├─ series.cpython-311.pyc
   │        │  │  │  ├─ series_cat.cpython-311.pyc
   │        │  │  │  ├─ series_dt.cpython-311.pyc
   │        │  │  │  ├─ series_list.cpython-311.pyc
   │        │  │  │  ├─ series_str.cpython-311.pyc
   │        │  │  │  ├─ series_struct.cpython-311.pyc
   │        │  │  │  ├─ typing.cpython-311.pyc
   │        │  │  │  └─ utils.cpython-311.pyc
   │        │  │  ├─ dataframe.py
   │        │  │  ├─ expr.py
   │        │  │  ├─ group_by.py
   │        │  │  ├─ namespace.py
   │        │  │  ├─ selectors.py
   │        │  │  ├─ series.py
   │        │  │  ├─ series_cat.py
   │        │  │  ├─ series_dt.py
   │        │  │  ├─ series_list.py
   │        │  │  ├─ series_str.py
   │        │  │  ├─ series_struct.py
   │        │  │  ├─ typing.py
   │        │  │  └─ utils.py
   │        │  ├─ _polars
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ dataframe.cpython-311.pyc
   │        │  │  │  ├─ expr.cpython-311.pyc
   │        │  │  │  ├─ group_by.cpython-311.pyc
   │        │  │  │  ├─ namespace.cpython-311.pyc
   │        │  │  │  ├─ series.cpython-311.pyc
   │        │  │  │  ├─ typing.cpython-311.pyc
   │        │  │  │  └─ utils.cpython-311.pyc
   │        │  │  ├─ dataframe.py
   │        │  │  ├─ expr.py
   │        │  │  ├─ group_by.py
   │        │  │  ├─ namespace.py
   │        │  │  ├─ series.py
   │        │  │  ├─ typing.py
   │        │  │  └─ utils.py
   │        │  ├─ _spark_like
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ dataframe.cpython-311.pyc
   │        │  │  │  ├─ expr.cpython-311.pyc
   │        │  │  │  ├─ expr_dt.cpython-311.pyc
   │        │  │  │  ├─ expr_list.cpython-311.pyc
   │        │  │  │  ├─ expr_str.cpython-311.pyc
   │        │  │  │  ├─ expr_struct.cpython-311.pyc
   │        │  │  │  ├─ group_by.cpython-311.pyc
   │        │  │  │  ├─ namespace.cpython-311.pyc
   │        │  │  │  ├─ selectors.cpython-311.pyc
   │        │  │  │  └─ utils.cpython-311.pyc
   │        │  │  ├─ dataframe.py
   │        │  │  ├─ expr.py
   │        │  │  ├─ expr_dt.py
   │        │  │  ├─ expr_list.py
   │        │  │  ├─ expr_str.py
   │        │  │  ├─ expr_struct.py
   │        │  │  ├─ group_by.py
   │        │  │  ├─ namespace.py
   │        │  │  ├─ selectors.py
   │        │  │  └─ utils.py
   │        │  ├─ _translate.py
   │        │  ├─ _typing_compat.py
   │        │  ├─ dataframe.py
   │        │  ├─ dependencies.py
   │        │  ├─ dtypes.py
   │        │  ├─ exceptions.py
   │        │  ├─ expr.py
   │        │  ├─ expr_cat.py
   │        │  ├─ expr_dt.py
   │        │  ├─ expr_list.py
   │        │  ├─ expr_name.py
   │        │  ├─ expr_str.py
   │        │  ├─ expr_struct.py
   │        │  ├─ functions.py
   │        │  ├─ group_by.py
   │        │  ├─ py.typed
   │        │  ├─ schema.py
   │        │  ├─ selectors.py
   │        │  ├─ series.py
   │        │  ├─ series_cat.py
   │        │  ├─ series_dt.py
   │        │  ├─ series_list.py
   │        │  ├─ series_str.py
   │        │  ├─ series_struct.py
   │        │  ├─ stable
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  └─ v1
   │        │  │     ├─ __init__.py
   │        │  │     ├─ __pycache__
   │        │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │     │  ├─ _dtypes.cpython-311.pyc
   │        │  │     │  ├─ _namespace.cpython-311.pyc
   │        │  │     │  ├─ dependencies.cpython-311.pyc
   │        │  │     │  ├─ dtypes.cpython-311.pyc
   │        │  │     │  ├─ selectors.cpython-311.pyc
   │        │  │     │  └─ typing.cpython-311.pyc
   │        │  │     ├─ _dtypes.py
   │        │  │     ├─ _namespace.py
   │        │  │     ├─ dependencies.py
   │        │  │     ├─ dtypes.py
   │        │  │     ├─ selectors.py
   │        │  │     └─ typing.py
   │        │  ├─ this.py
   │        │  ├─ translate.py
   │        │  ├─ typing.py
   │        │  └─ utils.py
   │        ├─ narwhals-1.41.0.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  └─ licenses
   │        │     └─ LICENSE.md
   │        ├─ numpy
   │        │  ├─ __config__.py
   │        │  ├─ __config__.pyi
   │        │  ├─ __init__.cython-30.pxd
   │        │  ├─ __init__.pxd
   │        │  ├─ __init__.py
   │        │  ├─ __init__.pyi
   │        │  ├─ __pycache__
   │        │  │  ├─ __config__.cpython-311.pyc
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ _array_api_info.cpython-311.pyc
   │        │  │  ├─ _configtool.cpython-311.pyc
   │        │  │  ├─ _distributor_init.cpython-311.pyc
   │        │  │  ├─ _expired_attrs_2_0.cpython-311.pyc
   │        │  │  ├─ _globals.cpython-311.pyc
   │        │  │  ├─ _pytesttester.cpython-311.pyc
   │        │  │  ├─ conftest.cpython-311.pyc
   │        │  │  ├─ ctypeslib.cpython-311.pyc
   │        │  │  ├─ dtypes.cpython-311.pyc
   │        │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  ├─ matlib.cpython-311.pyc
   │        │  │  └─ version.cpython-311.pyc
   │        │  ├─ _array_api_info.py
   │        │  ├─ _array_api_info.pyi
   │        │  ├─ _configtool.py
   │        │  ├─ _configtool.pyi
   │        │  ├─ _core
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.pyi
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _add_newdocs.cpython-311.pyc
   │        │  │  │  ├─ _add_newdocs_scalars.cpython-311.pyc
   │        │  │  │  ├─ _asarray.cpython-311.pyc
   │        │  │  │  ├─ _dtype.cpython-311.pyc
   │        │  │  │  ├─ _dtype_ctypes.cpython-311.pyc
   │        │  │  │  ├─ _exceptions.cpython-311.pyc
   │        │  │  │  ├─ _internal.cpython-311.pyc
   │        │  │  │  ├─ _machar.cpython-311.pyc
   │        │  │  │  ├─ _methods.cpython-311.pyc
   │        │  │  │  ├─ _string_helpers.cpython-311.pyc
   │        │  │  │  ├─ _type_aliases.cpython-311.pyc
   │        │  │  │  ├─ _ufunc_config.cpython-311.pyc
   │        │  │  │  ├─ arrayprint.cpython-311.pyc
   │        │  │  │  ├─ cversions.cpython-311.pyc
   │        │  │  │  ├─ defchararray.cpython-311.pyc
   │        │  │  │  ├─ einsumfunc.cpython-311.pyc
   │        │  │  │  ├─ fromnumeric.cpython-311.pyc
   │        │  │  │  ├─ function_base.cpython-311.pyc
   │        │  │  │  ├─ getlimits.cpython-311.pyc
   │        │  │  │  ├─ memmap.cpython-311.pyc
   │        │  │  │  ├─ multiarray.cpython-311.pyc
   │        │  │  │  ├─ numeric.cpython-311.pyc
   │        │  │  │  ├─ numerictypes.cpython-311.pyc
   │        │  │  │  ├─ overrides.cpython-311.pyc
   │        │  │  │  ├─ printoptions.cpython-311.pyc
   │        │  │  │  ├─ records.cpython-311.pyc
   │        │  │  │  ├─ shape_base.cpython-311.pyc
   │        │  │  │  ├─ strings.cpython-311.pyc
   │        │  │  │  └─ umath.cpython-311.pyc
   │        │  │  ├─ _add_newdocs.py
   │        │  │  ├─ _add_newdocs.pyi
   │        │  │  ├─ _add_newdocs_scalars.py
   │        │  │  ├─ _add_newdocs_scalars.pyi
   │        │  │  ├─ _asarray.py
   │        │  │  ├─ _asarray.pyi
   │        │  │  ├─ _dtype.py
   │        │  │  ├─ _dtype.pyi
   │        │  │  ├─ _dtype_ctypes.py
   │        │  │  ├─ _dtype_ctypes.pyi
   │        │  │  ├─ _exceptions.py
   │        │  │  ├─ _exceptions.pyi
   │        │  │  ├─ _internal.py
   │        │  │  ├─ _internal.pyi
   │        │  │  ├─ _machar.py
   │        │  │  ├─ _machar.pyi
   │        │  │  ├─ _methods.py
   │        │  │  ├─ _methods.pyi
   │        │  │  ├─ _multiarray_tests.cpython-311-darwin.so
   │        │  │  ├─ _multiarray_umath.cpython-311-darwin.so
   │        │  │  ├─ _operand_flag_tests.cpython-311-darwin.so
   │        │  │  ├─ _rational_tests.cpython-311-darwin.so
   │        │  │  ├─ _simd.cpython-311-darwin.so
   │        │  │  ├─ _simd.pyi
   │        │  │  ├─ _string_helpers.py
   │        │  │  ├─ _string_helpers.pyi
   │        │  │  ├─ _struct_ufunc_tests.cpython-311-darwin.so
   │        │  │  ├─ _type_aliases.py
   │        │  │  ├─ _type_aliases.pyi
   │        │  │  ├─ _ufunc_config.py
   │        │  │  ├─ _ufunc_config.pyi
   │        │  │  ├─ _umath_tests.cpython-311-darwin.so
   │        │  │  ├─ arrayprint.py
   │        │  │  ├─ arrayprint.pyi
   │        │  │  ├─ cversions.py
   │        │  │  ├─ defchararray.py
   │        │  │  ├─ defchararray.pyi
   │        │  │  ├─ einsumfunc.py
   │        │  │  ├─ einsumfunc.pyi
   │        │  │  ├─ fromnumeric.py
   │        │  │  ├─ fromnumeric.pyi
   │        │  │  ├─ function_base.py
   │        │  │  ├─ function_base.pyi
   │        │  │  ├─ getlimits.py
   │        │  │  ├─ getlimits.pyi
   │        │  │  ├─ include
   │        │  │  │  └─ numpy
   │        │  │  │     ├─ __multiarray_api.c
   │        │  │  │     ├─ __multiarray_api.h
   │        │  │  │     ├─ __ufunc_api.c
   │        │  │  │     ├─ __ufunc_api.h
   │        │  │  │     ├─ _neighborhood_iterator_imp.h
   │        │  │  │     ├─ _numpyconfig.h
   │        │  │  │     ├─ _public_dtype_api_table.h
   │        │  │  │     ├─ arrayobject.h
   │        │  │  │     ├─ arrayscalars.h
   │        │  │  │     ├─ dtype_api.h
   │        │  │  │     ├─ halffloat.h
   │        │  │  │     ├─ ndarrayobject.h
   │        │  │  │     ├─ ndarraytypes.h
   │        │  │  │     ├─ npy_1_7_deprecated_api.h
   │        │  │  │     ├─ npy_2_compat.h
   │        │  │  │     ├─ npy_2_complexcompat.h
   │        │  │  │     ├─ npy_3kcompat.h
   │        │  │  │     ├─ npy_common.h
   │        │  │  │     ├─ npy_cpu.h
   │        │  │  │     ├─ npy_endian.h
   │        │  │  │     ├─ npy_math.h
   │        │  │  │     ├─ npy_no_deprecated_api.h
   │        │  │  │     ├─ npy_os.h
   │        │  │  │     ├─ numpyconfig.h
   │        │  │  │     ├─ random
   │        │  │  │     │  ├─ LICENSE.txt
   │        │  │  │     │  ├─ bitgen.h
   │        │  │  │     │  ├─ distributions.h
   │        │  │  │     │  └─ libdivide.h
   │        │  │  │     ├─ ufuncobject.h
   │        │  │  │     └─ utils.h
   │        │  │  ├─ lib
   │        │  │  │  ├─ libnpymath.a
   │        │  │  │  ├─ npy-pkg-config
   │        │  │  │  │  ├─ mlib.ini
   │        │  │  │  │  └─ npymath.ini
   │        │  │  │  └─ pkgconfig
   │        │  │  │     └─ numpy.pc
   │        │  │  ├─ memmap.py
   │        │  │  ├─ memmap.pyi
   │        │  │  ├─ multiarray.py
   │        │  │  ├─ multiarray.pyi
   │        │  │  ├─ numeric.py
   │        │  │  ├─ numeric.pyi
   │        │  │  ├─ numerictypes.py
   │        │  │  ├─ numerictypes.pyi
   │        │  │  ├─ overrides.py
   │        │  │  ├─ overrides.pyi
   │        │  │  ├─ printoptions.py
   │        │  │  ├─ printoptions.pyi
   │        │  │  ├─ records.py
   │        │  │  ├─ records.pyi
   │        │  │  ├─ shape_base.py
   │        │  │  ├─ shape_base.pyi
   │        │  │  ├─ strings.py
   │        │  │  ├─ strings.pyi
   │        │  │  ├─ tests
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ _locales.cpython-311.pyc
   │        │  │  │  │  ├─ _natype.cpython-311.pyc
   │        │  │  │  │  ├─ test__exceptions.cpython-311.pyc
   │        │  │  │  │  ├─ test_abc.cpython-311.pyc
   │        │  │  │  │  ├─ test_api.cpython-311.pyc
   │        │  │  │  │  ├─ test_argparse.cpython-311.pyc
   │        │  │  │  │  ├─ test_array_api_info.cpython-311.pyc
   │        │  │  │  │  ├─ test_array_coercion.cpython-311.pyc
   │        │  │  │  │  ├─ test_array_interface.cpython-311.pyc
   │        │  │  │  │  ├─ test_arraymethod.cpython-311.pyc
   │        │  │  │  │  ├─ test_arrayobject.cpython-311.pyc
   │        │  │  │  │  ├─ test_arrayprint.cpython-311.pyc
   │        │  │  │  │  ├─ test_casting_floatingpoint_errors.cpython-311.pyc
   │        │  │  │  │  ├─ test_casting_unittests.cpython-311.pyc
   │        │  │  │  │  ├─ test_conversion_utils.cpython-311.pyc
   │        │  │  │  │  ├─ test_cpu_dispatcher.cpython-311.pyc
   │        │  │  │  │  ├─ test_cpu_features.cpython-311.pyc
   │        │  │  │  │  ├─ test_custom_dtypes.cpython-311.pyc
   │        │  │  │  │  ├─ test_cython.cpython-311.pyc
   │        │  │  │  │  ├─ test_datetime.cpython-311.pyc
   │        │  │  │  │  ├─ test_defchararray.cpython-311.pyc
   │        │  │  │  │  ├─ test_deprecations.cpython-311.pyc
   │        │  │  │  │  ├─ test_dlpack.cpython-311.pyc
   │        │  │  │  │  ├─ test_dtype.cpython-311.pyc
   │        │  │  │  │  ├─ test_einsum.cpython-311.pyc
   │        │  │  │  │  ├─ test_errstate.cpython-311.pyc
   │        │  │  │  │  ├─ test_extint128.cpython-311.pyc
   │        │  │  │  │  ├─ test_function_base.cpython-311.pyc
   │        │  │  │  │  ├─ test_getlimits.cpython-311.pyc
   │        │  │  │  │  ├─ test_half.cpython-311.pyc
   │        │  │  │  │  ├─ test_hashtable.cpython-311.pyc
   │        │  │  │  │  ├─ test_indexerrors.cpython-311.pyc
   │        │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  ├─ test_item_selection.cpython-311.pyc
   │        │  │  │  │  ├─ test_limited_api.cpython-311.pyc
   │        │  │  │  │  ├─ test_longdouble.cpython-311.pyc
   │        │  │  │  │  ├─ test_machar.cpython-311.pyc
   │        │  │  │  │  ├─ test_mem_overlap.cpython-311.pyc
   │        │  │  │  │  ├─ test_mem_policy.cpython-311.pyc
   │        │  │  │  │  ├─ test_memmap.cpython-311.pyc
   │        │  │  │  │  ├─ test_multiarray.cpython-311.pyc
   │        │  │  │  │  ├─ test_multithreading.cpython-311.pyc
   │        │  │  │  │  ├─ test_nditer.cpython-311.pyc
   │        │  │  │  │  ├─ test_nep50_promotions.cpython-311.pyc
   │        │  │  │  │  ├─ test_numeric.cpython-311.pyc
   │        │  │  │  │  ├─ test_numerictypes.cpython-311.pyc
   │        │  │  │  │  ├─ test_overrides.cpython-311.pyc
   │        │  │  │  │  ├─ test_print.cpython-311.pyc
   │        │  │  │  │  ├─ test_protocols.cpython-311.pyc
   │        │  │  │  │  ├─ test_records.cpython-311.pyc
   │        │  │  │  │  ├─ test_regression.cpython-311.pyc
   │        │  │  │  │  ├─ test_scalar_ctors.cpython-311.pyc
   │        │  │  │  │  ├─ test_scalar_methods.cpython-311.pyc
   │        │  │  │  │  ├─ test_scalarbuffer.cpython-311.pyc
   │        │  │  │  │  ├─ test_scalarinherit.cpython-311.pyc
   │        │  │  │  │  ├─ test_scalarmath.cpython-311.pyc
   │        │  │  │  │  ├─ test_scalarprint.cpython-311.pyc
   │        │  │  │  │  ├─ test_shape_base.cpython-311.pyc
   │        │  │  │  │  ├─ test_simd.cpython-311.pyc
   │        │  │  │  │  ├─ test_simd_module.cpython-311.pyc
   │        │  │  │  │  ├─ test_stringdtype.cpython-311.pyc
   │        │  │  │  │  ├─ test_strings.cpython-311.pyc
   │        │  │  │  │  ├─ test_ufunc.cpython-311.pyc
   │        │  │  │  │  ├─ test_umath.cpython-311.pyc
   │        │  │  │  │  ├─ test_umath_accuracy.cpython-311.pyc
   │        │  │  │  │  ├─ test_umath_complex.cpython-311.pyc
   │        │  │  │  │  └─ test_unicode.cpython-311.pyc
   │        │  │  │  ├─ _locales.py
   │        │  │  │  ├─ _natype.py
   │        │  │  │  ├─ data
   │        │  │  │  │  ├─ astype_copy.pkl
   │        │  │  │  │  ├─ generate_umath_validation_data.cpp
   │        │  │  │  │  ├─ recarray_from_file.fits
   │        │  │  │  │  ├─ umath-validation-set-README.txt
   │        │  │  │  │  ├─ umath-validation-set-arccos.csv
   │        │  │  │  │  ├─ umath-validation-set-arccosh.csv
   │        │  │  │  │  ├─ umath-validation-set-arcsin.csv
   │        │  │  │  │  ├─ umath-validation-set-arcsinh.csv
   │        │  │  │  │  ├─ umath-validation-set-arctan.csv
   │        │  │  │  │  ├─ umath-validation-set-arctanh.csv
   │        │  │  │  │  ├─ umath-validation-set-cbrt.csv
   │        │  │  │  │  ├─ umath-validation-set-cos.csv
   │        │  │  │  │  ├─ umath-validation-set-cosh.csv
   │        │  │  │  │  ├─ umath-validation-set-exp.csv
   │        │  │  │  │  ├─ umath-validation-set-exp2.csv
   │        │  │  │  │  ├─ umath-validation-set-expm1.csv
   │        │  │  │  │  ├─ umath-validation-set-log.csv
   │        │  │  │  │  ├─ umath-validation-set-log10.csv
   │        │  │  │  │  ├─ umath-validation-set-log1p.csv
   │        │  │  │  │  ├─ umath-validation-set-log2.csv
   │        │  │  │  │  ├─ umath-validation-set-sin.csv
   │        │  │  │  │  ├─ umath-validation-set-sinh.csv
   │        │  │  │  │  ├─ umath-validation-set-tan.csv
   │        │  │  │  │  └─ umath-validation-set-tanh.csv
   │        │  │  │  ├─ examples
   │        │  │  │  │  ├─ cython
   │        │  │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  │  └─ setup.cpython-311.pyc
   │        │  │  │  │  │  ├─ checks.pyx
   │        │  │  │  │  │  ├─ meson.build
   │        │  │  │  │  │  └─ setup.py
   │        │  │  │  │  └─ limited_api
   │        │  │  │  │     ├─ __pycache__
   │        │  │  │  │     │  └─ setup.cpython-311.pyc
   │        │  │  │  │     ├─ limited_api1.c
   │        │  │  │  │     ├─ limited_api2.pyx
   │        │  │  │  │     ├─ limited_api_latest.c
   │        │  │  │  │     ├─ meson.build
   │        │  │  │  │     └─ setup.py
   │        │  │  │  ├─ test__exceptions.py
   │        │  │  │  ├─ test_abc.py
   │        │  │  │  ├─ test_api.py
   │        │  │  │  ├─ test_argparse.py
   │        │  │  │  ├─ test_array_api_info.py
   │        │  │  │  ├─ test_array_coercion.py
   │        │  │  │  ├─ test_array_interface.py
   │        │  │  │  ├─ test_arraymethod.py
   │        │  │  │  ├─ test_arrayobject.py
   │        │  │  │  ├─ test_arrayprint.py
   │        │  │  │  ├─ test_casting_floatingpoint_errors.py
   │        │  │  │  ├─ test_casting_unittests.py
   │        │  │  │  ├─ test_conversion_utils.py
   │        │  │  │  ├─ test_cpu_dispatcher.py
   │        │  │  │  ├─ test_cpu_features.py
   │        │  │  │  ├─ test_custom_dtypes.py
   │        │  │  │  ├─ test_cython.py
   │        │  │  │  ├─ test_datetime.py
   │        │  │  │  ├─ test_defchararray.py
   │        │  │  │  ├─ test_deprecations.py
   │        │  │  │  ├─ test_dlpack.py
   │        │  │  │  ├─ test_dtype.py
   │        │  │  │  ├─ test_einsum.py
   │        │  │  │  ├─ test_errstate.py
   │        │  │  │  ├─ test_extint128.py
   │        │  │  │  ├─ test_function_base.py
   │        │  │  │  ├─ test_getlimits.py
   │        │  │  │  ├─ test_half.py
   │        │  │  │  ├─ test_hashtable.py
   │        │  │  │  ├─ test_indexerrors.py
   │        │  │  │  ├─ test_indexing.py
   │        │  │  │  ├─ test_item_selection.py
   │        │  │  │  ├─ test_limited_api.py
   │        │  │  │  ├─ test_longdouble.py
   │        │  │  │  ├─ test_machar.py
   │        │  │  │  ├─ test_mem_overlap.py
   │        │  │  │  ├─ test_mem_policy.py
   │        │  │  │  ├─ test_memmap.py
   │        │  │  │  ├─ test_multiarray.py
   │        │  │  │  ├─ test_multithreading.py
   │        │  │  │  ├─ test_nditer.py
   │        │  │  │  ├─ test_nep50_promotions.py
   │        │  │  │  ├─ test_numeric.py
   │        │  │  │  ├─ test_numerictypes.py
   │        │  │  │  ├─ test_overrides.py
   │        │  │  │  ├─ test_print.py
   │        │  │  │  ├─ test_protocols.py
   │        │  │  │  ├─ test_records.py
   │        │  │  │  ├─ test_regression.py
   │        │  │  │  ├─ test_scalar_ctors.py
   │        │  │  │  ├─ test_scalar_methods.py
   │        │  │  │  ├─ test_scalarbuffer.py
   │        │  │  │  ├─ test_scalarinherit.py
   │        │  │  │  ├─ test_scalarmath.py
   │        │  │  │  ├─ test_scalarprint.py
   │        │  │  │  ├─ test_shape_base.py
   │        │  │  │  ├─ test_simd.py
   │        │  │  │  ├─ test_simd_module.py
   │        │  │  │  ├─ test_stringdtype.py
   │        │  │  │  ├─ test_strings.py
   │        │  │  │  ├─ test_ufunc.py
   │        │  │  │  ├─ test_umath.py
   │        │  │  │  ├─ test_umath_accuracy.py
   │        │  │  │  ├─ test_umath_complex.py
   │        │  │  │  └─ test_unicode.py
   │        │  │  ├─ umath.py
   │        │  │  └─ umath.pyi
   │        │  ├─ _distributor_init.py
   │        │  ├─ _distributor_init.pyi
   │        │  ├─ _expired_attrs_2_0.py
   │        │  ├─ _expired_attrs_2_0.pyi
   │        │  ├─ _globals.py
   │        │  ├─ _globals.pyi
   │        │  ├─ _pyinstaller
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.pyi
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  └─ hook-numpy.cpython-311.pyc
   │        │  │  ├─ hook-numpy.py
   │        │  │  ├─ hook-numpy.pyi
   │        │  │  └─ tests
   │        │  │     ├─ __init__.py
   │        │  │     ├─ __pycache__
   │        │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │     │  ├─ pyinstaller-smoke.cpython-311.pyc
   │        │  │     │  └─ test_pyinstaller.cpython-311.pyc
   │        │  │     ├─ pyinstaller-smoke.py
   │        │  │     └─ test_pyinstaller.py
   │        │  ├─ _pytesttester.py
   │        │  ├─ _pytesttester.pyi
   │        │  ├─ _typing
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _add_docstring.cpython-311.pyc
   │        │  │  │  ├─ _array_like.cpython-311.pyc
   │        │  │  │  ├─ _char_codes.cpython-311.pyc
   │        │  │  │  ├─ _dtype_like.cpython-311.pyc
   │        │  │  │  ├─ _extended_precision.cpython-311.pyc
   │        │  │  │  ├─ _nbit.cpython-311.pyc
   │        │  │  │  ├─ _nbit_base.cpython-311.pyc
   │        │  │  │  ├─ _nested_sequence.cpython-311.pyc
   │        │  │  │  ├─ _scalars.cpython-311.pyc
   │        │  │  │  ├─ _shape.cpython-311.pyc
   │        │  │  │  └─ _ufunc.cpython-311.pyc
   │        │  │  ├─ _add_docstring.py
   │        │  │  ├─ _array_like.py
   │        │  │  ├─ _callable.pyi
   │        │  │  ├─ _char_codes.py
   │        │  │  ├─ _dtype_like.py
   │        │  │  ├─ _extended_precision.py
   │        │  │  ├─ _nbit.py
   │        │  │  ├─ _nbit_base.py
   │        │  │  ├─ _nested_sequence.py
   │        │  │  ├─ _scalars.py
   │        │  │  ├─ _shape.py
   │        │  │  ├─ _ufunc.py
   │        │  │  └─ _ufunc.pyi
   │        │  ├─ _utils
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.pyi
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _convertions.cpython-311.pyc
   │        │  │  │  ├─ _inspect.cpython-311.pyc
   │        │  │  │  └─ _pep440.cpython-311.pyc
   │        │  │  ├─ _convertions.py
   │        │  │  ├─ _convertions.pyi
   │        │  │  ├─ _inspect.py
   │        │  │  ├─ _inspect.pyi
   │        │  │  ├─ _pep440.py
   │        │  │  └─ _pep440.pyi
   │        │  ├─ char
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.pyi
   │        │  │  └─ __pycache__
   │        │  │     └─ __init__.cpython-311.pyc
   │        │  ├─ compat
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  └─ py3k.cpython-311.pyc
   │        │  │  ├─ py3k.py
   │        │  │  └─ tests
   │        │  │     ├─ __init__.py
   │        │  │     └─ __pycache__
   │        │  │        └─ __init__.cpython-311.pyc
   │        │  ├─ conftest.py
   │        │  ├─ core
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.pyi
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _dtype.cpython-311.pyc
   │        │  │  │  ├─ _dtype_ctypes.cpython-311.pyc
   │        │  │  │  ├─ _internal.cpython-311.pyc
   │        │  │  │  ├─ _multiarray_umath.cpython-311.pyc
   │        │  │  │  ├─ _utils.cpython-311.pyc
   │        │  │  │  ├─ arrayprint.cpython-311.pyc
   │        │  │  │  ├─ defchararray.cpython-311.pyc
   │        │  │  │  ├─ einsumfunc.cpython-311.pyc
   │        │  │  │  ├─ fromnumeric.cpython-311.pyc
   │        │  │  │  ├─ function_base.cpython-311.pyc
   │        │  │  │  ├─ getlimits.cpython-311.pyc
   │        │  │  │  ├─ multiarray.cpython-311.pyc
   │        │  │  │  ├─ numeric.cpython-311.pyc
   │        │  │  │  ├─ numerictypes.cpython-311.pyc
   │        │  │  │  ├─ overrides.cpython-311.pyc
   │        │  │  │  ├─ records.cpython-311.pyc
   │        │  │  │  ├─ shape_base.cpython-311.pyc
   │        │  │  │  └─ umath.cpython-311.pyc
   │        │  │  ├─ _dtype.py
   │        │  │  ├─ _dtype.pyi
   │        │  │  ├─ _dtype_ctypes.py
   │        │  │  ├─ _dtype_ctypes.pyi
   │        │  │  ├─ _internal.py
   │        │  │  ├─ _multiarray_umath.py
   │        │  │  ├─ _utils.py
   │        │  │  ├─ arrayprint.py
   │        │  │  ├─ defchararray.py
   │        │  │  ├─ einsumfunc.py
   │        │  │  ├─ fromnumeric.py
   │        │  │  ├─ function_base.py
   │        │  │  ├─ getlimits.py
   │        │  │  ├─ multiarray.py
   │        │  │  ├─ numeric.py
   │        │  │  ├─ numerictypes.py
   │        │  │  ├─ overrides.py
   │        │  │  ├─ overrides.pyi
   │        │  │  ├─ records.py
   │        │  │  ├─ shape_base.py
   │        │  │  └─ umath.py
   │        │  ├─ ctypeslib.py
   │        │  ├─ ctypeslib.pyi
   │        │  ├─ distutils
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.pyi
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _shell_utils.cpython-311.pyc
   │        │  │  │  ├─ armccompiler.cpython-311.pyc
   │        │  │  │  ├─ ccompiler.cpython-311.pyc
   │        │  │  │  ├─ ccompiler_opt.cpython-311.pyc
   │        │  │  │  ├─ conv_template.cpython-311.pyc
   │        │  │  │  ├─ core.cpython-311.pyc
   │        │  │  │  ├─ cpuinfo.cpython-311.pyc
   │        │  │  │  ├─ exec_command.cpython-311.pyc
   │        │  │  │  ├─ extension.cpython-311.pyc
   │        │  │  │  ├─ from_template.cpython-311.pyc
   │        │  │  │  ├─ fujitsuccompiler.cpython-311.pyc
   │        │  │  │  ├─ intelccompiler.cpython-311.pyc
   │        │  │  │  ├─ lib2def.cpython-311.pyc
   │        │  │  │  ├─ line_endings.cpython-311.pyc
   │        │  │  │  ├─ log.cpython-311.pyc
   │        │  │  │  ├─ mingw32ccompiler.cpython-311.pyc
   │        │  │  │  ├─ misc_util.cpython-311.pyc
   │        │  │  │  ├─ msvc9compiler.cpython-311.pyc
   │        │  │  │  ├─ msvccompiler.cpython-311.pyc
   │        │  │  │  ├─ npy_pkg_config.cpython-311.pyc
   │        │  │  │  ├─ numpy_distribution.cpython-311.pyc
   │        │  │  │  ├─ pathccompiler.cpython-311.pyc
   │        │  │  │  ├─ system_info.cpython-311.pyc
   │        │  │  │  └─ unixccompiler.cpython-311.pyc
   │        │  │  ├─ _shell_utils.py
   │        │  │  ├─ armccompiler.py
   │        │  │  ├─ ccompiler.py
   │        │  │  ├─ ccompiler_opt.py
   │        │  │  ├─ checks
   │        │  │  │  ├─ cpu_asimd.c
   │        │  │  │  ├─ cpu_asimddp.c
   │        │  │  │  ├─ cpu_asimdfhm.c
   │        │  │  │  ├─ cpu_asimdhp.c
   │        │  │  │  ├─ cpu_avx.c
   │        │  │  │  ├─ cpu_avx2.c
   │        │  │  │  ├─ cpu_avx512_clx.c
   │        │  │  │  ├─ cpu_avx512_cnl.c
   │        │  │  │  ├─ cpu_avx512_icl.c
   │        │  │  │  ├─ cpu_avx512_knl.c
   │        │  │  │  ├─ cpu_avx512_knm.c
   │        │  │  │  ├─ cpu_avx512_skx.c
   │        │  │  │  ├─ cpu_avx512_spr.c
   │        │  │  │  ├─ cpu_avx512cd.c
   │        │  │  │  ├─ cpu_avx512f.c
   │        │  │  │  ├─ cpu_f16c.c
   │        │  │  │  ├─ cpu_fma3.c
   │        │  │  │  ├─ cpu_fma4.c
   │        │  │  │  ├─ cpu_neon.c
   │        │  │  │  ├─ cpu_neon_fp16.c
   │        │  │  │  ├─ cpu_neon_vfpv4.c
   │        │  │  │  ├─ cpu_popcnt.c
   │        │  │  │  ├─ cpu_rvv.c
   │        │  │  │  ├─ cpu_sse.c
   │        │  │  │  ├─ cpu_sse2.c
   │        │  │  │  ├─ cpu_sse3.c
   │        │  │  │  ├─ cpu_sse41.c
   │        │  │  │  ├─ cpu_sse42.c
   │        │  │  │  ├─ cpu_ssse3.c
   │        │  │  │  ├─ cpu_sve.c
   │        │  │  │  ├─ cpu_vsx.c
   │        │  │  │  ├─ cpu_vsx2.c
   │        │  │  │  ├─ cpu_vsx3.c
   │        │  │  │  ├─ cpu_vsx4.c
   │        │  │  │  ├─ cpu_vx.c
   │        │  │  │  ├─ cpu_vxe.c
   │        │  │  │  ├─ cpu_vxe2.c
   │        │  │  │  ├─ cpu_xop.c
   │        │  │  │  ├─ extra_avx512bw_mask.c
   │        │  │  │  ├─ extra_avx512dq_mask.c
   │        │  │  │  ├─ extra_avx512f_reduce.c
   │        │  │  │  ├─ extra_vsx3_half_double.c
   │        │  │  │  ├─ extra_vsx4_mma.c
   │        │  │  │  ├─ extra_vsx_asm.c
   │        │  │  │  └─ test_flags.c
   │        │  │  ├─ command
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ autodist.cpython-311.pyc
   │        │  │  │  │  ├─ bdist_rpm.cpython-311.pyc
   │        │  │  │  │  ├─ build.cpython-311.pyc
   │        │  │  │  │  ├─ build_clib.cpython-311.pyc
   │        │  │  │  │  ├─ build_ext.cpython-311.pyc
   │        │  │  │  │  ├─ build_py.cpython-311.pyc
   │        │  │  │  │  ├─ build_scripts.cpython-311.pyc
   │        │  │  │  │  ├─ build_src.cpython-311.pyc
   │        │  │  │  │  ├─ config.cpython-311.pyc
   │        │  │  │  │  ├─ config_compiler.cpython-311.pyc
   │        │  │  │  │  ├─ develop.cpython-311.pyc
   │        │  │  │  │  ├─ egg_info.cpython-311.pyc
   │        │  │  │  │  ├─ install.cpython-311.pyc
   │        │  │  │  │  ├─ install_clib.cpython-311.pyc
   │        │  │  │  │  ├─ install_data.cpython-311.pyc
   │        │  │  │  │  ├─ install_headers.cpython-311.pyc
   │        │  │  │  │  └─ sdist.cpython-311.pyc
   │        │  │  │  ├─ autodist.py
   │        │  │  │  ├─ bdist_rpm.py
   │        │  │  │  ├─ build.py
   │        │  │  │  ├─ build_clib.py
   │        │  │  │  ├─ build_ext.py
   │        │  │  │  ├─ build_py.py
   │        │  │  │  ├─ build_scripts.py
   │        │  │  │  ├─ build_src.py
   │        │  │  │  ├─ config.py
   │        │  │  │  ├─ config_compiler.py
   │        │  │  │  ├─ develop.py
   │        │  │  │  ├─ egg_info.py
   │        │  │  │  ├─ install.py
   │        │  │  │  ├─ install_clib.py
   │        │  │  │  ├─ install_data.py
   │        │  │  │  ├─ install_headers.py
   │        │  │  │  └─ sdist.py
   │        │  │  ├─ conv_template.py
   │        │  │  ├─ core.py
   │        │  │  ├─ cpuinfo.py
   │        │  │  ├─ exec_command.py
   │        │  │  ├─ extension.py
   │        │  │  ├─ fcompiler
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ absoft.cpython-311.pyc
   │        │  │  │  │  ├─ arm.cpython-311.pyc
   │        │  │  │  │  ├─ compaq.cpython-311.pyc
   │        │  │  │  │  ├─ environment.cpython-311.pyc
   │        │  │  │  │  ├─ fujitsu.cpython-311.pyc
   │        │  │  │  │  ├─ g95.cpython-311.pyc
   │        │  │  │  │  ├─ gnu.cpython-311.pyc
   │        │  │  │  │  ├─ hpux.cpython-311.pyc
   │        │  │  │  │  ├─ ibm.cpython-311.pyc
   │        │  │  │  │  ├─ intel.cpython-311.pyc
   │        │  │  │  │  ├─ lahey.cpython-311.pyc
   │        │  │  │  │  ├─ mips.cpython-311.pyc
   │        │  │  │  │  ├─ nag.cpython-311.pyc
   │        │  │  │  │  ├─ none.cpython-311.pyc
   │        │  │  │  │  ├─ nv.cpython-311.pyc
   │        │  │  │  │  ├─ pathf95.cpython-311.pyc
   │        │  │  │  │  ├─ pg.cpython-311.pyc
   │        │  │  │  │  ├─ sun.cpython-311.pyc
   │        │  │  │  │  └─ vast.cpython-311.pyc
   │        │  │  │  ├─ absoft.py
   │        │  │  │  ├─ arm.py
   │        │  │  │  ├─ compaq.py
   │        │  │  │  ├─ environment.py
   │        │  │  │  ├─ fujitsu.py
   │        │  │  │  ├─ g95.py
   │        │  │  │  ├─ gnu.py
   │        │  │  │  ├─ hpux.py
   │        │  │  │  ├─ ibm.py
   │        │  │  │  ├─ intel.py
   │        │  │  │  ├─ lahey.py
   │        │  │  │  ├─ mips.py
   │        │  │  │  ├─ nag.py
   │        │  │  │  ├─ none.py
   │        │  │  │  ├─ nv.py
   │        │  │  │  ├─ pathf95.py
   │        │  │  │  ├─ pg.py
   │        │  │  │  ├─ sun.py
   │        │  │  │  └─ vast.py
   │        │  │  ├─ from_template.py
   │        │  │  ├─ fujitsuccompiler.py
   │        │  │  ├─ intelccompiler.py
   │        │  │  ├─ lib2def.py
   │        │  │  ├─ line_endings.py
   │        │  │  ├─ log.py
   │        │  │  ├─ mingw
   │        │  │  │  └─ gfortran_vs2003_hack.c
   │        │  │  ├─ mingw32ccompiler.py
   │        │  │  ├─ misc_util.py
   │        │  │  ├─ msvc9compiler.py
   │        │  │  ├─ msvccompiler.py
   │        │  │  ├─ npy_pkg_config.py
   │        │  │  ├─ numpy_distribution.py
   │        │  │  ├─ pathccompiler.py
   │        │  │  ├─ system_info.py
   │        │  │  ├─ tests
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test_build_ext.cpython-311.pyc
   │        │  │  │  │  ├─ test_ccompiler_opt.cpython-311.pyc
   │        │  │  │  │  ├─ test_ccompiler_opt_conf.cpython-311.pyc
   │        │  │  │  │  ├─ test_exec_command.cpython-311.pyc
   │        │  │  │  │  ├─ test_fcompiler.cpython-311.pyc
   │        │  │  │  │  ├─ test_fcompiler_gnu.cpython-311.pyc
   │        │  │  │  │  ├─ test_fcompiler_intel.cpython-311.pyc
   │        │  │  │  │  ├─ test_fcompiler_nagfor.cpython-311.pyc
   │        │  │  │  │  ├─ test_from_template.cpython-311.pyc
   │        │  │  │  │  ├─ test_log.cpython-311.pyc
   │        │  │  │  │  ├─ test_mingw32ccompiler.cpython-311.pyc
   │        │  │  │  │  ├─ test_misc_util.cpython-311.pyc
   │        │  │  │  │  ├─ test_npy_pkg_config.cpython-311.pyc
   │        │  │  │  │  ├─ test_shell_utils.cpython-311.pyc
   │        │  │  │  │  ├─ test_system_info.cpython-311.pyc
   │        │  │  │  │  └─ utilities.cpython-311.pyc
   │        │  │  │  ├─ test_build_ext.py
   │        │  │  │  ├─ test_ccompiler_opt.py
   │        │  │  │  ├─ test_ccompiler_opt_conf.py
   │        │  │  │  ├─ test_exec_command.py
   │        │  │  │  ├─ test_fcompiler.py
   │        │  │  │  ├─ test_fcompiler_gnu.py
   │        │  │  │  ├─ test_fcompiler_intel.py
   │        │  │  │  ├─ test_fcompiler_nagfor.py
   │        │  │  │  ├─ test_from_template.py
   │        │  │  │  ├─ test_log.py
   │        │  │  │  ├─ test_mingw32ccompiler.py
   │        │  │  │  ├─ test_misc_util.py
   │        │  │  │  ├─ test_npy_pkg_config.py
   │        │  │  │  ├─ test_shell_utils.py
   │        │  │  │  ├─ test_system_info.py
   │        │  │  │  └─ utilities.py
   │        │  │  └─ unixccompiler.py
   │        │  ├─ doc
   │        │  │  ├─ __pycache__
   │        │  │  │  └─ ufuncs.cpython-311.pyc
   │        │  │  └─ ufuncs.py
   │        │  ├─ dtypes.py
   │        │  ├─ dtypes.pyi
   │        │  ├─ exceptions.py
   │        │  ├─ exceptions.pyi
   │        │  ├─ f2py
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.pyi
   │        │  │  ├─ __main__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ __main__.cpython-311.pyc
   │        │  │  │  ├─ __version__.cpython-311.pyc
   │        │  │  │  ├─ _isocbind.cpython-311.pyc
   │        │  │  │  ├─ _src_pyf.cpython-311.pyc
   │        │  │  │  ├─ auxfuncs.cpython-311.pyc
   │        │  │  │  ├─ capi_maps.cpython-311.pyc
   │        │  │  │  ├─ cb_rules.cpython-311.pyc
   │        │  │  │  ├─ cfuncs.cpython-311.pyc
   │        │  │  │  ├─ common_rules.cpython-311.pyc
   │        │  │  │  ├─ crackfortran.cpython-311.pyc
   │        │  │  │  ├─ diagnose.cpython-311.pyc
   │        │  │  │  ├─ f2py2e.cpython-311.pyc
   │        │  │  │  ├─ f90mod_rules.cpython-311.pyc
   │        │  │  │  ├─ func2subr.cpython-311.pyc
   │        │  │  │  ├─ rules.cpython-311.pyc
   │        │  │  │  ├─ symbolic.cpython-311.pyc
   │        │  │  │  └─ use_rules.cpython-311.pyc
   │        │  │  ├─ __version__.py
   │        │  │  ├─ _backends
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ _backend.cpython-311.pyc
   │        │  │  │  │  ├─ _distutils.cpython-311.pyc
   │        │  │  │  │  └─ _meson.cpython-311.pyc
   │        │  │  │  ├─ _backend.py
   │        │  │  │  ├─ _distutils.py
   │        │  │  │  ├─ _meson.py
   │        │  │  │  └─ meson.build.template
   │        │  │  ├─ _isocbind.py
   │        │  │  ├─ _src_pyf.py
   │        │  │  ├─ auxfuncs.py
   │        │  │  ├─ capi_maps.py
   │        │  │  ├─ cb_rules.py
   │        │  │  ├─ cfuncs.py
   │        │  │  ├─ common_rules.py
   │        │  │  ├─ crackfortran.py
   │        │  │  ├─ diagnose.py
   │        │  │  ├─ f2py2e.py
   │        │  │  ├─ f90mod_rules.py
   │        │  │  ├─ func2subr.py
   │        │  │  ├─ rules.py
   │        │  │  ├─ setup.cfg
   │        │  │  ├─ src
   │        │  │  │  ├─ fortranobject.c
   │        │  │  │  └─ fortranobject.h
   │        │  │  ├─ symbolic.py
   │        │  │  ├─ tests
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test_abstract_interface.cpython-311.pyc
   │        │  │  │  │  ├─ test_array_from_pyobj.cpython-311.pyc
   │        │  │  │  │  ├─ test_assumed_shape.cpython-311.pyc
   │        │  │  │  │  ├─ test_block_docstring.cpython-311.pyc
   │        │  │  │  │  ├─ test_callback.cpython-311.pyc
   │        │  │  │  │  ├─ test_character.cpython-311.pyc
   │        │  │  │  │  ├─ test_common.cpython-311.pyc
   │        │  │  │  │  ├─ test_crackfortran.cpython-311.pyc
   │        │  │  │  │  ├─ test_data.cpython-311.pyc
   │        │  │  │  │  ├─ test_docs.cpython-311.pyc
   │        │  │  │  │  ├─ test_f2cmap.cpython-311.pyc
   │        │  │  │  │  ├─ test_f2py2e.cpython-311.pyc
   │        │  │  │  │  ├─ test_isoc.cpython-311.pyc
   │        │  │  │  │  ├─ test_kind.cpython-311.pyc
   │        │  │  │  │  ├─ test_mixed.cpython-311.pyc
   │        │  │  │  │  ├─ test_modules.cpython-311.pyc
   │        │  │  │  │  ├─ test_parameter.cpython-311.pyc
   │        │  │  │  │  ├─ test_pyf_src.cpython-311.pyc
   │        │  │  │  │  ├─ test_quoted_character.cpython-311.pyc
   │        │  │  │  │  ├─ test_regression.cpython-311.pyc
   │        │  │  │  │  ├─ test_return_character.cpython-311.pyc
   │        │  │  │  │  ├─ test_return_complex.cpython-311.pyc
   │        │  │  │  │  ├─ test_return_integer.cpython-311.pyc
   │        │  │  │  │  ├─ test_return_logical.cpython-311.pyc
   │        │  │  │  │  ├─ test_return_real.cpython-311.pyc
   │        │  │  │  │  ├─ test_routines.cpython-311.pyc
   │        │  │  │  │  ├─ test_semicolon_split.cpython-311.pyc
   │        │  │  │  │  ├─ test_size.cpython-311.pyc
   │        │  │  │  │  ├─ test_string.cpython-311.pyc
   │        │  │  │  │  ├─ test_symbolic.cpython-311.pyc
   │        │  │  │  │  ├─ test_value_attrspec.cpython-311.pyc
   │        │  │  │  │  └─ util.cpython-311.pyc
   │        │  │  │  ├─ src
   │        │  │  │  │  ├─ abstract_interface
   │        │  │  │  │  │  ├─ foo.f90
   │        │  │  │  │  │  └─ gh18403_mod.f90
   │        │  │  │  │  ├─ array_from_pyobj
   │        │  │  │  │  │  └─ wrapmodule.c
   │        │  │  │  │  ├─ assumed_shape
   │        │  │  │  │  │  ├─ .f2py_f2cmap
   │        │  │  │  │  │  ├─ foo_free.f90
   │        │  │  │  │  │  ├─ foo_mod.f90
   │        │  │  │  │  │  ├─ foo_use.f90
   │        │  │  │  │  │  └─ precision.f90
   │        │  │  │  │  ├─ block_docstring
   │        │  │  │  │  │  └─ foo.f
   │        │  │  │  │  ├─ callback
   │        │  │  │  │  │  ├─ foo.f
   │        │  │  │  │  │  ├─ gh17797.f90
   │        │  │  │  │  │  ├─ gh18335.f90
   │        │  │  │  │  │  ├─ gh25211.f
   │        │  │  │  │  │  ├─ gh25211.pyf
   │        │  │  │  │  │  └─ gh26681.f90
   │        │  │  │  │  ├─ cli
   │        │  │  │  │  │  ├─ gh_22819.pyf
   │        │  │  │  │  │  ├─ hi77.f
   │        │  │  │  │  │  └─ hiworld.f90
   │        │  │  │  │  ├─ common
   │        │  │  │  │  │  ├─ block.f
   │        │  │  │  │  │  └─ gh19161.f90
   │        │  │  │  │  ├─ crackfortran
   │        │  │  │  │  │  ├─ accesstype.f90
   │        │  │  │  │  │  ├─ common_with_division.f
   │        │  │  │  │  │  ├─ data_common.f
   │        │  │  │  │  │  ├─ data_multiplier.f
   │        │  │  │  │  │  ├─ data_stmts.f90
   │        │  │  │  │  │  ├─ data_with_comments.f
   │        │  │  │  │  │  ├─ foo_deps.f90
   │        │  │  │  │  │  ├─ gh15035.f
   │        │  │  │  │  │  ├─ gh17859.f
   │        │  │  │  │  │  ├─ gh22648.pyf
   │        │  │  │  │  │  ├─ gh23533.f
   │        │  │  │  │  │  ├─ gh23598.f90
   │        │  │  │  │  │  ├─ gh23598Warn.f90
   │        │  │  │  │  │  ├─ gh23879.f90
   │        │  │  │  │  │  ├─ gh27697.f90
   │        │  │  │  │  │  ├─ gh2848.f90
   │        │  │  │  │  │  ├─ operators.f90
   │        │  │  │  │  │  ├─ privatemod.f90
   │        │  │  │  │  │  ├─ publicmod.f90
   │        │  │  │  │  │  ├─ pubprivmod.f90
   │        │  │  │  │  │  └─ unicode_comment.f90
   │        │  │  │  │  ├─ f2cmap
   │        │  │  │  │  │  ├─ .f2py_f2cmap
   │        │  │  │  │  │  └─ isoFortranEnvMap.f90
   │        │  │  │  │  ├─ isocintrin
   │        │  │  │  │  │  └─ isoCtests.f90
   │        │  │  │  │  ├─ kind
   │        │  │  │  │  │  └─ foo.f90
   │        │  │  │  │  ├─ mixed
   │        │  │  │  │  │  ├─ foo.f
   │        │  │  │  │  │  ├─ foo_fixed.f90
   │        │  │  │  │  │  └─ foo_free.f90
   │        │  │  │  │  ├─ modules
   │        │  │  │  │  │  ├─ gh25337
   │        │  │  │  │  │  │  ├─ data.f90
   │        │  │  │  │  │  │  └─ use_data.f90
   │        │  │  │  │  │  ├─ gh26920
   │        │  │  │  │  │  │  ├─ two_mods_with_no_public_entities.f90
   │        │  │  │  │  │  │  └─ two_mods_with_one_public_routine.f90
   │        │  │  │  │  │  ├─ module_data_docstring.f90
   │        │  │  │  │  │  └─ use_modules.f90
   │        │  │  │  │  ├─ negative_bounds
   │        │  │  │  │  │  └─ issue_20853.f90
   │        │  │  │  │  ├─ parameter
   │        │  │  │  │  │  ├─ constant_array.f90
   │        │  │  │  │  │  ├─ constant_both.f90
   │        │  │  │  │  │  ├─ constant_compound.f90
   │        │  │  │  │  │  ├─ constant_integer.f90
   │        │  │  │  │  │  ├─ constant_non_compound.f90
   │        │  │  │  │  │  └─ constant_real.f90
   │        │  │  │  │  ├─ quoted_character
   │        │  │  │  │  │  └─ foo.f
   │        │  │  │  │  ├─ regression
   │        │  │  │  │  │  ├─ AB.inc
   │        │  │  │  │  │  ├─ assignOnlyModule.f90
   │        │  │  │  │  │  ├─ datonly.f90
   │        │  │  │  │  │  ├─ f77comments.f
   │        │  │  │  │  │  ├─ f77fixedform.f95
   │        │  │  │  │  │  ├─ f90continuation.f90
   │        │  │  │  │  │  ├─ incfile.f90
   │        │  │  │  │  │  ├─ inout.f90
   │        │  │  │  │  │  └─ lower_f2py_fortran.f90
   │        │  │  │  │  ├─ return_character
   │        │  │  │  │  │  ├─ foo77.f
   │        │  │  │  │  │  └─ foo90.f90
   │        │  │  │  │  ├─ return_complex
   │        │  │  │  │  │  ├─ foo77.f
   │        │  │  │  │  │  └─ foo90.f90
   │        │  │  │  │  ├─ return_integer
   │        │  │  │  │  │  ├─ foo77.f
   │        │  │  │  │  │  └─ foo90.f90
   │        │  │  │  │  ├─ return_logical
   │        │  │  │  │  │  ├─ foo77.f
   │        │  │  │  │  │  └─ foo90.f90
   │        │  │  │  │  ├─ return_real
   │        │  │  │  │  │  ├─ foo77.f
   │        │  │  │  │  │  └─ foo90.f90
   │        │  │  │  │  ├─ routines
   │        │  │  │  │  │  ├─ funcfortranname.f
   │        │  │  │  │  │  ├─ funcfortranname.pyf
   │        │  │  │  │  │  ├─ subrout.f
   │        │  │  │  │  │  └─ subrout.pyf
   │        │  │  │  │  ├─ size
   │        │  │  │  │  │  └─ foo.f90
   │        │  │  │  │  ├─ string
   │        │  │  │  │  │  ├─ char.f90
   │        │  │  │  │  │  ├─ fixed_string.f90
   │        │  │  │  │  │  ├─ gh24008.f
   │        │  │  │  │  │  ├─ gh24662.f90
   │        │  │  │  │  │  ├─ gh25286.f90
   │        │  │  │  │  │  ├─ gh25286.pyf
   │        │  │  │  │  │  ├─ gh25286_bc.pyf
   │        │  │  │  │  │  ├─ scalar_string.f90
   │        │  │  │  │  │  └─ string.f
   │        │  │  │  │  └─ value_attrspec
   │        │  │  │  │     └─ gh21665.f90
   │        │  │  │  ├─ test_abstract_interface.py
   │        │  │  │  ├─ test_array_from_pyobj.py
   │        │  │  │  ├─ test_assumed_shape.py
   │        │  │  │  ├─ test_block_docstring.py
   │        │  │  │  ├─ test_callback.py
   │        │  │  │  ├─ test_character.py
   │        │  │  │  ├─ test_common.py
   │        │  │  │  ├─ test_crackfortran.py
   │        │  │  │  ├─ test_data.py
   │        │  │  │  ├─ test_docs.py
   │        │  │  │  ├─ test_f2cmap.py
   │        │  │  │  ├─ test_f2py2e.py
   │        │  │  │  ├─ test_isoc.py
   │        │  │  │  ├─ test_kind.py
   │        │  │  │  ├─ test_mixed.py
   │        │  │  │  ├─ test_modules.py
   │        │  │  │  ├─ test_parameter.py
   │        │  │  │  ├─ test_pyf_src.py
   │        │  │  │  ├─ test_quoted_character.py
   │        │  │  │  ├─ test_regression.py
   │        │  │  │  ├─ test_return_character.py
   │        │  │  │  ├─ test_return_complex.py
   │        │  │  │  ├─ test_return_integer.py
   │        │  │  │  ├─ test_return_logical.py
   │        │  │  │  ├─ test_return_real.py
   │        │  │  │  ├─ test_routines.py
   │        │  │  │  ├─ test_semicolon_split.py
   │        │  │  │  ├─ test_size.py
   │        │  │  │  ├─ test_string.py
   │        │  │  │  ├─ test_symbolic.py
   │        │  │  │  ├─ test_value_attrspec.py
   │        │  │  │  └─ util.py
   │        │  │  └─ use_rules.py
   │        │  ├─ fft
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.pyi
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _helper.cpython-311.pyc
   │        │  │  │  ├─ _pocketfft.cpython-311.pyc
   │        │  │  │  └─ helper.cpython-311.pyc
   │        │  │  ├─ _helper.py
   │        │  │  ├─ _helper.pyi
   │        │  │  ├─ _pocketfft.py
   │        │  │  ├─ _pocketfft.pyi
   │        │  │  ├─ _pocketfft_umath.cpython-311-darwin.so
   │        │  │  ├─ helper.py
   │        │  │  ├─ helper.pyi
   │        │  │  └─ tests
   │        │  │     ├─ __init__.py
   │        │  │     ├─ __pycache__
   │        │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │     │  ├─ test_helper.cpython-311.pyc
   │        │  │     │  └─ test_pocketfft.cpython-311.pyc
   │        │  │     ├─ test_helper.py
   │        │  │     └─ test_pocketfft.py
   │        │  ├─ lib
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.pyi
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _array_utils_impl.cpython-311.pyc
   │        │  │  │  ├─ _arraypad_impl.cpython-311.pyc
   │        │  │  │  ├─ _arraysetops_impl.cpython-311.pyc
   │        │  │  │  ├─ _arrayterator_impl.cpython-311.pyc
   │        │  │  │  ├─ _datasource.cpython-311.pyc
   │        │  │  │  ├─ _function_base_impl.cpython-311.pyc
   │        │  │  │  ├─ _histograms_impl.cpython-311.pyc
   │        │  │  │  ├─ _index_tricks_impl.cpython-311.pyc
   │        │  │  │  ├─ _iotools.cpython-311.pyc
   │        │  │  │  ├─ _nanfunctions_impl.cpython-311.pyc
   │        │  │  │  ├─ _npyio_impl.cpython-311.pyc
   │        │  │  │  ├─ _polynomial_impl.cpython-311.pyc
   │        │  │  │  ├─ _scimath_impl.cpython-311.pyc
   │        │  │  │  ├─ _shape_base_impl.cpython-311.pyc
   │        │  │  │  ├─ _stride_tricks_impl.cpython-311.pyc
   │        │  │  │  ├─ _twodim_base_impl.cpython-311.pyc
   │        │  │  │  ├─ _type_check_impl.cpython-311.pyc
   │        │  │  │  ├─ _ufunclike_impl.cpython-311.pyc
   │        │  │  │  ├─ _user_array_impl.cpython-311.pyc
   │        │  │  │  ├─ _utils_impl.cpython-311.pyc
   │        │  │  │  ├─ _version.cpython-311.pyc
   │        │  │  │  ├─ array_utils.cpython-311.pyc
   │        │  │  │  ├─ format.cpython-311.pyc
   │        │  │  │  ├─ introspect.cpython-311.pyc
   │        │  │  │  ├─ mixins.cpython-311.pyc
   │        │  │  │  ├─ npyio.cpython-311.pyc
   │        │  │  │  ├─ recfunctions.cpython-311.pyc
   │        │  │  │  ├─ scimath.cpython-311.pyc
   │        │  │  │  ├─ stride_tricks.cpython-311.pyc
   │        │  │  │  └─ user_array.cpython-311.pyc
   │        │  │  ├─ _array_utils_impl.py
   │        │  │  ├─ _array_utils_impl.pyi
   │        │  │  ├─ _arraypad_impl.py
   │        │  │  ├─ _arraypad_impl.pyi
   │        │  │  ├─ _arraysetops_impl.py
   │        │  │  ├─ _arraysetops_impl.pyi
   │        │  │  ├─ _arrayterator_impl.py
   │        │  │  ├─ _arrayterator_impl.pyi
   │        │  │  ├─ _datasource.py
   │        │  │  ├─ _datasource.pyi
   │        │  │  ├─ _function_base_impl.py
   │        │  │  ├─ _function_base_impl.pyi
   │        │  │  ├─ _histograms_impl.py
   │        │  │  ├─ _histograms_impl.pyi
   │        │  │  ├─ _index_tricks_impl.py
   │        │  │  ├─ _index_tricks_impl.pyi
   │        │  │  ├─ _iotools.py
   │        │  │  ├─ _iotools.pyi
   │        │  │  ├─ _nanfunctions_impl.py
   │        │  │  ├─ _nanfunctions_impl.pyi
   │        │  │  ├─ _npyio_impl.py
   │        │  │  ├─ _npyio_impl.pyi
   │        │  │  ├─ _polynomial_impl.py
   │        │  │  ├─ _polynomial_impl.pyi
   │        │  │  ├─ _scimath_impl.py
   │        │  │  ├─ _scimath_impl.pyi
   │        │  │  ├─ _shape_base_impl.py
   │        │  │  ├─ _shape_base_impl.pyi
   │        │  │  ├─ _stride_tricks_impl.py
   │        │  │  ├─ _stride_tricks_impl.pyi
   │        │  │  ├─ _twodim_base_impl.py
   │        │  │  ├─ _twodim_base_impl.pyi
   │        │  │  ├─ _type_check_impl.py
   │        │  │  ├─ _type_check_impl.pyi
   │        │  │  ├─ _ufunclike_impl.py
   │        │  │  ├─ _ufunclike_impl.pyi
   │        │  │  ├─ _user_array_impl.py
   │        │  │  ├─ _user_array_impl.pyi
   │        │  │  ├─ _utils_impl.py
   │        │  │  ├─ _utils_impl.pyi
   │        │  │  ├─ _version.py
   │        │  │  ├─ _version.pyi
   │        │  │  ├─ array_utils.py
   │        │  │  ├─ array_utils.pyi
   │        │  │  ├─ format.py
   │        │  │  ├─ format.pyi
   │        │  │  ├─ introspect.py
   │        │  │  ├─ introspect.pyi
   │        │  │  ├─ mixins.py
   │        │  │  ├─ mixins.pyi
   │        │  │  ├─ npyio.py
   │        │  │  ├─ npyio.pyi
   │        │  │  ├─ recfunctions.py
   │        │  │  ├─ recfunctions.pyi
   │        │  │  ├─ scimath.py
   │        │  │  ├─ scimath.pyi
   │        │  │  ├─ stride_tricks.py
   │        │  │  ├─ stride_tricks.pyi
   │        │  │  ├─ tests
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test__datasource.cpython-311.pyc
   │        │  │  │  │  ├─ test__iotools.cpython-311.pyc
   │        │  │  │  │  ├─ test__version.cpython-311.pyc
   │        │  │  │  │  ├─ test_array_utils.cpython-311.pyc
   │        │  │  │  │  ├─ test_arraypad.cpython-311.pyc
   │        │  │  │  │  ├─ test_arraysetops.cpython-311.pyc
   │        │  │  │  │  ├─ test_arrayterator.cpython-311.pyc
   │        │  │  │  │  ├─ test_format.cpython-311.pyc
   │        │  │  │  │  ├─ test_function_base.cpython-311.pyc
   │        │  │  │  │  ├─ test_histograms.cpython-311.pyc
   │        │  │  │  │  ├─ test_index_tricks.cpython-311.pyc
   │        │  │  │  │  ├─ test_io.cpython-311.pyc
   │        │  │  │  │  ├─ test_loadtxt.cpython-311.pyc
   │        │  │  │  │  ├─ test_mixins.cpython-311.pyc
   │        │  │  │  │  ├─ test_nanfunctions.cpython-311.pyc
   │        │  │  │  │  ├─ test_packbits.cpython-311.pyc
   │        │  │  │  │  ├─ test_polynomial.cpython-311.pyc
   │        │  │  │  │  ├─ test_recfunctions.cpython-311.pyc
   │        │  │  │  │  ├─ test_regression.cpython-311.pyc
   │        │  │  │  │  ├─ test_shape_base.cpython-311.pyc
   │        │  │  │  │  ├─ test_stride_tricks.cpython-311.pyc
   │        │  │  │  │  ├─ test_twodim_base.cpython-311.pyc
   │        │  │  │  │  ├─ test_type_check.cpython-311.pyc
   │        │  │  │  │  ├─ test_ufunclike.cpython-311.pyc
   │        │  │  │  │  └─ test_utils.cpython-311.pyc
   │        │  │  │  ├─ data
   │        │  │  │  │  ├─ py2-np0-objarr.npy
   │        │  │  │  │  ├─ py2-objarr.npy
   │        │  │  │  │  ├─ py2-objarr.npz
   │        │  │  │  │  ├─ py3-objarr.npy
   │        │  │  │  │  ├─ py3-objarr.npz
   │        │  │  │  │  ├─ python3.npy
   │        │  │  │  │  └─ win64python2.npy
   │        │  │  │  ├─ test__datasource.py
   │        │  │  │  ├─ test__iotools.py
   │        │  │  │  ├─ test__version.py
   │        │  │  │  ├─ test_array_utils.py
   │        │  │  │  ├─ test_arraypad.py
   │        │  │  │  ├─ test_arraysetops.py
   │        │  │  │  ├─ test_arrayterator.py
   │        │  │  │  ├─ test_format.py
   │        │  │  │  ├─ test_function_base.py
   │        │  │  │  ├─ test_histograms.py
   │        │  │  │  ├─ test_index_tricks.py
   │        │  │  │  ├─ test_io.py
   │        │  │  │  ├─ test_loadtxt.py
   │        │  │  │  ├─ test_mixins.py
   │        │  │  │  ├─ test_nanfunctions.py
   │        │  │  │  ├─ test_packbits.py
   │        │  │  │  ├─ test_polynomial.py
   │        │  │  │  ├─ test_recfunctions.py
   │        │  │  │  ├─ test_regression.py
   │        │  │  │  ├─ test_shape_base.py
   │        │  │  │  ├─ test_stride_tricks.py
   │        │  │  │  ├─ test_twodim_base.py
   │        │  │  │  ├─ test_type_check.py
   │        │  │  │  ├─ test_ufunclike.py
   │        │  │  │  └─ test_utils.py
   │        │  │  ├─ user_array.py
   │        │  │  └─ user_array.pyi
   │        │  ├─ linalg
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.pyi
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _linalg.cpython-311.pyc
   │        │  │  │  └─ linalg.cpython-311.pyc
   │        │  │  ├─ _linalg.py
   │        │  │  ├─ _linalg.pyi
   │        │  │  ├─ _umath_linalg.cpython-311-darwin.so
   │        │  │  ├─ _umath_linalg.pyi
   │        │  │  ├─ lapack_lite.cpython-311-darwin.so
   │        │  │  ├─ lapack_lite.pyi
   │        │  │  ├─ linalg.py
   │        │  │  ├─ linalg.pyi
   │        │  │  └─ tests
   │        │  │     ├─ __init__.py
   │        │  │     ├─ __pycache__
   │        │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │     │  ├─ test_deprecations.cpython-311.pyc
   │        │  │     │  ├─ test_linalg.cpython-311.pyc
   │        │  │     │  └─ test_regression.cpython-311.pyc
   │        │  │     ├─ test_deprecations.py
   │        │  │     ├─ test_linalg.py
   │        │  │     └─ test_regression.py
   │        │  ├─ ma
   │        │  │  ├─ API_CHANGES.txt
   │        │  │  ├─ LICENSE
   │        │  │  ├─ README.rst
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.pyi
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ core.cpython-311.pyc
   │        │  │  │  ├─ extras.cpython-311.pyc
   │        │  │  │  ├─ mrecords.cpython-311.pyc
   │        │  │  │  ├─ testutils.cpython-311.pyc
   │        │  │  │  └─ timer_comparison.cpython-311.pyc
   │        │  │  ├─ core.py
   │        │  │  ├─ core.pyi
   │        │  │  ├─ extras.py
   │        │  │  ├─ extras.pyi
   │        │  │  ├─ mrecords.py
   │        │  │  ├─ mrecords.pyi
   │        │  │  ├─ tests
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test_arrayobject.cpython-311.pyc
   │        │  │  │  │  ├─ test_core.cpython-311.pyc
   │        │  │  │  │  ├─ test_deprecations.cpython-311.pyc
   │        │  │  │  │  ├─ test_extras.cpython-311.pyc
   │        │  │  │  │  ├─ test_mrecords.cpython-311.pyc
   │        │  │  │  │  ├─ test_old_ma.cpython-311.pyc
   │        │  │  │  │  ├─ test_regression.cpython-311.pyc
   │        │  │  │  │  └─ test_subclassing.cpython-311.pyc
   │        │  │  │  ├─ test_arrayobject.py
   │        │  │  │  ├─ test_core.py
   │        │  │  │  ├─ test_deprecations.py
   │        │  │  │  ├─ test_extras.py
   │        │  │  │  ├─ test_mrecords.py
   │        │  │  │  ├─ test_old_ma.py
   │        │  │  │  ├─ test_regression.py
   │        │  │  │  └─ test_subclassing.py
   │        │  │  ├─ testutils.py
   │        │  │  └─ timer_comparison.py
   │        │  ├─ matlib.py
   │        │  ├─ matlib.pyi
   │        │  ├─ matrixlib
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.pyi
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  └─ defmatrix.cpython-311.pyc
   │        │  │  ├─ defmatrix.py
   │        │  │  ├─ defmatrix.pyi
   │        │  │  └─ tests
   │        │  │     ├─ __init__.py
   │        │  │     ├─ __pycache__
   │        │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │     │  ├─ test_defmatrix.cpython-311.pyc
   │        │  │     │  ├─ test_interaction.cpython-311.pyc
   │        │  │     │  ├─ test_masked_matrix.cpython-311.pyc
   │        │  │     │  ├─ test_matrix_linalg.cpython-311.pyc
   │        │  │     │  ├─ test_multiarray.cpython-311.pyc
   │        │  │     │  ├─ test_numeric.cpython-311.pyc
   │        │  │     │  └─ test_regression.cpython-311.pyc
   │        │  │     ├─ test_defmatrix.py
   │        │  │     ├─ test_interaction.py
   │        │  │     ├─ test_masked_matrix.py
   │        │  │     ├─ test_matrix_linalg.py
   │        │  │     ├─ test_multiarray.py
   │        │  │     ├─ test_numeric.py
   │        │  │     └─ test_regression.py
   │        │  ├─ polynomial
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.pyi
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _polybase.cpython-311.pyc
   │        │  │  │  ├─ chebyshev.cpython-311.pyc
   │        │  │  │  ├─ hermite.cpython-311.pyc
   │        │  │  │  ├─ hermite_e.cpython-311.pyc
   │        │  │  │  ├─ laguerre.cpython-311.pyc
   │        │  │  │  ├─ legendre.cpython-311.pyc
   │        │  │  │  ├─ polynomial.cpython-311.pyc
   │        │  │  │  └─ polyutils.cpython-311.pyc
   │        │  │  ├─ _polybase.py
   │        │  │  ├─ _polybase.pyi
   │        │  │  ├─ _polytypes.pyi
   │        │  │  ├─ chebyshev.py
   │        │  │  ├─ chebyshev.pyi
   │        │  │  ├─ hermite.py
   │        │  │  ├─ hermite.pyi
   │        │  │  ├─ hermite_e.py
   │        │  │  ├─ hermite_e.pyi
   │        │  │  ├─ laguerre.py
   │        │  │  ├─ laguerre.pyi
   │        │  │  ├─ legendre.py
   │        │  │  ├─ legendre.pyi
   │        │  │  ├─ polynomial.py
   │        │  │  ├─ polynomial.pyi
   │        │  │  ├─ polyutils.py
   │        │  │  ├─ polyutils.pyi
   │        │  │  └─ tests
   │        │  │     ├─ __init__.py
   │        │  │     ├─ __pycache__
   │        │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │     │  ├─ test_chebyshev.cpython-311.pyc
   │        │  │     │  ├─ test_classes.cpython-311.pyc
   │        │  │     │  ├─ test_hermite.cpython-311.pyc
   │        │  │     │  ├─ test_hermite_e.cpython-311.pyc
   │        │  │     │  ├─ test_laguerre.cpython-311.pyc
   │        │  │     │  ├─ test_legendre.cpython-311.pyc
   │        │  │     │  ├─ test_polynomial.cpython-311.pyc
   │        │  │     │  ├─ test_polyutils.cpython-311.pyc
   │        │  │     │  ├─ test_printing.cpython-311.pyc
   │        │  │     │  └─ test_symbol.cpython-311.pyc
   │        │  │     ├─ test_chebyshev.py
   │        │  │     ├─ test_classes.py
   │        │  │     ├─ test_hermite.py
   │        │  │     ├─ test_hermite_e.py
   │        │  │     ├─ test_laguerre.py
   │        │  │     ├─ test_legendre.py
   │        │  │     ├─ test_polynomial.py
   │        │  │     ├─ test_polyutils.py
   │        │  │     ├─ test_printing.py
   │        │  │     └─ test_symbol.py
   │        │  ├─ py.typed
   │        │  ├─ random
   │        │  │  ├─ LICENSE.md
   │        │  │  ├─ __init__.pxd
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.pyi
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  └─ _pickle.cpython-311.pyc
   │        │  │  ├─ _bounded_integers.cpython-311-darwin.so
   │        │  │  ├─ _bounded_integers.pxd
   │        │  │  ├─ _common.cpython-311-darwin.so
   │        │  │  ├─ _common.pxd
   │        │  │  ├─ _examples
   │        │  │  │  ├─ cffi
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ extending.cpython-311.pyc
   │        │  │  │  │  │  └─ parse.cpython-311.pyc
   │        │  │  │  │  ├─ extending.py
   │        │  │  │  │  └─ parse.py
   │        │  │  │  ├─ cython
   │        │  │  │  │  ├─ extending.pyx
   │        │  │  │  │  ├─ extending_distributions.pyx
   │        │  │  │  │  └─ meson.build
   │        │  │  │  └─ numba
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ extending.cpython-311.pyc
   │        │  │  │     │  └─ extending_distributions.cpython-311.pyc
   │        │  │  │     ├─ extending.py
   │        │  │  │     └─ extending_distributions.py
   │        │  │  ├─ _generator.cpython-311-darwin.so
   │        │  │  ├─ _generator.pyi
   │        │  │  ├─ _mt19937.cpython-311-darwin.so
   │        │  │  ├─ _mt19937.pyi
   │        │  │  ├─ _pcg64.cpython-311-darwin.so
   │        │  │  ├─ _pcg64.pyi
   │        │  │  ├─ _philox.cpython-311-darwin.so
   │        │  │  ├─ _philox.pyi
   │        │  │  ├─ _pickle.py
   │        │  │  ├─ _pickle.pyi
   │        │  │  ├─ _sfc64.cpython-311-darwin.so
   │        │  │  ├─ _sfc64.pyi
   │        │  │  ├─ bit_generator.cpython-311-darwin.so
   │        │  │  ├─ bit_generator.pxd
   │        │  │  ├─ bit_generator.pyi
   │        │  │  ├─ c_distributions.pxd
   │        │  │  ├─ lib
   │        │  │  │  └─ libnpyrandom.a
   │        │  │  ├─ mtrand.cpython-311-darwin.so
   │        │  │  ├─ mtrand.pyi
   │        │  │  └─ tests
   │        │  │     ├─ __init__.py
   │        │  │     ├─ __pycache__
   │        │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │     │  ├─ test_direct.cpython-311.pyc
   │        │  │     │  ├─ test_extending.cpython-311.pyc
   │        │  │     │  ├─ test_generator_mt19937.cpython-311.pyc
   │        │  │     │  ├─ test_generator_mt19937_regressions.cpython-311.pyc
   │        │  │     │  ├─ test_random.cpython-311.pyc
   │        │  │     │  ├─ test_randomstate.cpython-311.pyc
   │        │  │     │  ├─ test_randomstate_regression.cpython-311.pyc
   │        │  │     │  ├─ test_regression.cpython-311.pyc
   │        │  │     │  ├─ test_seed_sequence.cpython-311.pyc
   │        │  │     │  └─ test_smoke.cpython-311.pyc
   │        │  │     ├─ data
   │        │  │     │  ├─ __init__.py
   │        │  │     │  ├─ __pycache__
   │        │  │     │  │  └─ __init__.cpython-311.pyc
   │        │  │     │  ├─ generator_pcg64_np121.pkl.gz
   │        │  │     │  ├─ generator_pcg64_np126.pkl.gz
   │        │  │     │  ├─ mt19937-testset-1.csv
   │        │  │     │  ├─ mt19937-testset-2.csv
   │        │  │     │  ├─ pcg64-testset-1.csv
   │        │  │     │  ├─ pcg64-testset-2.csv
   │        │  │     │  ├─ pcg64dxsm-testset-1.csv
   │        │  │     │  ├─ pcg64dxsm-testset-2.csv
   │        │  │     │  ├─ philox-testset-1.csv
   │        │  │     │  ├─ philox-testset-2.csv
   │        │  │     │  ├─ sfc64-testset-1.csv
   │        │  │     │  ├─ sfc64-testset-2.csv
   │        │  │     │  └─ sfc64_np126.pkl.gz
   │        │  │     ├─ test_direct.py
   │        │  │     ├─ test_extending.py
   │        │  │     ├─ test_generator_mt19937.py
   │        │  │     ├─ test_generator_mt19937_regressions.py
   │        │  │     ├─ test_random.py
   │        │  │     ├─ test_randomstate.py
   │        │  │     ├─ test_randomstate_regression.py
   │        │  │     ├─ test_regression.py
   │        │  │     ├─ test_seed_sequence.py
   │        │  │     └─ test_smoke.py
   │        │  ├─ rec
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.pyi
   │        │  │  └─ __pycache__
   │        │  │     └─ __init__.cpython-311.pyc
   │        │  ├─ strings
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.pyi
   │        │  │  └─ __pycache__
   │        │  │     └─ __init__.cpython-311.pyc
   │        │  ├─ testing
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.pyi
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ overrides.cpython-311.pyc
   │        │  │  │  └─ print_coercion_tables.cpython-311.pyc
   │        │  │  ├─ _private
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.pyi
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ extbuild.cpython-311.pyc
   │        │  │  │  │  └─ utils.cpython-311.pyc
   │        │  │  │  ├─ extbuild.py
   │        │  │  │  ├─ extbuild.pyi
   │        │  │  │  ├─ utils.py
   │        │  │  │  └─ utils.pyi
   │        │  │  ├─ overrides.py
   │        │  │  ├─ overrides.pyi
   │        │  │  ├─ print_coercion_tables.py
   │        │  │  ├─ print_coercion_tables.pyi
   │        │  │  └─ tests
   │        │  │     ├─ __init__.py
   │        │  │     ├─ __pycache__
   │        │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │     │  └─ test_utils.cpython-311.pyc
   │        │  │     └─ test_utils.py
   │        │  ├─ tests
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ test__all__.cpython-311.pyc
   │        │  │  │  ├─ test_configtool.cpython-311.pyc
   │        │  │  │  ├─ test_ctypeslib.cpython-311.pyc
   │        │  │  │  ├─ test_lazyloading.cpython-311.pyc
   │        │  │  │  ├─ test_matlib.cpython-311.pyc
   │        │  │  │  ├─ test_numpy_config.cpython-311.pyc
   │        │  │  │  ├─ test_numpy_version.cpython-311.pyc
   │        │  │  │  ├─ test_public_api.cpython-311.pyc
   │        │  │  │  ├─ test_reloading.cpython-311.pyc
   │        │  │  │  ├─ test_scripts.cpython-311.pyc
   │        │  │  │  └─ test_warnings.cpython-311.pyc
   │        │  │  ├─ test__all__.py
   │        │  │  ├─ test_configtool.py
   │        │  │  ├─ test_ctypeslib.py
   │        │  │  ├─ test_lazyloading.py
   │        │  │  ├─ test_matlib.py
   │        │  │  ├─ test_numpy_config.py
   │        │  │  ├─ test_numpy_version.py
   │        │  │  ├─ test_public_api.py
   │        │  │  ├─ test_reloading.py
   │        │  │  ├─ test_scripts.py
   │        │  │  └─ test_warnings.py
   │        │  ├─ typing
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  └─ mypy_plugin.cpython-311.pyc
   │        │  │  ├─ mypy_plugin.py
   │        │  │  └─ tests
   │        │  │     ├─ __init__.py
   │        │  │     ├─ __pycache__
   │        │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │     │  ├─ test_isfile.cpython-311.pyc
   │        │  │     │  ├─ test_runtime.cpython-311.pyc
   │        │  │     │  └─ test_typing.cpython-311.pyc
   │        │  │     ├─ data
   │        │  │     │  ├─ fail
   │        │  │     │  │  ├─ arithmetic.pyi
   │        │  │     │  │  ├─ array_constructors.pyi
   │        │  │     │  │  ├─ array_like.pyi
   │        │  │     │  │  ├─ array_pad.pyi
   │        │  │     │  │  ├─ arrayprint.pyi
   │        │  │     │  │  ├─ arrayterator.pyi
   │        │  │     │  │  ├─ bitwise_ops.pyi
   │        │  │     │  │  ├─ char.pyi
   │        │  │     │  │  ├─ chararray.pyi
   │        │  │     │  │  ├─ comparisons.pyi
   │        │  │     │  │  ├─ constants.pyi
   │        │  │     │  │  ├─ datasource.pyi
   │        │  │     │  │  ├─ dtype.pyi
   │        │  │     │  │  ├─ einsumfunc.pyi
   │        │  │     │  │  ├─ flatiter.pyi
   │        │  │     │  │  ├─ fromnumeric.pyi
   │        │  │     │  │  ├─ histograms.pyi
   │        │  │     │  │  ├─ index_tricks.pyi
   │        │  │     │  │  ├─ lib_function_base.pyi
   │        │  │     │  │  ├─ lib_polynomial.pyi
   │        │  │     │  │  ├─ lib_utils.pyi
   │        │  │     │  │  ├─ lib_version.pyi
   │        │  │     │  │  ├─ linalg.pyi
   │        │  │     │  │  ├─ memmap.pyi
   │        │  │     │  │  ├─ modules.pyi
   │        │  │     │  │  ├─ multiarray.pyi
   │        │  │     │  │  ├─ ndarray.pyi
   │        │  │     │  │  ├─ ndarray_misc.pyi
   │        │  │     │  │  ├─ nditer.pyi
   │        │  │     │  │  ├─ nested_sequence.pyi
   │        │  │     │  │  ├─ npyio.pyi
   │        │  │     │  │  ├─ numerictypes.pyi
   │        │  │     │  │  ├─ random.pyi
   │        │  │     │  │  ├─ rec.pyi
   │        │  │     │  │  ├─ scalars.pyi
   │        │  │     │  │  ├─ shape.pyi
   │        │  │     │  │  ├─ shape_base.pyi
   │        │  │     │  │  ├─ stride_tricks.pyi
   │        │  │     │  │  ├─ strings.pyi
   │        │  │     │  │  ├─ testing.pyi
   │        │  │     │  │  ├─ twodim_base.pyi
   │        │  │     │  │  ├─ type_check.pyi
   │        │  │     │  │  ├─ ufunc_config.pyi
   │        │  │     │  │  ├─ ufunclike.pyi
   │        │  │     │  │  ├─ ufuncs.pyi
   │        │  │     │  │  └─ warnings_and_errors.pyi
   │        │  │     │  ├─ misc
   │        │  │     │  │  └─ extended_precision.pyi
   │        │  │     │  ├─ mypy.ini
   │        │  │     │  ├─ pass
   │        │  │     │  │  ├─ __pycache__
   │        │  │     │  │  │  ├─ arithmetic.cpython-311.pyc
   │        │  │     │  │  │  ├─ array_constructors.cpython-311.pyc
   │        │  │     │  │  │  ├─ array_like.cpython-311.pyc
   │        │  │     │  │  │  ├─ arrayprint.cpython-311.pyc
   │        │  │     │  │  │  ├─ arrayterator.cpython-311.pyc
   │        │  │     │  │  │  ├─ bitwise_ops.cpython-311.pyc
   │        │  │     │  │  │  ├─ comparisons.cpython-311.pyc
   │        │  │     │  │  │  ├─ dtype.cpython-311.pyc
   │        │  │     │  │  │  ├─ einsumfunc.cpython-311.pyc
   │        │  │     │  │  │  ├─ flatiter.cpython-311.pyc
   │        │  │     │  │  │  ├─ fromnumeric.cpython-311.pyc
   │        │  │     │  │  │  ├─ index_tricks.cpython-311.pyc
   │        │  │     │  │  │  ├─ lib_user_array.cpython-311.pyc
   │        │  │     │  │  │  ├─ lib_utils.cpython-311.pyc
   │        │  │     │  │  │  ├─ lib_version.cpython-311.pyc
   │        │  │     │  │  │  ├─ literal.cpython-311.pyc
   │        │  │     │  │  │  ├─ ma.cpython-311.pyc
   │        │  │     │  │  │  ├─ mod.cpython-311.pyc
   │        │  │     │  │  │  ├─ modules.cpython-311.pyc
   │        │  │     │  │  │  ├─ multiarray.cpython-311.pyc
   │        │  │     │  │  │  ├─ ndarray_conversion.cpython-311.pyc
   │        │  │     │  │  │  ├─ ndarray_misc.cpython-311.pyc
   │        │  │     │  │  │  ├─ ndarray_shape_manipulation.cpython-311.pyc
   │        │  │     │  │  │  ├─ nditer.cpython-311.pyc
   │        │  │     │  │  │  ├─ numeric.cpython-311.pyc
   │        │  │     │  │  │  ├─ numerictypes.cpython-311.pyc
   │        │  │     │  │  │  ├─ random.cpython-311.pyc
   │        │  │     │  │  │  ├─ recfunctions.cpython-311.pyc
   │        │  │     │  │  │  ├─ scalars.cpython-311.pyc
   │        │  │     │  │  │  ├─ shape.cpython-311.pyc
   │        │  │     │  │  │  ├─ simple.cpython-311.pyc
   │        │  │     │  │  │  ├─ simple_py3.cpython-311.pyc
   │        │  │     │  │  │  ├─ ufunc_config.cpython-311.pyc
   │        │  │     │  │  │  ├─ ufunclike.cpython-311.pyc
   │        │  │     │  │  │  ├─ ufuncs.cpython-311.pyc
   │        │  │     │  │  │  └─ warnings_and_errors.cpython-311.pyc
   │        │  │     │  │  ├─ arithmetic.py
   │        │  │     │  │  ├─ array_constructors.py
   │        │  │     │  │  ├─ array_like.py
   │        │  │     │  │  ├─ arrayprint.py
   │        │  │     │  │  ├─ arrayterator.py
   │        │  │     │  │  ├─ bitwise_ops.py
   │        │  │     │  │  ├─ comparisons.py
   │        │  │     │  │  ├─ dtype.py
   │        │  │     │  │  ├─ einsumfunc.py
   │        │  │     │  │  ├─ flatiter.py
   │        │  │     │  │  ├─ fromnumeric.py
   │        │  │     │  │  ├─ index_tricks.py
   │        │  │     │  │  ├─ lib_user_array.py
   │        │  │     │  │  ├─ lib_utils.py
   │        │  │     │  │  ├─ lib_version.py
   │        │  │     │  │  ├─ literal.py
   │        │  │     │  │  ├─ ma.py
   │        │  │     │  │  ├─ mod.py
   │        │  │     │  │  ├─ modules.py
   │        │  │     │  │  ├─ multiarray.py
   │        │  │     │  │  ├─ ndarray_conversion.py
   │        │  │     │  │  ├─ ndarray_misc.py
   │        │  │     │  │  ├─ ndarray_shape_manipulation.py
   │        │  │     │  │  ├─ nditer.py
   │        │  │     │  │  ├─ numeric.py
   │        │  │     │  │  ├─ numerictypes.py
   │        │  │     │  │  ├─ random.py
   │        │  │     │  │  ├─ recfunctions.py
   │        │  │     │  │  ├─ scalars.py
   │        │  │     │  │  ├─ shape.py
   │        │  │     │  │  ├─ simple.py
   │        │  │     │  │  ├─ simple_py3.py
   │        │  │     │  │  ├─ ufunc_config.py
   │        │  │     │  │  ├─ ufunclike.py
   │        │  │     │  │  ├─ ufuncs.py
   │        │  │     │  │  └─ warnings_and_errors.py
   │        │  │     │  └─ reveal
   │        │  │     │     ├─ arithmetic.pyi
   │        │  │     │     ├─ array_api_info.pyi
   │        │  │     │     ├─ array_constructors.pyi
   │        │  │     │     ├─ arraypad.pyi
   │        │  │     │     ├─ arrayprint.pyi
   │        │  │     │     ├─ arraysetops.pyi
   │        │  │     │     ├─ arrayterator.pyi
   │        │  │     │     ├─ bitwise_ops.pyi
   │        │  │     │     ├─ char.pyi
   │        │  │     │     ├─ chararray.pyi
   │        │  │     │     ├─ comparisons.pyi
   │        │  │     │     ├─ constants.pyi
   │        │  │     │     ├─ ctypeslib.pyi
   │        │  │     │     ├─ datasource.pyi
   │        │  │     │     ├─ dtype.pyi
   │        │  │     │     ├─ einsumfunc.pyi
   │        │  │     │     ├─ emath.pyi
   │        │  │     │     ├─ fft.pyi
   │        │  │     │     ├─ flatiter.pyi
   │        │  │     │     ├─ fromnumeric.pyi
   │        │  │     │     ├─ getlimits.pyi
   │        │  │     │     ├─ histograms.pyi
   │        │  │     │     ├─ index_tricks.pyi
   │        │  │     │     ├─ lib_function_base.pyi
   │        │  │     │     ├─ lib_polynomial.pyi
   │        │  │     │     ├─ lib_utils.pyi
   │        │  │     │     ├─ lib_version.pyi
   │        │  │     │     ├─ linalg.pyi
   │        │  │     │     ├─ matrix.pyi
   │        │  │     │     ├─ memmap.pyi
   │        │  │     │     ├─ mod.pyi
   │        │  │     │     ├─ modules.pyi
   │        │  │     │     ├─ multiarray.pyi
   │        │  │     │     ├─ nbit_base_example.pyi
   │        │  │     │     ├─ ndarray_assignability.pyi
   │        │  │     │     ├─ ndarray_conversion.pyi
   │        │  │     │     ├─ ndarray_misc.pyi
   │        │  │     │     ├─ ndarray_shape_manipulation.pyi
   │        │  │     │     ├─ nditer.pyi
   │        │  │     │     ├─ nested_sequence.pyi
   │        │  │     │     ├─ npyio.pyi
   │        │  │     │     ├─ numeric.pyi
   │        │  │     │     ├─ numerictypes.pyi
   │        │  │     │     ├─ polynomial_polybase.pyi
   │        │  │     │     ├─ polynomial_polyutils.pyi
   │        │  │     │     ├─ polynomial_series.pyi
   │        │  │     │     ├─ random.pyi
   │        │  │     │     ├─ rec.pyi
   │        │  │     │     ├─ scalars.pyi
   │        │  │     │     ├─ shape.pyi
   │        │  │     │     ├─ shape_base.pyi
   │        │  │     │     ├─ stride_tricks.pyi
   │        │  │     │     ├─ strings.pyi
   │        │  │     │     ├─ testing.pyi
   │        │  │     │     ├─ twodim_base.pyi
   │        │  │     │     ├─ type_check.pyi
   │        │  │     │     ├─ ufunc_config.pyi
   │        │  │     │     ├─ ufunclike.pyi
   │        │  │     │     ├─ ufuncs.pyi
   │        │  │     │     └─ warnings_and_errors.pyi
   │        │  │     ├─ test_isfile.py
   │        │  │     ├─ test_runtime.py
   │        │  │     └─ test_typing.py
   │        │  ├─ version.py
   │        │  └─ version.pyi
   │        ├─ numpy-2.2.6.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ LICENSE.txt
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  └─ entry_points.txt
   │        ├─ packaging
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ _elffile.cpython-311.pyc
   │        │  │  ├─ _manylinux.cpython-311.pyc
   │        │  │  ├─ _musllinux.cpython-311.pyc
   │        │  │  ├─ _parser.cpython-311.pyc
   │        │  │  ├─ _structures.cpython-311.pyc
   │        │  │  ├─ _tokenizer.cpython-311.pyc
   │        │  │  ├─ markers.cpython-311.pyc
   │        │  │  ├─ metadata.cpython-311.pyc
   │        │  │  ├─ requirements.cpython-311.pyc
   │        │  │  ├─ specifiers.cpython-311.pyc
   │        │  │  ├─ tags.cpython-311.pyc
   │        │  │  ├─ utils.cpython-311.pyc
   │        │  │  └─ version.cpython-311.pyc
   │        │  ├─ _elffile.py
   │        │  ├─ _manylinux.py
   │        │  ├─ _musllinux.py
   │        │  ├─ _parser.py
   │        │  ├─ _structures.py
   │        │  ├─ _tokenizer.py
   │        │  ├─ licenses
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  └─ _spdx.cpython-311.pyc
   │        │  │  └─ _spdx.py
   │        │  ├─ markers.py
   │        │  ├─ metadata.py
   │        │  ├─ py.typed
   │        │  ├─ requirements.py
   │        │  ├─ specifiers.py
   │        │  ├─ tags.py
   │        │  ├─ utils.py
   │        │  └─ version.py
   │        ├─ packaging-24.2.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ LICENSE
   │        │  ├─ LICENSE.APACHE
   │        │  ├─ LICENSE.BSD
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  └─ WHEEL
   │        ├─ pandas
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ _typing.cpython-311.pyc
   │        │  │  ├─ _version.cpython-311.pyc
   │        │  │  ├─ _version_meson.cpython-311.pyc
   │        │  │  ├─ conftest.cpython-311.pyc
   │        │  │  └─ testing.cpython-311.pyc
   │        │  ├─ _config
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ config.cpython-311.pyc
   │        │  │  │  ├─ dates.cpython-311.pyc
   │        │  │  │  ├─ display.cpython-311.pyc
   │        │  │  │  └─ localization.cpython-311.pyc
   │        │  │  ├─ config.py
   │        │  │  ├─ dates.py
   │        │  │  ├─ display.py
   │        │  │  └─ localization.py
   │        │  ├─ _libs
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  ├─ algos.cpython-311-darwin.so
   │        │  │  ├─ algos.pyi
   │        │  │  ├─ arrays.cpython-311-darwin.so
   │        │  │  ├─ arrays.pyi
   │        │  │  ├─ byteswap.cpython-311-darwin.so
   │        │  │  ├─ byteswap.pyi
   │        │  │  ├─ groupby.cpython-311-darwin.so
   │        │  │  ├─ groupby.pyi
   │        │  │  ├─ hashing.cpython-311-darwin.so
   │        │  │  ├─ hashing.pyi
   │        │  │  ├─ hashtable.cpython-311-darwin.so
   │        │  │  ├─ hashtable.pyi
   │        │  │  ├─ index.cpython-311-darwin.so
   │        │  │  ├─ index.pyi
   │        │  │  ├─ indexing.cpython-311-darwin.so
   │        │  │  ├─ indexing.pyi
   │        │  │  ├─ internals.cpython-311-darwin.so
   │        │  │  ├─ internals.pyi
   │        │  │  ├─ interval.cpython-311-darwin.so
   │        │  │  ├─ interval.pyi
   │        │  │  ├─ join.cpython-311-darwin.so
   │        │  │  ├─ join.pyi
   │        │  │  ├─ json.cpython-311-darwin.so
   │        │  │  ├─ json.pyi
   │        │  │  ├─ lib.cpython-311-darwin.so
   │        │  │  ├─ lib.pyi
   │        │  │  ├─ missing.cpython-311-darwin.so
   │        │  │  ├─ missing.pyi
   │        │  │  ├─ ops.cpython-311-darwin.so
   │        │  │  ├─ ops.pyi
   │        │  │  ├─ ops_dispatch.cpython-311-darwin.so
   │        │  │  ├─ ops_dispatch.pyi
   │        │  │  ├─ pandas_datetime.cpython-311-darwin.so
   │        │  │  ├─ pandas_parser.cpython-311-darwin.so
   │        │  │  ├─ parsers.cpython-311-darwin.so
   │        │  │  ├─ parsers.pyi
   │        │  │  ├─ properties.cpython-311-darwin.so
   │        │  │  ├─ properties.pyi
   │        │  │  ├─ reshape.cpython-311-darwin.so
   │        │  │  ├─ reshape.pyi
   │        │  │  ├─ sas.cpython-311-darwin.so
   │        │  │  ├─ sas.pyi
   │        │  │  ├─ sparse.cpython-311-darwin.so
   │        │  │  ├─ sparse.pyi
   │        │  │  ├─ testing.cpython-311-darwin.so
   │        │  │  ├─ testing.pyi
   │        │  │  ├─ tslib.cpython-311-darwin.so
   │        │  │  ├─ tslib.pyi
   │        │  │  ├─ tslibs
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  │  ├─ base.cpython-311-darwin.so
   │        │  │  │  ├─ ccalendar.cpython-311-darwin.so
   │        │  │  │  ├─ ccalendar.pyi
   │        │  │  │  ├─ conversion.cpython-311-darwin.so
   │        │  │  │  ├─ conversion.pyi
   │        │  │  │  ├─ dtypes.cpython-311-darwin.so
   │        │  │  │  ├─ dtypes.pyi
   │        │  │  │  ├─ fields.cpython-311-darwin.so
   │        │  │  │  ├─ fields.pyi
   │        │  │  │  ├─ nattype.cpython-311-darwin.so
   │        │  │  │  ├─ nattype.pyi
   │        │  │  │  ├─ np_datetime.cpython-311-darwin.so
   │        │  │  │  ├─ np_datetime.pyi
   │        │  │  │  ├─ offsets.cpython-311-darwin.so
   │        │  │  │  ├─ offsets.pyi
   │        │  │  │  ├─ parsing.cpython-311-darwin.so
   │        │  │  │  ├─ parsing.pyi
   │        │  │  │  ├─ period.cpython-311-darwin.so
   │        │  │  │  ├─ period.pyi
   │        │  │  │  ├─ strptime.cpython-311-darwin.so
   │        │  │  │  ├─ strptime.pyi
   │        │  │  │  ├─ timedeltas.cpython-311-darwin.so
   │        │  │  │  ├─ timedeltas.pyi
   │        │  │  │  ├─ timestamps.cpython-311-darwin.so
   │        │  │  │  ├─ timestamps.pyi
   │        │  │  │  ├─ timezones.cpython-311-darwin.so
   │        │  │  │  ├─ timezones.pyi
   │        │  │  │  ├─ tzconversion.cpython-311-darwin.so
   │        │  │  │  ├─ tzconversion.pyi
   │        │  │  │  ├─ vectorized.cpython-311-darwin.so
   │        │  │  │  └─ vectorized.pyi
   │        │  │  ├─ window
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  │  ├─ aggregations.cpython-311-darwin.so
   │        │  │  │  ├─ aggregations.pyi
   │        │  │  │  ├─ indexers.cpython-311-darwin.so
   │        │  │  │  └─ indexers.pyi
   │        │  │  ├─ writers.cpython-311-darwin.so
   │        │  │  └─ writers.pyi
   │        │  ├─ _testing
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _hypothesis.cpython-311.pyc
   │        │  │  │  ├─ _io.cpython-311.pyc
   │        │  │  │  ├─ _warnings.cpython-311.pyc
   │        │  │  │  ├─ asserters.cpython-311.pyc
   │        │  │  │  ├─ compat.cpython-311.pyc
   │        │  │  │  └─ contexts.cpython-311.pyc
   │        │  │  ├─ _hypothesis.py
   │        │  │  ├─ _io.py
   │        │  │  ├─ _warnings.py
   │        │  │  ├─ asserters.py
   │        │  │  ├─ compat.py
   │        │  │  └─ contexts.py
   │        │  ├─ _typing.py
   │        │  ├─ _version.py
   │        │  ├─ _version_meson.py
   │        │  ├─ api
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  ├─ extensions
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ indexers
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ interchange
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ types
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  └─ typing
   │        │  │     ├─ __init__.py
   │        │  │     └─ __pycache__
   │        │  │        └─ __init__.cpython-311.pyc
   │        │  ├─ arrays
   │        │  │  ├─ __init__.py
   │        │  │  └─ __pycache__
   │        │  │     └─ __init__.cpython-311.pyc
   │        │  ├─ compat
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _constants.cpython-311.pyc
   │        │  │  │  ├─ _optional.cpython-311.pyc
   │        │  │  │  ├─ compressors.cpython-311.pyc
   │        │  │  │  ├─ pickle_compat.cpython-311.pyc
   │        │  │  │  └─ pyarrow.cpython-311.pyc
   │        │  │  ├─ _constants.py
   │        │  │  ├─ _optional.py
   │        │  │  ├─ compressors.py
   │        │  │  ├─ numpy
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  └─ function.cpython-311.pyc
   │        │  │  │  └─ function.py
   │        │  │  ├─ pickle_compat.py
   │        │  │  └─ pyarrow.py
   │        │  ├─ conftest.py
   │        │  ├─ core
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ accessor.cpython-311.pyc
   │        │  │  │  ├─ algorithms.cpython-311.pyc
   │        │  │  │  ├─ api.cpython-311.pyc
   │        │  │  │  ├─ apply.cpython-311.pyc
   │        │  │  │  ├─ arraylike.cpython-311.pyc
   │        │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  ├─ common.cpython-311.pyc
   │        │  │  │  ├─ config_init.cpython-311.pyc
   │        │  │  │  ├─ construction.cpython-311.pyc
   │        │  │  │  ├─ flags.cpython-311.pyc
   │        │  │  │  ├─ frame.cpython-311.pyc
   │        │  │  │  ├─ generic.cpython-311.pyc
   │        │  │  │  ├─ indexing.cpython-311.pyc
   │        │  │  │  ├─ missing.cpython-311.pyc
   │        │  │  │  ├─ nanops.cpython-311.pyc
   │        │  │  │  ├─ resample.cpython-311.pyc
   │        │  │  │  ├─ roperator.cpython-311.pyc
   │        │  │  │  ├─ sample.cpython-311.pyc
   │        │  │  │  ├─ series.cpython-311.pyc
   │        │  │  │  ├─ shared_docs.cpython-311.pyc
   │        │  │  │  └─ sorting.cpython-311.pyc
   │        │  │  ├─ _numba
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ executor.cpython-311.pyc
   │        │  │  │  │  └─ extensions.cpython-311.pyc
   │        │  │  │  ├─ executor.py
   │        │  │  │  ├─ extensions.py
   │        │  │  │  └─ kernels
   │        │  │  │     ├─ __init__.py
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │     │  ├─ mean_.cpython-311.pyc
   │        │  │  │     │  ├─ min_max_.cpython-311.pyc
   │        │  │  │     │  ├─ shared.cpython-311.pyc
   │        │  │  │     │  ├─ sum_.cpython-311.pyc
   │        │  │  │     │  └─ var_.cpython-311.pyc
   │        │  │  │     ├─ mean_.py
   │        │  │  │     ├─ min_max_.py
   │        │  │  │     ├─ shared.py
   │        │  │  │     ├─ sum_.py
   │        │  │  │     └─ var_.py
   │        │  │  ├─ accessor.py
   │        │  │  ├─ algorithms.py
   │        │  │  ├─ api.py
   │        │  │  ├─ apply.py
   │        │  │  ├─ array_algos
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ datetimelike_accumulations.cpython-311.pyc
   │        │  │  │  │  ├─ masked_accumulations.cpython-311.pyc
   │        │  │  │  │  ├─ masked_reductions.cpython-311.pyc
   │        │  │  │  │  ├─ putmask.cpython-311.pyc
   │        │  │  │  │  ├─ quantile.cpython-311.pyc
   │        │  │  │  │  ├─ replace.cpython-311.pyc
   │        │  │  │  │  ├─ take.cpython-311.pyc
   │        │  │  │  │  └─ transforms.cpython-311.pyc
   │        │  │  │  ├─ datetimelike_accumulations.py
   │        │  │  │  ├─ masked_accumulations.py
   │        │  │  │  ├─ masked_reductions.py
   │        │  │  │  ├─ putmask.py
   │        │  │  │  ├─ quantile.py
   │        │  │  │  ├─ replace.py
   │        │  │  │  ├─ take.py
   │        │  │  │  └─ transforms.py
   │        │  │  ├─ arraylike.py
   │        │  │  ├─ arrays
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ _arrow_string_mixins.cpython-311.pyc
   │        │  │  │  │  ├─ _mixins.cpython-311.pyc
   │        │  │  │  │  ├─ _ranges.cpython-311.pyc
   │        │  │  │  │  ├─ _utils.cpython-311.pyc
   │        │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  ├─ boolean.cpython-311.pyc
   │        │  │  │  │  ├─ categorical.cpython-311.pyc
   │        │  │  │  │  ├─ datetimelike.cpython-311.pyc
   │        │  │  │  │  ├─ datetimes.cpython-311.pyc
   │        │  │  │  │  ├─ floating.cpython-311.pyc
   │        │  │  │  │  ├─ integer.cpython-311.pyc
   │        │  │  │  │  ├─ interval.cpython-311.pyc
   │        │  │  │  │  ├─ masked.cpython-311.pyc
   │        │  │  │  │  ├─ numeric.cpython-311.pyc
   │        │  │  │  │  ├─ numpy_.cpython-311.pyc
   │        │  │  │  │  ├─ period.cpython-311.pyc
   │        │  │  │  │  ├─ string_.cpython-311.pyc
   │        │  │  │  │  ├─ string_arrow.cpython-311.pyc
   │        │  │  │  │  └─ timedeltas.cpython-311.pyc
   │        │  │  │  ├─ _arrow_string_mixins.py
   │        │  │  │  ├─ _mixins.py
   │        │  │  │  ├─ _ranges.py
   │        │  │  │  ├─ _utils.py
   │        │  │  │  ├─ arrow
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ _arrow_utils.cpython-311.pyc
   │        │  │  │  │  │  ├─ accessors.cpython-311.pyc
   │        │  │  │  │  │  ├─ array.cpython-311.pyc
   │        │  │  │  │  │  └─ extension_types.cpython-311.pyc
   │        │  │  │  │  ├─ _arrow_utils.py
   │        │  │  │  │  ├─ accessors.py
   │        │  │  │  │  ├─ array.py
   │        │  │  │  │  └─ extension_types.py
   │        │  │  │  ├─ base.py
   │        │  │  │  ├─ boolean.py
   │        │  │  │  ├─ categorical.py
   │        │  │  │  ├─ datetimelike.py
   │        │  │  │  ├─ datetimes.py
   │        │  │  │  ├─ floating.py
   │        │  │  │  ├─ integer.py
   │        │  │  │  ├─ interval.py
   │        │  │  │  ├─ masked.py
   │        │  │  │  ├─ numeric.py
   │        │  │  │  ├─ numpy_.py
   │        │  │  │  ├─ period.py
   │        │  │  │  ├─ sparse
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ accessor.cpython-311.pyc
   │        │  │  │  │  │  ├─ array.cpython-311.pyc
   │        │  │  │  │  │  └─ scipy_sparse.cpython-311.pyc
   │        │  │  │  │  ├─ accessor.py
   │        │  │  │  │  ├─ array.py
   │        │  │  │  │  └─ scipy_sparse.py
   │        │  │  │  ├─ string_.py
   │        │  │  │  ├─ string_arrow.py
   │        │  │  │  └─ timedeltas.py
   │        │  │  ├─ base.py
   │        │  │  ├─ common.py
   │        │  │  ├─ computation
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ align.cpython-311.pyc
   │        │  │  │  │  ├─ api.cpython-311.pyc
   │        │  │  │  │  ├─ check.cpython-311.pyc
   │        │  │  │  │  ├─ common.cpython-311.pyc
   │        │  │  │  │  ├─ engines.cpython-311.pyc
   │        │  │  │  │  ├─ eval.cpython-311.pyc
   │        │  │  │  │  ├─ expr.cpython-311.pyc
   │        │  │  │  │  ├─ expressions.cpython-311.pyc
   │        │  │  │  │  ├─ ops.cpython-311.pyc
   │        │  │  │  │  ├─ parsing.cpython-311.pyc
   │        │  │  │  │  ├─ pytables.cpython-311.pyc
   │        │  │  │  │  └─ scope.cpython-311.pyc
   │        │  │  │  ├─ align.py
   │        │  │  │  ├─ api.py
   │        │  │  │  ├─ check.py
   │        │  │  │  ├─ common.py
   │        │  │  │  ├─ engines.py
   │        │  │  │  ├─ eval.py
   │        │  │  │  ├─ expr.py
   │        │  │  │  ├─ expressions.py
   │        │  │  │  ├─ ops.py
   │        │  │  │  ├─ parsing.py
   │        │  │  │  ├─ pytables.py
   │        │  │  │  └─ scope.py
   │        │  │  ├─ config_init.py
   │        │  │  ├─ construction.py
   │        │  │  ├─ dtypes
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ api.cpython-311.pyc
   │        │  │  │  │  ├─ astype.cpython-311.pyc
   │        │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  ├─ cast.cpython-311.pyc
   │        │  │  │  │  ├─ common.cpython-311.pyc
   │        │  │  │  │  ├─ concat.cpython-311.pyc
   │        │  │  │  │  ├─ dtypes.cpython-311.pyc
   │        │  │  │  │  ├─ generic.cpython-311.pyc
   │        │  │  │  │  ├─ inference.cpython-311.pyc
   │        │  │  │  │  └─ missing.cpython-311.pyc
   │        │  │  │  ├─ api.py
   │        │  │  │  ├─ astype.py
   │        │  │  │  ├─ base.py
   │        │  │  │  ├─ cast.py
   │        │  │  │  ├─ common.py
   │        │  │  │  ├─ concat.py
   │        │  │  │  ├─ dtypes.py
   │        │  │  │  ├─ generic.py
   │        │  │  │  ├─ inference.py
   │        │  │  │  └─ missing.py
   │        │  │  ├─ flags.py
   │        │  │  ├─ frame.py
   │        │  │  ├─ generic.py
   │        │  │  ├─ groupby
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  ├─ categorical.cpython-311.pyc
   │        │  │  │  │  ├─ generic.cpython-311.pyc
   │        │  │  │  │  ├─ groupby.cpython-311.pyc
   │        │  │  │  │  ├─ grouper.cpython-311.pyc
   │        │  │  │  │  ├─ indexing.cpython-311.pyc
   │        │  │  │  │  ├─ numba_.cpython-311.pyc
   │        │  │  │  │  └─ ops.cpython-311.pyc
   │        │  │  │  ├─ base.py
   │        │  │  │  ├─ categorical.py
   │        │  │  │  ├─ generic.py
   │        │  │  │  ├─ groupby.py
   │        │  │  │  ├─ grouper.py
   │        │  │  │  ├─ indexing.py
   │        │  │  │  ├─ numba_.py
   │        │  │  │  └─ ops.py
   │        │  │  ├─ indexers
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ objects.cpython-311.pyc
   │        │  │  │  │  └─ utils.cpython-311.pyc
   │        │  │  │  ├─ objects.py
   │        │  │  │  └─ utils.py
   │        │  │  ├─ indexes
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ accessors.cpython-311.pyc
   │        │  │  │  │  ├─ api.cpython-311.pyc
   │        │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  ├─ category.cpython-311.pyc
   │        │  │  │  │  ├─ datetimelike.cpython-311.pyc
   │        │  │  │  │  ├─ datetimes.cpython-311.pyc
   │        │  │  │  │  ├─ extension.cpython-311.pyc
   │        │  │  │  │  ├─ frozen.cpython-311.pyc
   │        │  │  │  │  ├─ interval.cpython-311.pyc
   │        │  │  │  │  ├─ multi.cpython-311.pyc
   │        │  │  │  │  ├─ period.cpython-311.pyc
   │        │  │  │  │  ├─ range.cpython-311.pyc
   │        │  │  │  │  └─ timedeltas.cpython-311.pyc
   │        │  │  │  ├─ accessors.py
   │        │  │  │  ├─ api.py
   │        │  │  │  ├─ base.py
   │        │  │  │  ├─ category.py
   │        │  │  │  ├─ datetimelike.py
   │        │  │  │  ├─ datetimes.py
   │        │  │  │  ├─ extension.py
   │        │  │  │  ├─ frozen.py
   │        │  │  │  ├─ interval.py
   │        │  │  │  ├─ multi.py
   │        │  │  │  ├─ period.py
   │        │  │  │  ├─ range.py
   │        │  │  │  └─ timedeltas.py
   │        │  │  ├─ indexing.py
   │        │  │  ├─ interchange
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ buffer.cpython-311.pyc
   │        │  │  │  │  ├─ column.cpython-311.pyc
   │        │  │  │  │  ├─ dataframe.cpython-311.pyc
   │        │  │  │  │  ├─ dataframe_protocol.cpython-311.pyc
   │        │  │  │  │  ├─ from_dataframe.cpython-311.pyc
   │        │  │  │  │  └─ utils.cpython-311.pyc
   │        │  │  │  ├─ buffer.py
   │        │  │  │  ├─ column.py
   │        │  │  │  ├─ dataframe.py
   │        │  │  │  ├─ dataframe_protocol.py
   │        │  │  │  ├─ from_dataframe.py
   │        │  │  │  └─ utils.py
   │        │  │  ├─ internals
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ api.cpython-311.pyc
   │        │  │  │  │  ├─ array_manager.cpython-311.pyc
   │        │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  ├─ blocks.cpython-311.pyc
   │        │  │  │  │  ├─ concat.cpython-311.pyc
   │        │  │  │  │  ├─ construction.cpython-311.pyc
   │        │  │  │  │  ├─ managers.cpython-311.pyc
   │        │  │  │  │  └─ ops.cpython-311.pyc
   │        │  │  │  ├─ api.py
   │        │  │  │  ├─ array_manager.py
   │        │  │  │  ├─ base.py
   │        │  │  │  ├─ blocks.py
   │        │  │  │  ├─ concat.py
   │        │  │  │  ├─ construction.py
   │        │  │  │  ├─ managers.py
   │        │  │  │  └─ ops.py
   │        │  │  ├─ methods
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ describe.cpython-311.pyc
   │        │  │  │  │  ├─ selectn.cpython-311.pyc
   │        │  │  │  │  └─ to_dict.cpython-311.pyc
   │        │  │  │  ├─ describe.py
   │        │  │  │  ├─ selectn.py
   │        │  │  │  └─ to_dict.py
   │        │  │  ├─ missing.py
   │        │  │  ├─ nanops.py
   │        │  │  ├─ ops
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ array_ops.cpython-311.pyc
   │        │  │  │  │  ├─ common.cpython-311.pyc
   │        │  │  │  │  ├─ dispatch.cpython-311.pyc
   │        │  │  │  │  ├─ docstrings.cpython-311.pyc
   │        │  │  │  │  ├─ invalid.cpython-311.pyc
   │        │  │  │  │  ├─ mask_ops.cpython-311.pyc
   │        │  │  │  │  └─ missing.cpython-311.pyc
   │        │  │  │  ├─ array_ops.py
   │        │  │  │  ├─ common.py
   │        │  │  │  ├─ dispatch.py
   │        │  │  │  ├─ docstrings.py
   │        │  │  │  ├─ invalid.py
   │        │  │  │  ├─ mask_ops.py
   │        │  │  │  └─ missing.py
   │        │  │  ├─ resample.py
   │        │  │  ├─ reshape
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ api.cpython-311.pyc
   │        │  │  │  │  ├─ concat.cpython-311.pyc
   │        │  │  │  │  ├─ encoding.cpython-311.pyc
   │        │  │  │  │  ├─ melt.cpython-311.pyc
   │        │  │  │  │  ├─ merge.cpython-311.pyc
   │        │  │  │  │  ├─ pivot.cpython-311.pyc
   │        │  │  │  │  ├─ reshape.cpython-311.pyc
   │        │  │  │  │  ├─ tile.cpython-311.pyc
   │        │  │  │  │  └─ util.cpython-311.pyc
   │        │  │  │  ├─ api.py
   │        │  │  │  ├─ concat.py
   │        │  │  │  ├─ encoding.py
   │        │  │  │  ├─ melt.py
   │        │  │  │  ├─ merge.py
   │        │  │  │  ├─ pivot.py
   │        │  │  │  ├─ reshape.py
   │        │  │  │  ├─ tile.py
   │        │  │  │  └─ util.py
   │        │  │  ├─ roperator.py
   │        │  │  ├─ sample.py
   │        │  │  ├─ series.py
   │        │  │  ├─ shared_docs.py
   │        │  │  ├─ sorting.py
   │        │  │  ├─ sparse
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  └─ api.cpython-311.pyc
   │        │  │  │  └─ api.py
   │        │  │  ├─ strings
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ accessor.cpython-311.pyc
   │        │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  └─ object_array.cpython-311.pyc
   │        │  │  │  ├─ accessor.py
   │        │  │  │  ├─ base.py
   │        │  │  │  └─ object_array.py
   │        │  │  ├─ tools
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ datetimes.cpython-311.pyc
   │        │  │  │  │  ├─ numeric.cpython-311.pyc
   │        │  │  │  │  ├─ timedeltas.cpython-311.pyc
   │        │  │  │  │  └─ times.cpython-311.pyc
   │        │  │  │  ├─ datetimes.py
   │        │  │  │  ├─ numeric.py
   │        │  │  │  ├─ timedeltas.py
   │        │  │  │  └─ times.py
   │        │  │  ├─ util
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ hashing.cpython-311.pyc
   │        │  │  │  │  └─ numba_.cpython-311.pyc
   │        │  │  │  ├─ hashing.py
   │        │  │  │  └─ numba_.py
   │        │  │  └─ window
   │        │  │     ├─ __init__.py
   │        │  │     ├─ __pycache__
   │        │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │     │  ├─ common.cpython-311.pyc
   │        │  │     │  ├─ doc.cpython-311.pyc
   │        │  │     │  ├─ ewm.cpython-311.pyc
   │        │  │     │  ├─ expanding.cpython-311.pyc
   │        │  │     │  ├─ numba_.cpython-311.pyc
   │        │  │     │  ├─ online.cpython-311.pyc
   │        │  │     │  └─ rolling.cpython-311.pyc
   │        │  │     ├─ common.py
   │        │  │     ├─ doc.py
   │        │  │     ├─ ewm.py
   │        │  │     ├─ expanding.py
   │        │  │     ├─ numba_.py
   │        │  │     ├─ online.py
   │        │  │     └─ rolling.py
   │        │  ├─ errors
   │        │  │  ├─ __init__.py
   │        │  │  └─ __pycache__
   │        │  │     └─ __init__.cpython-311.pyc
   │        │  ├─ io
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _util.cpython-311.pyc
   │        │  │  │  ├─ api.cpython-311.pyc
   │        │  │  │  ├─ clipboards.cpython-311.pyc
   │        │  │  │  ├─ common.cpython-311.pyc
   │        │  │  │  ├─ feather_format.cpython-311.pyc
   │        │  │  │  ├─ gbq.cpython-311.pyc
   │        │  │  │  ├─ html.cpython-311.pyc
   │        │  │  │  ├─ orc.cpython-311.pyc
   │        │  │  │  ├─ parquet.cpython-311.pyc
   │        │  │  │  ├─ pickle.cpython-311.pyc
   │        │  │  │  ├─ pytables.cpython-311.pyc
   │        │  │  │  ├─ spss.cpython-311.pyc
   │        │  │  │  ├─ sql.cpython-311.pyc
   │        │  │  │  ├─ stata.cpython-311.pyc
   │        │  │  │  └─ xml.cpython-311.pyc
   │        │  │  ├─ _util.py
   │        │  │  ├─ api.py
   │        │  │  ├─ clipboard
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ clipboards.py
   │        │  │  ├─ common.py
   │        │  │  ├─ excel
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ _base.cpython-311.pyc
   │        │  │  │  │  ├─ _calamine.cpython-311.pyc
   │        │  │  │  │  ├─ _odfreader.cpython-311.pyc
   │        │  │  │  │  ├─ _odswriter.cpython-311.pyc
   │        │  │  │  │  ├─ _openpyxl.cpython-311.pyc
   │        │  │  │  │  ├─ _pyxlsb.cpython-311.pyc
   │        │  │  │  │  ├─ _util.cpython-311.pyc
   │        │  │  │  │  ├─ _xlrd.cpython-311.pyc
   │        │  │  │  │  └─ _xlsxwriter.cpython-311.pyc
   │        │  │  │  ├─ _base.py
   │        │  │  │  ├─ _calamine.py
   │        │  │  │  ├─ _odfreader.py
   │        │  │  │  ├─ _odswriter.py
   │        │  │  │  ├─ _openpyxl.py
   │        │  │  │  ├─ _pyxlsb.py
   │        │  │  │  ├─ _util.py
   │        │  │  │  ├─ _xlrd.py
   │        │  │  │  └─ _xlsxwriter.py
   │        │  │  ├─ feather_format.py
   │        │  │  ├─ formats
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ _color_data.cpython-311.pyc
   │        │  │  │  │  ├─ console.cpython-311.pyc
   │        │  │  │  │  ├─ css.cpython-311.pyc
   │        │  │  │  │  ├─ csvs.cpython-311.pyc
   │        │  │  │  │  ├─ excel.cpython-311.pyc
   │        │  │  │  │  ├─ format.cpython-311.pyc
   │        │  │  │  │  ├─ html.cpython-311.pyc
   │        │  │  │  │  ├─ info.cpython-311.pyc
   │        │  │  │  │  ├─ printing.cpython-311.pyc
   │        │  │  │  │  ├─ string.cpython-311.pyc
   │        │  │  │  │  ├─ style.cpython-311.pyc
   │        │  │  │  │  ├─ style_render.cpython-311.pyc
   │        │  │  │  │  └─ xml.cpython-311.pyc
   │        │  │  │  ├─ _color_data.py
   │        │  │  │  ├─ console.py
   │        │  │  │  ├─ css.py
   │        │  │  │  ├─ csvs.py
   │        │  │  │  ├─ excel.py
   │        │  │  │  ├─ format.py
   │        │  │  │  ├─ html.py
   │        │  │  │  ├─ info.py
   │        │  │  │  ├─ printing.py
   │        │  │  │  ├─ string.py
   │        │  │  │  ├─ style.py
   │        │  │  │  ├─ style_render.py
   │        │  │  │  ├─ templates
   │        │  │  │  │  ├─ html.tpl
   │        │  │  │  │  ├─ html_style.tpl
   │        │  │  │  │  ├─ html_table.tpl
   │        │  │  │  │  ├─ latex.tpl
   │        │  │  │  │  ├─ latex_longtable.tpl
   │        │  │  │  │  ├─ latex_table.tpl
   │        │  │  │  │  └─ string.tpl
   │        │  │  │  └─ xml.py
   │        │  │  ├─ gbq.py
   │        │  │  ├─ html.py
   │        │  │  ├─ json
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ _json.cpython-311.pyc
   │        │  │  │  │  ├─ _normalize.cpython-311.pyc
   │        │  │  │  │  └─ _table_schema.cpython-311.pyc
   │        │  │  │  ├─ _json.py
   │        │  │  │  ├─ _normalize.py
   │        │  │  │  └─ _table_schema.py
   │        │  │  ├─ orc.py
   │        │  │  ├─ parquet.py
   │        │  │  ├─ parsers
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ arrow_parser_wrapper.cpython-311.pyc
   │        │  │  │  │  ├─ base_parser.cpython-311.pyc
   │        │  │  │  │  ├─ c_parser_wrapper.cpython-311.pyc
   │        │  │  │  │  ├─ python_parser.cpython-311.pyc
   │        │  │  │  │  └─ readers.cpython-311.pyc
   │        │  │  │  ├─ arrow_parser_wrapper.py
   │        │  │  │  ├─ base_parser.py
   │        │  │  │  ├─ c_parser_wrapper.py
   │        │  │  │  ├─ python_parser.py
   │        │  │  │  └─ readers.py
   │        │  │  ├─ pickle.py
   │        │  │  ├─ pytables.py
   │        │  │  ├─ sas
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ sas7bdat.cpython-311.pyc
   │        │  │  │  │  ├─ sas_constants.cpython-311.pyc
   │        │  │  │  │  ├─ sas_xport.cpython-311.pyc
   │        │  │  │  │  └─ sasreader.cpython-311.pyc
   │        │  │  │  ├─ sas7bdat.py
   │        │  │  │  ├─ sas_constants.py
   │        │  │  │  ├─ sas_xport.py
   │        │  │  │  └─ sasreader.py
   │        │  │  ├─ spss.py
   │        │  │  ├─ sql.py
   │        │  │  ├─ stata.py
   │        │  │  └─ xml.py
   │        │  ├─ plotting
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _core.cpython-311.pyc
   │        │  │  │  └─ _misc.cpython-311.pyc
   │        │  │  ├─ _core.py
   │        │  │  ├─ _matplotlib
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ boxplot.cpython-311.pyc
   │        │  │  │  │  ├─ converter.cpython-311.pyc
   │        │  │  │  │  ├─ core.cpython-311.pyc
   │        │  │  │  │  ├─ groupby.cpython-311.pyc
   │        │  │  │  │  ├─ hist.cpython-311.pyc
   │        │  │  │  │  ├─ misc.cpython-311.pyc
   │        │  │  │  │  ├─ style.cpython-311.pyc
   │        │  │  │  │  ├─ timeseries.cpython-311.pyc
   │        │  │  │  │  └─ tools.cpython-311.pyc
   │        │  │  │  ├─ boxplot.py
   │        │  │  │  ├─ converter.py
   │        │  │  │  ├─ core.py
   │        │  │  │  ├─ groupby.py
   │        │  │  │  ├─ hist.py
   │        │  │  │  ├─ misc.py
   │        │  │  │  ├─ style.py
   │        │  │  │  ├─ timeseries.py
   │        │  │  │  └─ tools.py
   │        │  │  └─ _misc.py
   │        │  ├─ pyproject.toml
   │        │  ├─ testing.py
   │        │  ├─ tests
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ test_aggregation.cpython-311.pyc
   │        │  │  │  ├─ test_algos.cpython-311.pyc
   │        │  │  │  ├─ test_common.cpython-311.pyc
   │        │  │  │  ├─ test_downstream.cpython-311.pyc
   │        │  │  │  ├─ test_errors.cpython-311.pyc
   │        │  │  │  ├─ test_expressions.cpython-311.pyc
   │        │  │  │  ├─ test_flags.cpython-311.pyc
   │        │  │  │  ├─ test_multilevel.cpython-311.pyc
   │        │  │  │  ├─ test_nanops.cpython-311.pyc
   │        │  │  │  ├─ test_optional_dependency.cpython-311.pyc
   │        │  │  │  ├─ test_register_accessor.cpython-311.pyc
   │        │  │  │  ├─ test_sorting.cpython-311.pyc
   │        │  │  │  └─ test_take.cpython-311.pyc
   │        │  │  ├─ api
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test_api.cpython-311.pyc
   │        │  │  │  │  └─ test_types.cpython-311.pyc
   │        │  │  │  ├─ test_api.py
   │        │  │  │  └─ test_types.py
   │        │  │  ├─ apply
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ common.cpython-311.pyc
   │        │  │  │  │  ├─ test_frame_apply.cpython-311.pyc
   │        │  │  │  │  ├─ test_frame_apply_relabeling.cpython-311.pyc
   │        │  │  │  │  ├─ test_frame_transform.cpython-311.pyc
   │        │  │  │  │  ├─ test_invalid_arg.cpython-311.pyc
   │        │  │  │  │  ├─ test_numba.cpython-311.pyc
   │        │  │  │  │  ├─ test_series_apply.cpython-311.pyc
   │        │  │  │  │  ├─ test_series_apply_relabeling.cpython-311.pyc
   │        │  │  │  │  ├─ test_series_transform.cpython-311.pyc
   │        │  │  │  │  └─ test_str.cpython-311.pyc
   │        │  │  │  ├─ common.py
   │        │  │  │  ├─ test_frame_apply.py
   │        │  │  │  ├─ test_frame_apply_relabeling.py
   │        │  │  │  ├─ test_frame_transform.py
   │        │  │  │  ├─ test_invalid_arg.py
   │        │  │  │  ├─ test_numba.py
   │        │  │  │  ├─ test_series_apply.py
   │        │  │  │  ├─ test_series_apply_relabeling.py
   │        │  │  │  ├─ test_series_transform.py
   │        │  │  │  └─ test_str.py
   │        │  │  ├─ arithmetic
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ common.cpython-311.pyc
   │        │  │  │  │  ├─ conftest.cpython-311.pyc
   │        │  │  │  │  ├─ test_array_ops.cpython-311.pyc
   │        │  │  │  │  ├─ test_categorical.cpython-311.pyc
   │        │  │  │  │  ├─ test_datetime64.cpython-311.pyc
   │        │  │  │  │  ├─ test_interval.cpython-311.pyc
   │        │  │  │  │  ├─ test_numeric.cpython-311.pyc
   │        │  │  │  │  ├─ test_object.cpython-311.pyc
   │        │  │  │  │  ├─ test_period.cpython-311.pyc
   │        │  │  │  │  └─ test_timedelta64.cpython-311.pyc
   │        │  │  │  ├─ common.py
   │        │  │  │  ├─ conftest.py
   │        │  │  │  ├─ test_array_ops.py
   │        │  │  │  ├─ test_categorical.py
   │        │  │  │  ├─ test_datetime64.py
   │        │  │  │  ├─ test_interval.py
   │        │  │  │  ├─ test_numeric.py
   │        │  │  │  ├─ test_object.py
   │        │  │  │  ├─ test_period.py
   │        │  │  │  └─ test_timedelta64.py
   │        │  │  ├─ arrays
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ masked_shared.cpython-311.pyc
   │        │  │  │  │  ├─ test_array.cpython-311.pyc
   │        │  │  │  │  ├─ test_datetimelike.cpython-311.pyc
   │        │  │  │  │  ├─ test_datetimes.cpython-311.pyc
   │        │  │  │  │  ├─ test_ndarray_backed.cpython-311.pyc
   │        │  │  │  │  ├─ test_period.cpython-311.pyc
   │        │  │  │  │  └─ test_timedeltas.cpython-311.pyc
   │        │  │  │  ├─ boolean
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_arithmetic.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_astype.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_comparison.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_construction.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_function.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_logical.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_ops.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_reduction.cpython-311.pyc
   │        │  │  │  │  │  └─ test_repr.cpython-311.pyc
   │        │  │  │  │  ├─ test_arithmetic.py
   │        │  │  │  │  ├─ test_astype.py
   │        │  │  │  │  ├─ test_comparison.py
   │        │  │  │  │  ├─ test_construction.py
   │        │  │  │  │  ├─ test_function.py
   │        │  │  │  │  ├─ test_indexing.py
   │        │  │  │  │  ├─ test_logical.py
   │        │  │  │  │  ├─ test_ops.py
   │        │  │  │  │  ├─ test_reduction.py
   │        │  │  │  │  └─ test_repr.py
   │        │  │  │  ├─ categorical
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_algos.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_analytics.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_api.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_astype.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_constructors.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_dtypes.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_map.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_missing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_operators.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_replace.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_repr.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_sorting.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_subclass.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_take.cpython-311.pyc
   │        │  │  │  │  │  └─ test_warnings.cpython-311.pyc
   │        │  │  │  │  ├─ test_algos.py
   │        │  │  │  │  ├─ test_analytics.py
   │        │  │  │  │  ├─ test_api.py
   │        │  │  │  │  ├─ test_astype.py
   │        │  │  │  │  ├─ test_constructors.py
   │        │  │  │  │  ├─ test_dtypes.py
   │        │  │  │  │  ├─ test_indexing.py
   │        │  │  │  │  ├─ test_map.py
   │        │  │  │  │  ├─ test_missing.py
   │        │  │  │  │  ├─ test_operators.py
   │        │  │  │  │  ├─ test_replace.py
   │        │  │  │  │  ├─ test_repr.py
   │        │  │  │  │  ├─ test_sorting.py
   │        │  │  │  │  ├─ test_subclass.py
   │        │  │  │  │  ├─ test_take.py
   │        │  │  │  │  └─ test_warnings.py
   │        │  │  │  ├─ datetimes
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_constructors.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_cumulative.cpython-311.pyc
   │        │  │  │  │  │  └─ test_reductions.cpython-311.pyc
   │        │  │  │  │  ├─ test_constructors.py
   │        │  │  │  │  ├─ test_cumulative.py
   │        │  │  │  │  └─ test_reductions.py
   │        │  │  │  ├─ floating
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ conftest.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_arithmetic.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_astype.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_comparison.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_concat.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_construction.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_contains.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_function.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_repr.cpython-311.pyc
   │        │  │  │  │  │  └─ test_to_numpy.cpython-311.pyc
   │        │  │  │  │  ├─ conftest.py
   │        │  │  │  │  ├─ test_arithmetic.py
   │        │  │  │  │  ├─ test_astype.py
   │        │  │  │  │  ├─ test_comparison.py
   │        │  │  │  │  ├─ test_concat.py
   │        │  │  │  │  ├─ test_construction.py
   │        │  │  │  │  ├─ test_contains.py
   │        │  │  │  │  ├─ test_function.py
   │        │  │  │  │  ├─ test_repr.py
   │        │  │  │  │  └─ test_to_numpy.py
   │        │  │  │  ├─ integer
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ conftest.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_arithmetic.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_comparison.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_concat.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_construction.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_dtypes.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_function.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_reduction.cpython-311.pyc
   │        │  │  │  │  │  └─ test_repr.cpython-311.pyc
   │        │  │  │  │  ├─ conftest.py
   │        │  │  │  │  ├─ test_arithmetic.py
   │        │  │  │  │  ├─ test_comparison.py
   │        │  │  │  │  ├─ test_concat.py
   │        │  │  │  │  ├─ test_construction.py
   │        │  │  │  │  ├─ test_dtypes.py
   │        │  │  │  │  ├─ test_function.py
   │        │  │  │  │  ├─ test_indexing.py
   │        │  │  │  │  ├─ test_reduction.py
   │        │  │  │  │  └─ test_repr.py
   │        │  │  │  ├─ interval
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_astype.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_formats.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_interval.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_interval_pyarrow.cpython-311.pyc
   │        │  │  │  │  │  └─ test_overlaps.cpython-311.pyc
   │        │  │  │  │  ├─ test_astype.py
   │        │  │  │  │  ├─ test_formats.py
   │        │  │  │  │  ├─ test_interval.py
   │        │  │  │  │  ├─ test_interval_pyarrow.py
   │        │  │  │  │  └─ test_overlaps.py
   │        │  │  │  ├─ masked
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_arithmetic.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_arrow_compat.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_function.cpython-311.pyc
   │        │  │  │  │  │  └─ test_indexing.cpython-311.pyc
   │        │  │  │  │  ├─ test_arithmetic.py
   │        │  │  │  │  ├─ test_arrow_compat.py
   │        │  │  │  │  ├─ test_function.py
   │        │  │  │  │  └─ test_indexing.py
   │        │  │  │  ├─ masked_shared.py
   │        │  │  │  ├─ numpy_
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  │  └─ test_numpy.cpython-311.pyc
   │        │  │  │  │  ├─ test_indexing.py
   │        │  │  │  │  └─ test_numpy.py
   │        │  │  │  ├─ period
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_arrow_compat.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_astype.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_constructors.cpython-311.pyc
   │        │  │  │  │  │  └─ test_reductions.cpython-311.pyc
   │        │  │  │  │  ├─ test_arrow_compat.py
   │        │  │  │  │  ├─ test_astype.py
   │        │  │  │  │  ├─ test_constructors.py
   │        │  │  │  │  └─ test_reductions.py
   │        │  │  │  ├─ sparse
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_accessor.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_arithmetics.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_array.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_astype.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_combine_concat.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_constructors.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_dtype.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_libsparse.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_reductions.cpython-311.pyc
   │        │  │  │  │  │  └─ test_unary.cpython-311.pyc
   │        │  │  │  │  ├─ test_accessor.py
   │        │  │  │  │  ├─ test_arithmetics.py
   │        │  │  │  │  ├─ test_array.py
   │        │  │  │  │  ├─ test_astype.py
   │        │  │  │  │  ├─ test_combine_concat.py
   │        │  │  │  │  ├─ test_constructors.py
   │        │  │  │  │  ├─ test_dtype.py
   │        │  │  │  │  ├─ test_indexing.py
   │        │  │  │  │  ├─ test_libsparse.py
   │        │  │  │  │  ├─ test_reductions.py
   │        │  │  │  │  └─ test_unary.py
   │        │  │  │  ├─ string_
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_string.cpython-311.pyc
   │        │  │  │  │  │  └─ test_string_arrow.cpython-311.pyc
   │        │  │  │  │  ├─ test_string.py
   │        │  │  │  │  └─ test_string_arrow.py
   │        │  │  │  ├─ test_array.py
   │        │  │  │  ├─ test_datetimelike.py
   │        │  │  │  ├─ test_datetimes.py
   │        │  │  │  ├─ test_ndarray_backed.py
   │        │  │  │  ├─ test_period.py
   │        │  │  │  ├─ test_timedeltas.py
   │        │  │  │  └─ timedeltas
   │        │  │  │     ├─ __init__.py
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │     │  ├─ test_constructors.cpython-311.pyc
   │        │  │  │     │  ├─ test_cumulative.cpython-311.pyc
   │        │  │  │     │  └─ test_reductions.cpython-311.pyc
   │        │  │  │     ├─ test_constructors.py
   │        │  │  │     ├─ test_cumulative.py
   │        │  │  │     └─ test_reductions.py
   │        │  │  ├─ base
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ common.cpython-311.pyc
   │        │  │  │  │  ├─ test_constructors.cpython-311.pyc
   │        │  │  │  │  ├─ test_conversion.cpython-311.pyc
   │        │  │  │  │  ├─ test_fillna.cpython-311.pyc
   │        │  │  │  │  ├─ test_misc.cpython-311.pyc
   │        │  │  │  │  ├─ test_transpose.cpython-311.pyc
   │        │  │  │  │  ├─ test_unique.cpython-311.pyc
   │        │  │  │  │  └─ test_value_counts.cpython-311.pyc
   │        │  │  │  ├─ common.py
   │        │  │  │  ├─ test_constructors.py
   │        │  │  │  ├─ test_conversion.py
   │        │  │  │  ├─ test_fillna.py
   │        │  │  │  ├─ test_misc.py
   │        │  │  │  ├─ test_transpose.py
   │        │  │  │  ├─ test_unique.py
   │        │  │  │  └─ test_value_counts.py
   │        │  │  ├─ computation
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test_compat.cpython-311.pyc
   │        │  │  │  │  └─ test_eval.cpython-311.pyc
   │        │  │  │  ├─ test_compat.py
   │        │  │  │  └─ test_eval.py
   │        │  │  ├─ config
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test_config.cpython-311.pyc
   │        │  │  │  │  └─ test_localization.cpython-311.pyc
   │        │  │  │  ├─ test_config.py
   │        │  │  │  └─ test_localization.py
   │        │  │  ├─ construction
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  └─ test_extract_array.cpython-311.pyc
   │        │  │  │  └─ test_extract_array.py
   │        │  │  ├─ copy_view
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test_array.cpython-311.pyc
   │        │  │  │  │  ├─ test_astype.cpython-311.pyc
   │        │  │  │  │  ├─ test_chained_assignment_deprecation.cpython-311.pyc
   │        │  │  │  │  ├─ test_clip.cpython-311.pyc
   │        │  │  │  │  ├─ test_constructors.cpython-311.pyc
   │        │  │  │  │  ├─ test_core_functionalities.cpython-311.pyc
   │        │  │  │  │  ├─ test_functions.cpython-311.pyc
   │        │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  ├─ test_internals.cpython-311.pyc
   │        │  │  │  │  ├─ test_interp_fillna.cpython-311.pyc
   │        │  │  │  │  ├─ test_methods.cpython-311.pyc
   │        │  │  │  │  ├─ test_replace.cpython-311.pyc
   │        │  │  │  │  ├─ test_setitem.cpython-311.pyc
   │        │  │  │  │  ├─ test_util.cpython-311.pyc
   │        │  │  │  │  └─ util.cpython-311.pyc
   │        │  │  │  ├─ index
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_datetimeindex.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_index.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_periodindex.cpython-311.pyc
   │        │  │  │  │  │  └─ test_timedeltaindex.cpython-311.pyc
   │        │  │  │  │  ├─ test_datetimeindex.py
   │        │  │  │  │  ├─ test_index.py
   │        │  │  │  │  ├─ test_periodindex.py
   │        │  │  │  │  └─ test_timedeltaindex.py
   │        │  │  │  ├─ test_array.py
   │        │  │  │  ├─ test_astype.py
   │        │  │  │  ├─ test_chained_assignment_deprecation.py
   │        │  │  │  ├─ test_clip.py
   │        │  │  │  ├─ test_constructors.py
   │        │  │  │  ├─ test_core_functionalities.py
   │        │  │  │  ├─ test_functions.py
   │        │  │  │  ├─ test_indexing.py
   │        │  │  │  ├─ test_internals.py
   │        │  │  │  ├─ test_interp_fillna.py
   │        │  │  │  ├─ test_methods.py
   │        │  │  │  ├─ test_replace.py
   │        │  │  │  ├─ test_setitem.py
   │        │  │  │  ├─ test_util.py
   │        │  │  │  └─ util.py
   │        │  │  ├─ dtypes
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test_common.cpython-311.pyc
   │        │  │  │  │  ├─ test_concat.cpython-311.pyc
   │        │  │  │  │  ├─ test_dtypes.cpython-311.pyc
   │        │  │  │  │  ├─ test_generic.cpython-311.pyc
   │        │  │  │  │  ├─ test_inference.cpython-311.pyc
   │        │  │  │  │  └─ test_missing.cpython-311.pyc
   │        │  │  │  ├─ cast
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_can_hold_element.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_construct_from_scalar.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_construct_ndarray.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_construct_object_arr.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_dict_compat.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_downcast.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_find_common_type.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_infer_datetimelike.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_infer_dtype.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_maybe_box_native.cpython-311.pyc
   │        │  │  │  │  │  └─ test_promote.cpython-311.pyc
   │        │  │  │  │  ├─ test_can_hold_element.py
   │        │  │  │  │  ├─ test_construct_from_scalar.py
   │        │  │  │  │  ├─ test_construct_ndarray.py
   │        │  │  │  │  ├─ test_construct_object_arr.py
   │        │  │  │  │  ├─ test_dict_compat.py
   │        │  │  │  │  ├─ test_downcast.py
   │        │  │  │  │  ├─ test_find_common_type.py
   │        │  │  │  │  ├─ test_infer_datetimelike.py
   │        │  │  │  │  ├─ test_infer_dtype.py
   │        │  │  │  │  ├─ test_maybe_box_native.py
   │        │  │  │  │  └─ test_promote.py
   │        │  │  │  ├─ test_common.py
   │        │  │  │  ├─ test_concat.py
   │        │  │  │  ├─ test_dtypes.py
   │        │  │  │  ├─ test_generic.py
   │        │  │  │  ├─ test_inference.py
   │        │  │  │  └─ test_missing.py
   │        │  │  ├─ extension
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ conftest.cpython-311.pyc
   │        │  │  │  │  ├─ test_arrow.cpython-311.pyc
   │        │  │  │  │  ├─ test_categorical.cpython-311.pyc
   │        │  │  │  │  ├─ test_common.cpython-311.pyc
   │        │  │  │  │  ├─ test_datetime.cpython-311.pyc
   │        │  │  │  │  ├─ test_extension.cpython-311.pyc
   │        │  │  │  │  ├─ test_interval.cpython-311.pyc
   │        │  │  │  │  ├─ test_masked.cpython-311.pyc
   │        │  │  │  │  ├─ test_numpy.cpython-311.pyc
   │        │  │  │  │  ├─ test_period.cpython-311.pyc
   │        │  │  │  │  ├─ test_sparse.cpython-311.pyc
   │        │  │  │  │  └─ test_string.cpython-311.pyc
   │        │  │  │  ├─ array_with_attr
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ array.cpython-311.pyc
   │        │  │  │  │  │  └─ test_array_with_attr.cpython-311.pyc
   │        │  │  │  │  ├─ array.py
   │        │  │  │  │  └─ test_array_with_attr.py
   │        │  │  │  ├─ base
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ accumulate.cpython-311.pyc
   │        │  │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  │  ├─ casting.cpython-311.pyc
   │        │  │  │  │  │  ├─ constructors.cpython-311.pyc
   │        │  │  │  │  │  ├─ dim2.cpython-311.pyc
   │        │  │  │  │  │  ├─ dtype.cpython-311.pyc
   │        │  │  │  │  │  ├─ getitem.cpython-311.pyc
   │        │  │  │  │  │  ├─ groupby.cpython-311.pyc
   │        │  │  │  │  │  ├─ index.cpython-311.pyc
   │        │  │  │  │  │  ├─ interface.cpython-311.pyc
   │        │  │  │  │  │  ├─ io.cpython-311.pyc
   │        │  │  │  │  │  ├─ methods.cpython-311.pyc
   │        │  │  │  │  │  ├─ missing.cpython-311.pyc
   │        │  │  │  │  │  ├─ ops.cpython-311.pyc
   │        │  │  │  │  │  ├─ printing.cpython-311.pyc
   │        │  │  │  │  │  ├─ reduce.cpython-311.pyc
   │        │  │  │  │  │  ├─ reshaping.cpython-311.pyc
   │        │  │  │  │  │  └─ setitem.cpython-311.pyc
   │        │  │  │  │  ├─ accumulate.py
   │        │  │  │  │  ├─ base.py
   │        │  │  │  │  ├─ casting.py
   │        │  │  │  │  ├─ constructors.py
   │        │  │  │  │  ├─ dim2.py
   │        │  │  │  │  ├─ dtype.py
   │        │  │  │  │  ├─ getitem.py
   │        │  │  │  │  ├─ groupby.py
   │        │  │  │  │  ├─ index.py
   │        │  │  │  │  ├─ interface.py
   │        │  │  │  │  ├─ io.py
   │        │  │  │  │  ├─ methods.py
   │        │  │  │  │  ├─ missing.py
   │        │  │  │  │  ├─ ops.py
   │        │  │  │  │  ├─ printing.py
   │        │  │  │  │  ├─ reduce.py
   │        │  │  │  │  ├─ reshaping.py
   │        │  │  │  │  └─ setitem.py
   │        │  │  │  ├─ conftest.py
   │        │  │  │  ├─ date
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ array.cpython-311.pyc
   │        │  │  │  │  └─ array.py
   │        │  │  │  ├─ decimal
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ array.cpython-311.pyc
   │        │  │  │  │  │  └─ test_decimal.cpython-311.pyc
   │        │  │  │  │  ├─ array.py
   │        │  │  │  │  └─ test_decimal.py
   │        │  │  │  ├─ json
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ array.cpython-311.pyc
   │        │  │  │  │  │  └─ test_json.cpython-311.pyc
   │        │  │  │  │  ├─ array.py
   │        │  │  │  │  └─ test_json.py
   │        │  │  │  ├─ list
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ array.cpython-311.pyc
   │        │  │  │  │  │  └─ test_list.cpython-311.pyc
   │        │  │  │  │  ├─ array.py
   │        │  │  │  │  └─ test_list.py
   │        │  │  │  ├─ test_arrow.py
   │        │  │  │  ├─ test_categorical.py
   │        │  │  │  ├─ test_common.py
   │        │  │  │  ├─ test_datetime.py
   │        │  │  │  ├─ test_extension.py
   │        │  │  │  ├─ test_interval.py
   │        │  │  │  ├─ test_masked.py
   │        │  │  │  ├─ test_numpy.py
   │        │  │  │  ├─ test_period.py
   │        │  │  │  ├─ test_sparse.py
   │        │  │  │  └─ test_string.py
   │        │  │  ├─ frame
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ common.cpython-311.pyc
   │        │  │  │  │  ├─ conftest.cpython-311.pyc
   │        │  │  │  │  ├─ test_alter_axes.cpython-311.pyc
   │        │  │  │  │  ├─ test_api.cpython-311.pyc
   │        │  │  │  │  ├─ test_arithmetic.cpython-311.pyc
   │        │  │  │  │  ├─ test_arrow_interface.cpython-311.pyc
   │        │  │  │  │  ├─ test_block_internals.cpython-311.pyc
   │        │  │  │  │  ├─ test_constructors.cpython-311.pyc
   │        │  │  │  │  ├─ test_cumulative.cpython-311.pyc
   │        │  │  │  │  ├─ test_iteration.cpython-311.pyc
   │        │  │  │  │  ├─ test_logical_ops.cpython-311.pyc
   │        │  │  │  │  ├─ test_nonunique_indexes.cpython-311.pyc
   │        │  │  │  │  ├─ test_npfuncs.cpython-311.pyc
   │        │  │  │  │  ├─ test_query_eval.cpython-311.pyc
   │        │  │  │  │  ├─ test_reductions.cpython-311.pyc
   │        │  │  │  │  ├─ test_repr.cpython-311.pyc
   │        │  │  │  │  ├─ test_stack_unstack.cpython-311.pyc
   │        │  │  │  │  ├─ test_subclass.cpython-311.pyc
   │        │  │  │  │  ├─ test_ufunc.cpython-311.pyc
   │        │  │  │  │  ├─ test_unary.cpython-311.pyc
   │        │  │  │  │  └─ test_validate.cpython-311.pyc
   │        │  │  │  ├─ common.py
   │        │  │  │  ├─ conftest.py
   │        │  │  │  ├─ constructors
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_from_dict.cpython-311.pyc
   │        │  │  │  │  │  └─ test_from_records.cpython-311.pyc
   │        │  │  │  │  ├─ test_from_dict.py
   │        │  │  │  │  └─ test_from_records.py
   │        │  │  │  ├─ indexing
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_coercion.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_delitem.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_get.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_get_value.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_getitem.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_insert.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_mask.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_set_value.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_setitem.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_take.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_where.cpython-311.pyc
   │        │  │  │  │  │  └─ test_xs.cpython-311.pyc
   │        │  │  │  │  ├─ test_coercion.py
   │        │  │  │  │  ├─ test_delitem.py
   │        │  │  │  │  ├─ test_get.py
   │        │  │  │  │  ├─ test_get_value.py
   │        │  │  │  │  ├─ test_getitem.py
   │        │  │  │  │  ├─ test_indexing.py
   │        │  │  │  │  ├─ test_insert.py
   │        │  │  │  │  ├─ test_mask.py
   │        │  │  │  │  ├─ test_set_value.py
   │        │  │  │  │  ├─ test_setitem.py
   │        │  │  │  │  ├─ test_take.py
   │        │  │  │  │  ├─ test_where.py
   │        │  │  │  │  └─ test_xs.py
   │        │  │  │  ├─ methods
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_add_prefix_suffix.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_align.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_asfreq.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_asof.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_assign.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_astype.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_at_time.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_between_time.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_clip.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_combine.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_combine_first.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_compare.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_convert_dtypes.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_copy.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_count.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_cov_corr.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_describe.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_diff.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_dot.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_drop.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_drop_duplicates.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_droplevel.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_dropna.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_dtypes.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_duplicated.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_equals.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_explode.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_fillna.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_filter.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_first_and_last.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_first_valid_index.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_get_numeric_data.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_head_tail.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_infer_objects.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_info.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_interpolate.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_is_homogeneous_dtype.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_isetitem.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_isin.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_iterrows.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_join.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_map.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_matmul.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_nlargest.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_pct_change.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_pipe.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_pop.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_quantile.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_rank.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_reindex.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_reindex_like.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_rename.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_rename_axis.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_reorder_levels.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_replace.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_reset_index.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_round.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_sample.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_select_dtypes.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_set_axis.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_set_index.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_shift.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_size.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_sort_index.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_sort_values.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_swapaxes.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_swaplevel.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_to_csv.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_to_dict.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_to_dict_of_blocks.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_to_numpy.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_to_period.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_to_records.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_to_timestamp.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_transpose.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_truncate.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_tz_convert.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_tz_localize.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_update.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_value_counts.cpython-311.pyc
   │        │  │  │  │  │  └─ test_values.cpython-311.pyc
   │        │  │  │  │  ├─ test_add_prefix_suffix.py
   │        │  │  │  │  ├─ test_align.py
   │        │  │  │  │  ├─ test_asfreq.py
   │        │  │  │  │  ├─ test_asof.py
   │        │  │  │  │  ├─ test_assign.py
   │        │  │  │  │  ├─ test_astype.py
   │        │  │  │  │  ├─ test_at_time.py
   │        │  │  │  │  ├─ test_between_time.py
   │        │  │  │  │  ├─ test_clip.py
   │        │  │  │  │  ├─ test_combine.py
   │        │  │  │  │  ├─ test_combine_first.py
   │        │  │  │  │  ├─ test_compare.py
   │        │  │  │  │  ├─ test_convert_dtypes.py
   │        │  │  │  │  ├─ test_copy.py
   │        │  │  │  │  ├─ test_count.py
   │        │  │  │  │  ├─ test_cov_corr.py
   │        │  │  │  │  ├─ test_describe.py
   │        │  │  │  │  ├─ test_diff.py
   │        │  │  │  │  ├─ test_dot.py
   │        │  │  │  │  ├─ test_drop.py
   │        │  │  │  │  ├─ test_drop_duplicates.py
   │        │  │  │  │  ├─ test_droplevel.py
   │        │  │  │  │  ├─ test_dropna.py
   │        │  │  │  │  ├─ test_dtypes.py
   │        │  │  │  │  ├─ test_duplicated.py
   │        │  │  │  │  ├─ test_equals.py
   │        │  │  │  │  ├─ test_explode.py
   │        │  │  │  │  ├─ test_fillna.py
   │        │  │  │  │  ├─ test_filter.py
   │        │  │  │  │  ├─ test_first_and_last.py
   │        │  │  │  │  ├─ test_first_valid_index.py
   │        │  │  │  │  ├─ test_get_numeric_data.py
   │        │  │  │  │  ├─ test_head_tail.py
   │        │  │  │  │  ├─ test_infer_objects.py
   │        │  │  │  │  ├─ test_info.py
   │        │  │  │  │  ├─ test_interpolate.py
   │        │  │  │  │  ├─ test_is_homogeneous_dtype.py
   │        │  │  │  │  ├─ test_isetitem.py
   │        │  │  │  │  ├─ test_isin.py
   │        │  │  │  │  ├─ test_iterrows.py
   │        │  │  │  │  ├─ test_join.py
   │        │  │  │  │  ├─ test_map.py
   │        │  │  │  │  ├─ test_matmul.py
   │        │  │  │  │  ├─ test_nlargest.py
   │        │  │  │  │  ├─ test_pct_change.py
   │        │  │  │  │  ├─ test_pipe.py
   │        │  │  │  │  ├─ test_pop.py
   │        │  │  │  │  ├─ test_quantile.py
   │        │  │  │  │  ├─ test_rank.py
   │        │  │  │  │  ├─ test_reindex.py
   │        │  │  │  │  ├─ test_reindex_like.py
   │        │  │  │  │  ├─ test_rename.py
   │        │  │  │  │  ├─ test_rename_axis.py
   │        │  │  │  │  ├─ test_reorder_levels.py
   │        │  │  │  │  ├─ test_replace.py
   │        │  │  │  │  ├─ test_reset_index.py
   │        │  │  │  │  ├─ test_round.py
   │        │  │  │  │  ├─ test_sample.py
   │        │  │  │  │  ├─ test_select_dtypes.py
   │        │  │  │  │  ├─ test_set_axis.py
   │        │  │  │  │  ├─ test_set_index.py
   │        │  │  │  │  ├─ test_shift.py
   │        │  │  │  │  ├─ test_size.py
   │        │  │  │  │  ├─ test_sort_index.py
   │        │  │  │  │  ├─ test_sort_values.py
   │        │  │  │  │  ├─ test_swapaxes.py
   │        │  │  │  │  ├─ test_swaplevel.py
   │        │  │  │  │  ├─ test_to_csv.py
   │        │  │  │  │  ├─ test_to_dict.py
   │        │  │  │  │  ├─ test_to_dict_of_blocks.py
   │        │  │  │  │  ├─ test_to_numpy.py
   │        │  │  │  │  ├─ test_to_period.py
   │        │  │  │  │  ├─ test_to_records.py
   │        │  │  │  │  ├─ test_to_timestamp.py
   │        │  │  │  │  ├─ test_transpose.py
   │        │  │  │  │  ├─ test_truncate.py
   │        │  │  │  │  ├─ test_tz_convert.py
   │        │  │  │  │  ├─ test_tz_localize.py
   │        │  │  │  │  ├─ test_update.py
   │        │  │  │  │  ├─ test_value_counts.py
   │        │  │  │  │  └─ test_values.py
   │        │  │  │  ├─ test_alter_axes.py
   │        │  │  │  ├─ test_api.py
   │        │  │  │  ├─ test_arithmetic.py
   │        │  │  │  ├─ test_arrow_interface.py
   │        │  │  │  ├─ test_block_internals.py
   │        │  │  │  ├─ test_constructors.py
   │        │  │  │  ├─ test_cumulative.py
   │        │  │  │  ├─ test_iteration.py
   │        │  │  │  ├─ test_logical_ops.py
   │        │  │  │  ├─ test_nonunique_indexes.py
   │        │  │  │  ├─ test_npfuncs.py
   │        │  │  │  ├─ test_query_eval.py
   │        │  │  │  ├─ test_reductions.py
   │        │  │  │  ├─ test_repr.py
   │        │  │  │  ├─ test_stack_unstack.py
   │        │  │  │  ├─ test_subclass.py
   │        │  │  │  ├─ test_ufunc.py
   │        │  │  │  ├─ test_unary.py
   │        │  │  │  └─ test_validate.py
   │        │  │  ├─ generic
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test_duplicate_labels.cpython-311.pyc
   │        │  │  │  │  ├─ test_finalize.cpython-311.pyc
   │        │  │  │  │  ├─ test_frame.cpython-311.pyc
   │        │  │  │  │  ├─ test_generic.cpython-311.pyc
   │        │  │  │  │  ├─ test_label_or_level_utils.cpython-311.pyc
   │        │  │  │  │  ├─ test_series.cpython-311.pyc
   │        │  │  │  │  └─ test_to_xarray.cpython-311.pyc
   │        │  │  │  ├─ test_duplicate_labels.py
   │        │  │  │  ├─ test_finalize.py
   │        │  │  │  ├─ test_frame.py
   │        │  │  │  ├─ test_generic.py
   │        │  │  │  ├─ test_label_or_level_utils.py
   │        │  │  │  ├─ test_series.py
   │        │  │  │  └─ test_to_xarray.py
   │        │  │  ├─ groupby
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ conftest.cpython-311.pyc
   │        │  │  │  │  ├─ test_all_methods.cpython-311.pyc
   │        │  │  │  │  ├─ test_api.cpython-311.pyc
   │        │  │  │  │  ├─ test_apply.cpython-311.pyc
   │        │  │  │  │  ├─ test_apply_mutate.cpython-311.pyc
   │        │  │  │  │  ├─ test_bin_groupby.cpython-311.pyc
   │        │  │  │  │  ├─ test_categorical.cpython-311.pyc
   │        │  │  │  │  ├─ test_counting.cpython-311.pyc
   │        │  │  │  │  ├─ test_cumulative.cpython-311.pyc
   │        │  │  │  │  ├─ test_filters.cpython-311.pyc
   │        │  │  │  │  ├─ test_groupby.cpython-311.pyc
   │        │  │  │  │  ├─ test_groupby_dropna.cpython-311.pyc
   │        │  │  │  │  ├─ test_groupby_subclass.cpython-311.pyc
   │        │  │  │  │  ├─ test_grouping.cpython-311.pyc
   │        │  │  │  │  ├─ test_index_as_string.cpython-311.pyc
   │        │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  ├─ test_libgroupby.cpython-311.pyc
   │        │  │  │  │  ├─ test_missing.cpython-311.pyc
   │        │  │  │  │  ├─ test_numba.cpython-311.pyc
   │        │  │  │  │  ├─ test_numeric_only.cpython-311.pyc
   │        │  │  │  │  ├─ test_pipe.cpython-311.pyc
   │        │  │  │  │  ├─ test_raises.cpython-311.pyc
   │        │  │  │  │  ├─ test_reductions.cpython-311.pyc
   │        │  │  │  │  └─ test_timegrouper.cpython-311.pyc
   │        │  │  │  ├─ aggregate
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_aggregate.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_cython.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_numba.cpython-311.pyc
   │        │  │  │  │  │  └─ test_other.cpython-311.pyc
   │        │  │  │  │  ├─ test_aggregate.py
   │        │  │  │  │  ├─ test_cython.py
   │        │  │  │  │  ├─ test_numba.py
   │        │  │  │  │  └─ test_other.py
   │        │  │  │  ├─ conftest.py
   │        │  │  │  ├─ methods
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_corrwith.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_describe.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_groupby_shift_diff.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_is_monotonic.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_nlargest_nsmallest.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_nth.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_quantile.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_rank.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_sample.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_size.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_skew.cpython-311.pyc
   │        │  │  │  │  │  └─ test_value_counts.cpython-311.pyc
   │        │  │  │  │  ├─ test_corrwith.py
   │        │  │  │  │  ├─ test_describe.py
   │        │  │  │  │  ├─ test_groupby_shift_diff.py
   │        │  │  │  │  ├─ test_is_monotonic.py
   │        │  │  │  │  ├─ test_nlargest_nsmallest.py
   │        │  │  │  │  ├─ test_nth.py
   │        │  │  │  │  ├─ test_quantile.py
   │        │  │  │  │  ├─ test_rank.py
   │        │  │  │  │  ├─ test_sample.py
   │        │  │  │  │  ├─ test_size.py
   │        │  │  │  │  ├─ test_skew.py
   │        │  │  │  │  └─ test_value_counts.py
   │        │  │  │  ├─ test_all_methods.py
   │        │  │  │  ├─ test_api.py
   │        │  │  │  ├─ test_apply.py
   │        │  │  │  ├─ test_apply_mutate.py
   │        │  │  │  ├─ test_bin_groupby.py
   │        │  │  │  ├─ test_categorical.py
   │        │  │  │  ├─ test_counting.py
   │        │  │  │  ├─ test_cumulative.py
   │        │  │  │  ├─ test_filters.py
   │        │  │  │  ├─ test_groupby.py
   │        │  │  │  ├─ test_groupby_dropna.py
   │        │  │  │  ├─ test_groupby_subclass.py
   │        │  │  │  ├─ test_grouping.py
   │        │  │  │  ├─ test_index_as_string.py
   │        │  │  │  ├─ test_indexing.py
   │        │  │  │  ├─ test_libgroupby.py
   │        │  │  │  ├─ test_missing.py
   │        │  │  │  ├─ test_numba.py
   │        │  │  │  ├─ test_numeric_only.py
   │        │  │  │  ├─ test_pipe.py
   │        │  │  │  ├─ test_raises.py
   │        │  │  │  ├─ test_reductions.py
   │        │  │  │  ├─ test_timegrouper.py
   │        │  │  │  └─ transform
   │        │  │  │     ├─ __init__.py
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │     │  ├─ test_numba.cpython-311.pyc
   │        │  │  │     │  └─ test_transform.cpython-311.pyc
   │        │  │  │     ├─ test_numba.py
   │        │  │  │     └─ test_transform.py
   │        │  │  ├─ indexes
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ conftest.cpython-311.pyc
   │        │  │  │  │  ├─ test_any_index.cpython-311.pyc
   │        │  │  │  │  ├─ test_base.cpython-311.pyc
   │        │  │  │  │  ├─ test_common.cpython-311.pyc
   │        │  │  │  │  ├─ test_datetimelike.cpython-311.pyc
   │        │  │  │  │  ├─ test_engines.cpython-311.pyc
   │        │  │  │  │  ├─ test_frozen.cpython-311.pyc
   │        │  │  │  │  ├─ test_index_new.cpython-311.pyc
   │        │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  ├─ test_numpy_compat.cpython-311.pyc
   │        │  │  │  │  ├─ test_old_base.cpython-311.pyc
   │        │  │  │  │  ├─ test_setops.cpython-311.pyc
   │        │  │  │  │  └─ test_subclass.cpython-311.pyc
   │        │  │  │  ├─ base_class
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_constructors.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_formats.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_pickle.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_reshape.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_setops.cpython-311.pyc
   │        │  │  │  │  │  └─ test_where.cpython-311.pyc
   │        │  │  │  │  ├─ test_constructors.py
   │        │  │  │  │  ├─ test_formats.py
   │        │  │  │  │  ├─ test_indexing.py
   │        │  │  │  │  ├─ test_pickle.py
   │        │  │  │  │  ├─ test_reshape.py
   │        │  │  │  │  ├─ test_setops.py
   │        │  │  │  │  └─ test_where.py
   │        │  │  │  ├─ categorical
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_append.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_astype.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_category.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_constructors.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_equals.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_fillna.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_formats.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_map.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_reindex.cpython-311.pyc
   │        │  │  │  │  │  └─ test_setops.cpython-311.pyc
   │        │  │  │  │  ├─ test_append.py
   │        │  │  │  │  ├─ test_astype.py
   │        │  │  │  │  ├─ test_category.py
   │        │  │  │  │  ├─ test_constructors.py
   │        │  │  │  │  ├─ test_equals.py
   │        │  │  │  │  ├─ test_fillna.py
   │        │  │  │  │  ├─ test_formats.py
   │        │  │  │  │  ├─ test_indexing.py
   │        │  │  │  │  ├─ test_map.py
   │        │  │  │  │  ├─ test_reindex.py
   │        │  │  │  │  └─ test_setops.py
   │        │  │  │  ├─ conftest.py
   │        │  │  │  ├─ datetimelike_
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_drop_duplicates.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_equals.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_is_monotonic.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_nat.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_sort_values.cpython-311.pyc
   │        │  │  │  │  │  └─ test_value_counts.cpython-311.pyc
   │        │  │  │  │  ├─ test_drop_duplicates.py
   │        │  │  │  │  ├─ test_equals.py
   │        │  │  │  │  ├─ test_indexing.py
   │        │  │  │  │  ├─ test_is_monotonic.py
   │        │  │  │  │  ├─ test_nat.py
   │        │  │  │  │  ├─ test_sort_values.py
   │        │  │  │  │  └─ test_value_counts.py
   │        │  │  │  ├─ datetimes
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_arithmetic.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_constructors.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_date_range.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_datetime.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_formats.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_freq_attr.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_iter.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_join.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_npfuncs.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_ops.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_partial_slicing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_pickle.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_reindex.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_scalar_compat.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_setops.cpython-311.pyc
   │        │  │  │  │  │  └─ test_timezones.cpython-311.pyc
   │        │  │  │  │  ├─ methods
   │        │  │  │  │  │  ├─ __init__.py
   │        │  │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_asof.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_astype.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_delete.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_factorize.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_fillna.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_insert.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_isocalendar.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_map.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_normalize.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_repeat.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_resolution.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_round.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_shift.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_snap.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_to_frame.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_to_julian_date.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_to_period.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_to_pydatetime.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_to_series.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_tz_convert.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_tz_localize.cpython-311.pyc
   │        │  │  │  │  │  │  └─ test_unique.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_asof.py
   │        │  │  │  │  │  ├─ test_astype.py
   │        │  │  │  │  │  ├─ test_delete.py
   │        │  │  │  │  │  ├─ test_factorize.py
   │        │  │  │  │  │  ├─ test_fillna.py
   │        │  │  │  │  │  ├─ test_insert.py
   │        │  │  │  │  │  ├─ test_isocalendar.py
   │        │  │  │  │  │  ├─ test_map.py
   │        │  │  │  │  │  ├─ test_normalize.py
   │        │  │  │  │  │  ├─ test_repeat.py
   │        │  │  │  │  │  ├─ test_resolution.py
   │        │  │  │  │  │  ├─ test_round.py
   │        │  │  │  │  │  ├─ test_shift.py
   │        │  │  │  │  │  ├─ test_snap.py
   │        │  │  │  │  │  ├─ test_to_frame.py
   │        │  │  │  │  │  ├─ test_to_julian_date.py
   │        │  │  │  │  │  ├─ test_to_period.py
   │        │  │  │  │  │  ├─ test_to_pydatetime.py
   │        │  │  │  │  │  ├─ test_to_series.py
   │        │  │  │  │  │  ├─ test_tz_convert.py
   │        │  │  │  │  │  ├─ test_tz_localize.py
   │        │  │  │  │  │  └─ test_unique.py
   │        │  │  │  │  ├─ test_arithmetic.py
   │        │  │  │  │  ├─ test_constructors.py
   │        │  │  │  │  ├─ test_date_range.py
   │        │  │  │  │  ├─ test_datetime.py
   │        │  │  │  │  ├─ test_formats.py
   │        │  │  │  │  ├─ test_freq_attr.py
   │        │  │  │  │  ├─ test_indexing.py
   │        │  │  │  │  ├─ test_iter.py
   │        │  │  │  │  ├─ test_join.py
   │        │  │  │  │  ├─ test_npfuncs.py
   │        │  │  │  │  ├─ test_ops.py
   │        │  │  │  │  ├─ test_partial_slicing.py
   │        │  │  │  │  ├─ test_pickle.py
   │        │  │  │  │  ├─ test_reindex.py
   │        │  │  │  │  ├─ test_scalar_compat.py
   │        │  │  │  │  ├─ test_setops.py
   │        │  │  │  │  └─ test_timezones.py
   │        │  │  │  ├─ interval
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_astype.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_constructors.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_equals.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_formats.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_interval.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_interval_range.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_interval_tree.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_join.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_pickle.cpython-311.pyc
   │        │  │  │  │  │  └─ test_setops.cpython-311.pyc
   │        │  │  │  │  ├─ test_astype.py
   │        │  │  │  │  ├─ test_constructors.py
   │        │  │  │  │  ├─ test_equals.py
   │        │  │  │  │  ├─ test_formats.py
   │        │  │  │  │  ├─ test_indexing.py
   │        │  │  │  │  ├─ test_interval.py
   │        │  │  │  │  ├─ test_interval_range.py
   │        │  │  │  │  ├─ test_interval_tree.py
   │        │  │  │  │  ├─ test_join.py
   │        │  │  │  │  ├─ test_pickle.py
   │        │  │  │  │  └─ test_setops.py
   │        │  │  │  ├─ multi
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ conftest.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_analytics.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_astype.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_compat.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_constructors.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_conversion.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_copy.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_drop.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_duplicates.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_equivalence.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_formats.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_get_level_values.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_get_set.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_integrity.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_isin.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_join.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_lexsort.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_missing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_monotonic.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_names.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_partial_indexing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_pickle.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_reindex.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_reshape.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_setops.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_sorting.cpython-311.pyc
   │        │  │  │  │  │  └─ test_take.cpython-311.pyc
   │        │  │  │  │  ├─ conftest.py
   │        │  │  │  │  ├─ test_analytics.py
   │        │  │  │  │  ├─ test_astype.py
   │        │  │  │  │  ├─ test_compat.py
   │        │  │  │  │  ├─ test_constructors.py
   │        │  │  │  │  ├─ test_conversion.py
   │        │  │  │  │  ├─ test_copy.py
   │        │  │  │  │  ├─ test_drop.py
   │        │  │  │  │  ├─ test_duplicates.py
   │        │  │  │  │  ├─ test_equivalence.py
   │        │  │  │  │  ├─ test_formats.py
   │        │  │  │  │  ├─ test_get_level_values.py
   │        │  │  │  │  ├─ test_get_set.py
   │        │  │  │  │  ├─ test_indexing.py
   │        │  │  │  │  ├─ test_integrity.py
   │        │  │  │  │  ├─ test_isin.py
   │        │  │  │  │  ├─ test_join.py
   │        │  │  │  │  ├─ test_lexsort.py
   │        │  │  │  │  ├─ test_missing.py
   │        │  │  │  │  ├─ test_monotonic.py
   │        │  │  │  │  ├─ test_names.py
   │        │  │  │  │  ├─ test_partial_indexing.py
   │        │  │  │  │  ├─ test_pickle.py
   │        │  │  │  │  ├─ test_reindex.py
   │        │  │  │  │  ├─ test_reshape.py
   │        │  │  │  │  ├─ test_setops.py
   │        │  │  │  │  ├─ test_sorting.py
   │        │  │  │  │  └─ test_take.py
   │        │  │  │  ├─ numeric
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_astype.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_join.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_numeric.cpython-311.pyc
   │        │  │  │  │  │  └─ test_setops.cpython-311.pyc
   │        │  │  │  │  ├─ test_astype.py
   │        │  │  │  │  ├─ test_indexing.py
   │        │  │  │  │  ├─ test_join.py
   │        │  │  │  │  ├─ test_numeric.py
   │        │  │  │  │  └─ test_setops.py
   │        │  │  │  ├─ object
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_astype.cpython-311.pyc
   │        │  │  │  │  │  └─ test_indexing.cpython-311.pyc
   │        │  │  │  │  ├─ test_astype.py
   │        │  │  │  │  └─ test_indexing.py
   │        │  │  │  ├─ period
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_constructors.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_formats.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_freq_attr.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_join.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_monotonic.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_partial_slicing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_period.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_period_range.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_pickle.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_resolution.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_scalar_compat.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_searchsorted.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_setops.cpython-311.pyc
   │        │  │  │  │  │  └─ test_tools.cpython-311.pyc
   │        │  │  │  │  ├─ methods
   │        │  │  │  │  │  ├─ __init__.py
   │        │  │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_asfreq.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_astype.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_factorize.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_fillna.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_insert.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_is_full.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_repeat.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_shift.cpython-311.pyc
   │        │  │  │  │  │  │  └─ test_to_timestamp.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_asfreq.py
   │        │  │  │  │  │  ├─ test_astype.py
   │        │  │  │  │  │  ├─ test_factorize.py
   │        │  │  │  │  │  ├─ test_fillna.py
   │        │  │  │  │  │  ├─ test_insert.py
   │        │  │  │  │  │  ├─ test_is_full.py
   │        │  │  │  │  │  ├─ test_repeat.py
   │        │  │  │  │  │  ├─ test_shift.py
   │        │  │  │  │  │  └─ test_to_timestamp.py
   │        │  │  │  │  ├─ test_constructors.py
   │        │  │  │  │  ├─ test_formats.py
   │        │  │  │  │  ├─ test_freq_attr.py
   │        │  │  │  │  ├─ test_indexing.py
   │        │  │  │  │  ├─ test_join.py
   │        │  │  │  │  ├─ test_monotonic.py
   │        │  │  │  │  ├─ test_partial_slicing.py
   │        │  │  │  │  ├─ test_period.py
   │        │  │  │  │  ├─ test_period_range.py
   │        │  │  │  │  ├─ test_pickle.py
   │        │  │  │  │  ├─ test_resolution.py
   │        │  │  │  │  ├─ test_scalar_compat.py
   │        │  │  │  │  ├─ test_searchsorted.py
   │        │  │  │  │  ├─ test_setops.py
   │        │  │  │  │  └─ test_tools.py
   │        │  │  │  ├─ ranges
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_constructors.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_join.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_range.cpython-311.pyc
   │        │  │  │  │  │  └─ test_setops.cpython-311.pyc
   │        │  │  │  │  ├─ test_constructors.py
   │        │  │  │  │  ├─ test_indexing.py
   │        │  │  │  │  ├─ test_join.py
   │        │  │  │  │  ├─ test_range.py
   │        │  │  │  │  └─ test_setops.py
   │        │  │  │  ├─ test_any_index.py
   │        │  │  │  ├─ test_base.py
   │        │  │  │  ├─ test_common.py
   │        │  │  │  ├─ test_datetimelike.py
   │        │  │  │  ├─ test_engines.py
   │        │  │  │  ├─ test_frozen.py
   │        │  │  │  ├─ test_index_new.py
   │        │  │  │  ├─ test_indexing.py
   │        │  │  │  ├─ test_numpy_compat.py
   │        │  │  │  ├─ test_old_base.py
   │        │  │  │  ├─ test_setops.py
   │        │  │  │  ├─ test_subclass.py
   │        │  │  │  └─ timedeltas
   │        │  │  │     ├─ __init__.py
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │     │  ├─ test_arithmetic.cpython-311.pyc
   │        │  │  │     │  ├─ test_constructors.cpython-311.pyc
   │        │  │  │     │  ├─ test_delete.cpython-311.pyc
   │        │  │  │     │  ├─ test_formats.cpython-311.pyc
   │        │  │  │     │  ├─ test_freq_attr.cpython-311.pyc
   │        │  │  │     │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │     │  ├─ test_join.cpython-311.pyc
   │        │  │  │     │  ├─ test_ops.cpython-311.pyc
   │        │  │  │     │  ├─ test_pickle.cpython-311.pyc
   │        │  │  │     │  ├─ test_scalar_compat.cpython-311.pyc
   │        │  │  │     │  ├─ test_searchsorted.cpython-311.pyc
   │        │  │  │     │  ├─ test_setops.cpython-311.pyc
   │        │  │  │     │  ├─ test_timedelta.cpython-311.pyc
   │        │  │  │     │  └─ test_timedelta_range.cpython-311.pyc
   │        │  │  │     ├─ methods
   │        │  │  │     │  ├─ __init__.py
   │        │  │  │     │  ├─ __pycache__
   │        │  │  │     │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │     │  │  ├─ test_astype.cpython-311.pyc
   │        │  │  │     │  │  ├─ test_factorize.cpython-311.pyc
   │        │  │  │     │  │  ├─ test_fillna.cpython-311.pyc
   │        │  │  │     │  │  ├─ test_insert.cpython-311.pyc
   │        │  │  │     │  │  ├─ test_repeat.cpython-311.pyc
   │        │  │  │     │  │  └─ test_shift.cpython-311.pyc
   │        │  │  │     │  ├─ test_astype.py
   │        │  │  │     │  ├─ test_factorize.py
   │        │  │  │     │  ├─ test_fillna.py
   │        │  │  │     │  ├─ test_insert.py
   │        │  │  │     │  ├─ test_repeat.py
   │        │  │  │     │  └─ test_shift.py
   │        │  │  │     ├─ test_arithmetic.py
   │        │  │  │     ├─ test_constructors.py
   │        │  │  │     ├─ test_delete.py
   │        │  │  │     ├─ test_formats.py
   │        │  │  │     ├─ test_freq_attr.py
   │        │  │  │     ├─ test_indexing.py
   │        │  │  │     ├─ test_join.py
   │        │  │  │     ├─ test_ops.py
   │        │  │  │     ├─ test_pickle.py
   │        │  │  │     ├─ test_scalar_compat.py
   │        │  │  │     ├─ test_searchsorted.py
   │        │  │  │     ├─ test_setops.py
   │        │  │  │     ├─ test_timedelta.py
   │        │  │  │     └─ test_timedelta_range.py
   │        │  │  ├─ indexing
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ common.cpython-311.pyc
   │        │  │  │  │  ├─ conftest.cpython-311.pyc
   │        │  │  │  │  ├─ test_at.cpython-311.pyc
   │        │  │  │  │  ├─ test_categorical.cpython-311.pyc
   │        │  │  │  │  ├─ test_chaining_and_caching.cpython-311.pyc
   │        │  │  │  │  ├─ test_check_indexer.cpython-311.pyc
   │        │  │  │  │  ├─ test_coercion.cpython-311.pyc
   │        │  │  │  │  ├─ test_datetime.cpython-311.pyc
   │        │  │  │  │  ├─ test_floats.cpython-311.pyc
   │        │  │  │  │  ├─ test_iat.cpython-311.pyc
   │        │  │  │  │  ├─ test_iloc.cpython-311.pyc
   │        │  │  │  │  ├─ test_indexers.cpython-311.pyc
   │        │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  ├─ test_loc.cpython-311.pyc
   │        │  │  │  │  ├─ test_na_indexing.cpython-311.pyc
   │        │  │  │  │  ├─ test_partial.cpython-311.pyc
   │        │  │  │  │  └─ test_scalar.cpython-311.pyc
   │        │  │  │  ├─ common.py
   │        │  │  │  ├─ conftest.py
   │        │  │  │  ├─ interval
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_interval.cpython-311.pyc
   │        │  │  │  │  │  └─ test_interval_new.cpython-311.pyc
   │        │  │  │  │  ├─ test_interval.py
   │        │  │  │  │  └─ test_interval_new.py
   │        │  │  │  ├─ multiindex
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_chaining_and_caching.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_datetime.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_getitem.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_iloc.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_indexing_slow.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_loc.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_multiindex.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_partial.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_setitem.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_slice.cpython-311.pyc
   │        │  │  │  │  │  └─ test_sorted.cpython-311.pyc
   │        │  │  │  │  ├─ test_chaining_and_caching.py
   │        │  │  │  │  ├─ test_datetime.py
   │        │  │  │  │  ├─ test_getitem.py
   │        │  │  │  │  ├─ test_iloc.py
   │        │  │  │  │  ├─ test_indexing_slow.py
   │        │  │  │  │  ├─ test_loc.py
   │        │  │  │  │  ├─ test_multiindex.py
   │        │  │  │  │  ├─ test_partial.py
   │        │  │  │  │  ├─ test_setitem.py
   │        │  │  │  │  ├─ test_slice.py
   │        │  │  │  │  └─ test_sorted.py
   │        │  │  │  ├─ test_at.py
   │        │  │  │  ├─ test_categorical.py
   │        │  │  │  ├─ test_chaining_and_caching.py
   │        │  │  │  ├─ test_check_indexer.py
   │        │  │  │  ├─ test_coercion.py
   │        │  │  │  ├─ test_datetime.py
   │        │  │  │  ├─ test_floats.py
   │        │  │  │  ├─ test_iat.py
   │        │  │  │  ├─ test_iloc.py
   │        │  │  │  ├─ test_indexers.py
   │        │  │  │  ├─ test_indexing.py
   │        │  │  │  ├─ test_loc.py
   │        │  │  │  ├─ test_na_indexing.py
   │        │  │  │  ├─ test_partial.py
   │        │  │  │  └─ test_scalar.py
   │        │  │  ├─ interchange
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test_impl.cpython-311.pyc
   │        │  │  │  │  ├─ test_spec_conformance.cpython-311.pyc
   │        │  │  │  │  └─ test_utils.cpython-311.pyc
   │        │  │  │  ├─ test_impl.py
   │        │  │  │  ├─ test_spec_conformance.py
   │        │  │  │  └─ test_utils.py
   │        │  │  ├─ internals
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test_api.cpython-311.pyc
   │        │  │  │  │  ├─ test_internals.cpython-311.pyc
   │        │  │  │  │  └─ test_managers.cpython-311.pyc
   │        │  │  │  ├─ test_api.py
   │        │  │  │  ├─ test_internals.py
   │        │  │  │  └─ test_managers.py
   │        │  │  ├─ io
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ conftest.cpython-311.pyc
   │        │  │  │  │  ├─ generate_legacy_storage_files.cpython-311.pyc
   │        │  │  │  │  ├─ test_clipboard.cpython-311.pyc
   │        │  │  │  │  ├─ test_common.cpython-311.pyc
   │        │  │  │  │  ├─ test_compression.cpython-311.pyc
   │        │  │  │  │  ├─ test_feather.cpython-311.pyc
   │        │  │  │  │  ├─ test_fsspec.cpython-311.pyc
   │        │  │  │  │  ├─ test_gbq.cpython-311.pyc
   │        │  │  │  │  ├─ test_gcs.cpython-311.pyc
   │        │  │  │  │  ├─ test_html.cpython-311.pyc
   │        │  │  │  │  ├─ test_http_headers.cpython-311.pyc
   │        │  │  │  │  ├─ test_orc.cpython-311.pyc
   │        │  │  │  │  ├─ test_parquet.cpython-311.pyc
   │        │  │  │  │  ├─ test_pickle.cpython-311.pyc
   │        │  │  │  │  ├─ test_s3.cpython-311.pyc
   │        │  │  │  │  ├─ test_spss.cpython-311.pyc
   │        │  │  │  │  ├─ test_sql.cpython-311.pyc
   │        │  │  │  │  └─ test_stata.cpython-311.pyc
   │        │  │  │  ├─ conftest.py
   │        │  │  │  ├─ excel
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_odf.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_odswriter.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_openpyxl.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_readers.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_style.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_writers.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_xlrd.cpython-311.pyc
   │        │  │  │  │  │  └─ test_xlsxwriter.cpython-311.pyc
   │        │  │  │  │  ├─ test_odf.py
   │        │  │  │  │  ├─ test_odswriter.py
   │        │  │  │  │  ├─ test_openpyxl.py
   │        │  │  │  │  ├─ test_readers.py
   │        │  │  │  │  ├─ test_style.py
   │        │  │  │  │  ├─ test_writers.py
   │        │  │  │  │  ├─ test_xlrd.py
   │        │  │  │  │  └─ test_xlsxwriter.py
   │        │  │  │  ├─ formats
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_console.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_css.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_eng_formatting.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_format.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_ipython_compat.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_printing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_to_csv.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_to_excel.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_to_html.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_to_latex.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_to_markdown.cpython-311.pyc
   │        │  │  │  │  │  └─ test_to_string.cpython-311.pyc
   │        │  │  │  │  ├─ style
   │        │  │  │  │  │  ├─ __init__.py
   │        │  │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_bar.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_exceptions.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_format.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_highlight.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_html.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_matplotlib.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_non_unique.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_style.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_to_latex.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_to_string.cpython-311.pyc
   │        │  │  │  │  │  │  └─ test_tooltip.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_bar.py
   │        │  │  │  │  │  ├─ test_exceptions.py
   │        │  │  │  │  │  ├─ test_format.py
   │        │  │  │  │  │  ├─ test_highlight.py
   │        │  │  │  │  │  ├─ test_html.py
   │        │  │  │  │  │  ├─ test_matplotlib.py
   │        │  │  │  │  │  ├─ test_non_unique.py
   │        │  │  │  │  │  ├─ test_style.py
   │        │  │  │  │  │  ├─ test_to_latex.py
   │        │  │  │  │  │  ├─ test_to_string.py
   │        │  │  │  │  │  └─ test_tooltip.py
   │        │  │  │  │  ├─ test_console.py
   │        │  │  │  │  ├─ test_css.py
   │        │  │  │  │  ├─ test_eng_formatting.py
   │        │  │  │  │  ├─ test_format.py
   │        │  │  │  │  ├─ test_ipython_compat.py
   │        │  │  │  │  ├─ test_printing.py
   │        │  │  │  │  ├─ test_to_csv.py
   │        │  │  │  │  ├─ test_to_excel.py
   │        │  │  │  │  ├─ test_to_html.py
   │        │  │  │  │  ├─ test_to_latex.py
   │        │  │  │  │  ├─ test_to_markdown.py
   │        │  │  │  │  └─ test_to_string.py
   │        │  │  │  ├─ generate_legacy_storage_files.py
   │        │  │  │  ├─ json
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ conftest.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_compression.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_deprecated_kwargs.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_json_table_schema.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_json_table_schema_ext_dtype.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_normalize.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_pandas.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_readlines.cpython-311.pyc
   │        │  │  │  │  │  └─ test_ujson.cpython-311.pyc
   │        │  │  │  │  ├─ conftest.py
   │        │  │  │  │  ├─ test_compression.py
   │        │  │  │  │  ├─ test_deprecated_kwargs.py
   │        │  │  │  │  ├─ test_json_table_schema.py
   │        │  │  │  │  ├─ test_json_table_schema_ext_dtype.py
   │        │  │  │  │  ├─ test_normalize.py
   │        │  │  │  │  ├─ test_pandas.py
   │        │  │  │  │  ├─ test_readlines.py
   │        │  │  │  │  └─ test_ujson.py
   │        │  │  │  ├─ parser
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ conftest.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_c_parser_only.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_comment.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_compression.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_concatenate_chunks.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_converters.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_dialect.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_encoding.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_header.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_index_col.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_mangle_dupes.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_multi_thread.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_na_values.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_network.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_parse_dates.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_python_parser_only.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_quoting.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_read_fwf.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_skiprows.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_textreader.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_unsupported.cpython-311.pyc
   │        │  │  │  │  │  └─ test_upcast.cpython-311.pyc
   │        │  │  │  │  ├─ common
   │        │  │  │  │  │  ├─ __init__.py
   │        │  │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_chunksize.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_common_basic.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_data_list.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_decimal.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_file_buffer_url.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_float.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_index.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_inf.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_ints.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_iterator.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_read_errors.cpython-311.pyc
   │        │  │  │  │  │  │  └─ test_verbose.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_chunksize.py
   │        │  │  │  │  │  ├─ test_common_basic.py
   │        │  │  │  │  │  ├─ test_data_list.py
   │        │  │  │  │  │  ├─ test_decimal.py
   │        │  │  │  │  │  ├─ test_file_buffer_url.py
   │        │  │  │  │  │  ├─ test_float.py
   │        │  │  │  │  │  ├─ test_index.py
   │        │  │  │  │  │  ├─ test_inf.py
   │        │  │  │  │  │  ├─ test_ints.py
   │        │  │  │  │  │  ├─ test_iterator.py
   │        │  │  │  │  │  ├─ test_read_errors.py
   │        │  │  │  │  │  └─ test_verbose.py
   │        │  │  │  │  ├─ conftest.py
   │        │  │  │  │  ├─ dtypes
   │        │  │  │  │  │  ├─ __init__.py
   │        │  │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_categorical.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_dtypes_basic.cpython-311.pyc
   │        │  │  │  │  │  │  └─ test_empty.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_categorical.py
   │        │  │  │  │  │  ├─ test_dtypes_basic.py
   │        │  │  │  │  │  └─ test_empty.py
   │        │  │  │  │  ├─ test_c_parser_only.py
   │        │  │  │  │  ├─ test_comment.py
   │        │  │  │  │  ├─ test_compression.py
   │        │  │  │  │  ├─ test_concatenate_chunks.py
   │        │  │  │  │  ├─ test_converters.py
   │        │  │  │  │  ├─ test_dialect.py
   │        │  │  │  │  ├─ test_encoding.py
   │        │  │  │  │  ├─ test_header.py
   │        │  │  │  │  ├─ test_index_col.py
   │        │  │  │  │  ├─ test_mangle_dupes.py
   │        │  │  │  │  ├─ test_multi_thread.py
   │        │  │  │  │  ├─ test_na_values.py
   │        │  │  │  │  ├─ test_network.py
   │        │  │  │  │  ├─ test_parse_dates.py
   │        │  │  │  │  ├─ test_python_parser_only.py
   │        │  │  │  │  ├─ test_quoting.py
   │        │  │  │  │  ├─ test_read_fwf.py
   │        │  │  │  │  ├─ test_skiprows.py
   │        │  │  │  │  ├─ test_textreader.py
   │        │  │  │  │  ├─ test_unsupported.py
   │        │  │  │  │  ├─ test_upcast.py
   │        │  │  │  │  └─ usecols
   │        │  │  │  │     ├─ __init__.py
   │        │  │  │  │     ├─ __pycache__
   │        │  │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │     │  ├─ test_parse_dates.cpython-311.pyc
   │        │  │  │  │     │  ├─ test_strings.cpython-311.pyc
   │        │  │  │  │     │  └─ test_usecols_basic.cpython-311.pyc
   │        │  │  │  │     ├─ test_parse_dates.py
   │        │  │  │  │     ├─ test_strings.py
   │        │  │  │  │     └─ test_usecols_basic.py
   │        │  │  │  ├─ pytables
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ common.cpython-311.pyc
   │        │  │  │  │  │  ├─ conftest.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_append.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_categorical.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_compat.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_complex.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_errors.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_file_handling.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_keys.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_put.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_pytables_missing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_read.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_retain_attributes.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_round_trip.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_select.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_store.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_subclass.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_time_series.cpython-311.pyc
   │        │  │  │  │  │  └─ test_timezones.cpython-311.pyc
   │        │  │  │  │  ├─ common.py
   │        │  │  │  │  ├─ conftest.py
   │        │  │  │  │  ├─ test_append.py
   │        │  │  │  │  ├─ test_categorical.py
   │        │  │  │  │  ├─ test_compat.py
   │        │  │  │  │  ├─ test_complex.py
   │        │  │  │  │  ├─ test_errors.py
   │        │  │  │  │  ├─ test_file_handling.py
   │        │  │  │  │  ├─ test_keys.py
   │        │  │  │  │  ├─ test_put.py
   │        │  │  │  │  ├─ test_pytables_missing.py
   │        │  │  │  │  ├─ test_read.py
   │        │  │  │  │  ├─ test_retain_attributes.py
   │        │  │  │  │  ├─ test_round_trip.py
   │        │  │  │  │  ├─ test_select.py
   │        │  │  │  │  ├─ test_store.py
   │        │  │  │  │  ├─ test_subclass.py
   │        │  │  │  │  ├─ test_time_series.py
   │        │  │  │  │  └─ test_timezones.py
   │        │  │  │  ├─ sas
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_byteswap.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_sas.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_sas7bdat.cpython-311.pyc
   │        │  │  │  │  │  └─ test_xport.cpython-311.pyc
   │        │  │  │  │  ├─ test_byteswap.py
   │        │  │  │  │  ├─ test_sas.py
   │        │  │  │  │  ├─ test_sas7bdat.py
   │        │  │  │  │  └─ test_xport.py
   │        │  │  │  ├─ test_clipboard.py
   │        │  │  │  ├─ test_common.py
   │        │  │  │  ├─ test_compression.py
   │        │  │  │  ├─ test_feather.py
   │        │  │  │  ├─ test_fsspec.py
   │        │  │  │  ├─ test_gbq.py
   │        │  │  │  ├─ test_gcs.py
   │        │  │  │  ├─ test_html.py
   │        │  │  │  ├─ test_http_headers.py
   │        │  │  │  ├─ test_orc.py
   │        │  │  │  ├─ test_parquet.py
   │        │  │  │  ├─ test_pickle.py
   │        │  │  │  ├─ test_s3.py
   │        │  │  │  ├─ test_spss.py
   │        │  │  │  ├─ test_sql.py
   │        │  │  │  ├─ test_stata.py
   │        │  │  │  └─ xml
   │        │  │  │     ├─ __init__.py
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │     │  ├─ conftest.cpython-311.pyc
   │        │  │  │     │  ├─ test_to_xml.cpython-311.pyc
   │        │  │  │     │  ├─ test_xml.cpython-311.pyc
   │        │  │  │     │  └─ test_xml_dtypes.cpython-311.pyc
   │        │  │  │     ├─ conftest.py
   │        │  │  │     ├─ test_to_xml.py
   │        │  │  │     ├─ test_xml.py
   │        │  │  │     └─ test_xml_dtypes.py
   │        │  │  ├─ libs
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test_hashtable.cpython-311.pyc
   │        │  │  │  │  ├─ test_join.cpython-311.pyc
   │        │  │  │  │  ├─ test_lib.cpython-311.pyc
   │        │  │  │  │  └─ test_libalgos.cpython-311.pyc
   │        │  │  │  ├─ test_hashtable.py
   │        │  │  │  ├─ test_join.py
   │        │  │  │  ├─ test_lib.py
   │        │  │  │  └─ test_libalgos.py
   │        │  │  ├─ plotting
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ common.cpython-311.pyc
   │        │  │  │  │  ├─ conftest.cpython-311.pyc
   │        │  │  │  │  ├─ test_backend.cpython-311.pyc
   │        │  │  │  │  ├─ test_boxplot_method.cpython-311.pyc
   │        │  │  │  │  ├─ test_common.cpython-311.pyc
   │        │  │  │  │  ├─ test_converter.cpython-311.pyc
   │        │  │  │  │  ├─ test_datetimelike.cpython-311.pyc
   │        │  │  │  │  ├─ test_groupby.cpython-311.pyc
   │        │  │  │  │  ├─ test_hist_method.cpython-311.pyc
   │        │  │  │  │  ├─ test_misc.cpython-311.pyc
   │        │  │  │  │  ├─ test_series.cpython-311.pyc
   │        │  │  │  │  └─ test_style.cpython-311.pyc
   │        │  │  │  ├─ common.py
   │        │  │  │  ├─ conftest.py
   │        │  │  │  ├─ frame
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_frame.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_frame_color.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_frame_groupby.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_frame_legend.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_frame_subplots.cpython-311.pyc
   │        │  │  │  │  │  └─ test_hist_box_by.cpython-311.pyc
   │        │  │  │  │  ├─ test_frame.py
   │        │  │  │  │  ├─ test_frame_color.py
   │        │  │  │  │  ├─ test_frame_groupby.py
   │        │  │  │  │  ├─ test_frame_legend.py
   │        │  │  │  │  ├─ test_frame_subplots.py
   │        │  │  │  │  └─ test_hist_box_by.py
   │        │  │  │  ├─ test_backend.py
   │        │  │  │  ├─ test_boxplot_method.py
   │        │  │  │  ├─ test_common.py
   │        │  │  │  ├─ test_converter.py
   │        │  │  │  ├─ test_datetimelike.py
   │        │  │  │  ├─ test_groupby.py
   │        │  │  │  ├─ test_hist_method.py
   │        │  │  │  ├─ test_misc.py
   │        │  │  │  ├─ test_series.py
   │        │  │  │  └─ test_style.py
   │        │  │  ├─ reductions
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test_reductions.cpython-311.pyc
   │        │  │  │  │  └─ test_stat_reductions.cpython-311.pyc
   │        │  │  │  ├─ test_reductions.py
   │        │  │  │  └─ test_stat_reductions.py
   │        │  │  ├─ resample
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ conftest.cpython-311.pyc
   │        │  │  │  │  ├─ test_base.cpython-311.pyc
   │        │  │  │  │  ├─ test_datetime_index.cpython-311.pyc
   │        │  │  │  │  ├─ test_period_index.cpython-311.pyc
   │        │  │  │  │  ├─ test_resample_api.cpython-311.pyc
   │        │  │  │  │  ├─ test_resampler_grouper.cpython-311.pyc
   │        │  │  │  │  ├─ test_time_grouper.cpython-311.pyc
   │        │  │  │  │  └─ test_timedelta.cpython-311.pyc
   │        │  │  │  ├─ conftest.py
   │        │  │  │  ├─ test_base.py
   │        │  │  │  ├─ test_datetime_index.py
   │        │  │  │  ├─ test_period_index.py
   │        │  │  │  ├─ test_resample_api.py
   │        │  │  │  ├─ test_resampler_grouper.py
   │        │  │  │  ├─ test_time_grouper.py
   │        │  │  │  └─ test_timedelta.py
   │        │  │  ├─ reshape
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test_crosstab.cpython-311.pyc
   │        │  │  │  │  ├─ test_cut.cpython-311.pyc
   │        │  │  │  │  ├─ test_from_dummies.cpython-311.pyc
   │        │  │  │  │  ├─ test_get_dummies.cpython-311.pyc
   │        │  │  │  │  ├─ test_melt.cpython-311.pyc
   │        │  │  │  │  ├─ test_pivot.cpython-311.pyc
   │        │  │  │  │  ├─ test_pivot_multilevel.cpython-311.pyc
   │        │  │  │  │  ├─ test_qcut.cpython-311.pyc
   │        │  │  │  │  ├─ test_union_categoricals.cpython-311.pyc
   │        │  │  │  │  └─ test_util.cpython-311.pyc
   │        │  │  │  ├─ concat
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ conftest.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_append.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_append_common.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_categorical.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_concat.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_dataframe.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_datetimes.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_empty.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_index.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_invalid.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_series.cpython-311.pyc
   │        │  │  │  │  │  └─ test_sort.cpython-311.pyc
   │        │  │  │  │  ├─ conftest.py
   │        │  │  │  │  ├─ test_append.py
   │        │  │  │  │  ├─ test_append_common.py
   │        │  │  │  │  ├─ test_categorical.py
   │        │  │  │  │  ├─ test_concat.py
   │        │  │  │  │  ├─ test_dataframe.py
   │        │  │  │  │  ├─ test_datetimes.py
   │        │  │  │  │  ├─ test_empty.py
   │        │  │  │  │  ├─ test_index.py
   │        │  │  │  │  ├─ test_invalid.py
   │        │  │  │  │  ├─ test_series.py
   │        │  │  │  │  └─ test_sort.py
   │        │  │  │  ├─ merge
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_join.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_merge.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_merge_asof.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_merge_cross.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_merge_index_as_string.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_merge_ordered.cpython-311.pyc
   │        │  │  │  │  │  └─ test_multi.cpython-311.pyc
   │        │  │  │  │  ├─ test_join.py
   │        │  │  │  │  ├─ test_merge.py
   │        │  │  │  │  ├─ test_merge_asof.py
   │        │  │  │  │  ├─ test_merge_cross.py
   │        │  │  │  │  ├─ test_merge_index_as_string.py
   │        │  │  │  │  ├─ test_merge_ordered.py
   │        │  │  │  │  └─ test_multi.py
   │        │  │  │  ├─ test_crosstab.py
   │        │  │  │  ├─ test_cut.py
   │        │  │  │  ├─ test_from_dummies.py
   │        │  │  │  ├─ test_get_dummies.py
   │        │  │  │  ├─ test_melt.py
   │        │  │  │  ├─ test_pivot.py
   │        │  │  │  ├─ test_pivot_multilevel.py
   │        │  │  │  ├─ test_qcut.py
   │        │  │  │  ├─ test_union_categoricals.py
   │        │  │  │  └─ test_util.py
   │        │  │  ├─ scalar
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test_na_scalar.cpython-311.pyc
   │        │  │  │  │  └─ test_nat.cpython-311.pyc
   │        │  │  │  ├─ interval
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_arithmetic.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_constructors.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_contains.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_formats.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_interval.cpython-311.pyc
   │        │  │  │  │  │  └─ test_overlaps.cpython-311.pyc
   │        │  │  │  │  ├─ test_arithmetic.py
   │        │  │  │  │  ├─ test_constructors.py
   │        │  │  │  │  ├─ test_contains.py
   │        │  │  │  │  ├─ test_formats.py
   │        │  │  │  │  ├─ test_interval.py
   │        │  │  │  │  └─ test_overlaps.py
   │        │  │  │  ├─ period
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_arithmetic.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_asfreq.cpython-311.pyc
   │        │  │  │  │  │  └─ test_period.cpython-311.pyc
   │        │  │  │  │  ├─ test_arithmetic.py
   │        │  │  │  │  ├─ test_asfreq.py
   │        │  │  │  │  └─ test_period.py
   │        │  │  │  ├─ test_na_scalar.py
   │        │  │  │  ├─ test_nat.py
   │        │  │  │  ├─ timedelta
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_arithmetic.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_constructors.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_formats.cpython-311.pyc
   │        │  │  │  │  │  └─ test_timedelta.cpython-311.pyc
   │        │  │  │  │  ├─ methods
   │        │  │  │  │  │  ├─ __init__.py
   │        │  │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ test_as_unit.cpython-311.pyc
   │        │  │  │  │  │  │  └─ test_round.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_as_unit.py
   │        │  │  │  │  │  └─ test_round.py
   │        │  │  │  │  ├─ test_arithmetic.py
   │        │  │  │  │  ├─ test_constructors.py
   │        │  │  │  │  ├─ test_formats.py
   │        │  │  │  │  └─ test_timedelta.py
   │        │  │  │  └─ timestamp
   │        │  │  │     ├─ __init__.py
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │     │  ├─ test_arithmetic.cpython-311.pyc
   │        │  │  │     │  ├─ test_comparisons.cpython-311.pyc
   │        │  │  │     │  ├─ test_constructors.cpython-311.pyc
   │        │  │  │     │  ├─ test_formats.cpython-311.pyc
   │        │  │  │     │  ├─ test_timestamp.cpython-311.pyc
   │        │  │  │     │  └─ test_timezones.cpython-311.pyc
   │        │  │  │     ├─ methods
   │        │  │  │     │  ├─ __init__.py
   │        │  │  │     │  ├─ __pycache__
   │        │  │  │     │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │     │  │  ├─ test_as_unit.cpython-311.pyc
   │        │  │  │     │  │  ├─ test_normalize.cpython-311.pyc
   │        │  │  │     │  │  ├─ test_replace.cpython-311.pyc
   │        │  │  │     │  │  ├─ test_round.cpython-311.pyc
   │        │  │  │     │  │  ├─ test_timestamp_method.cpython-311.pyc
   │        │  │  │     │  │  ├─ test_to_julian_date.cpython-311.pyc
   │        │  │  │     │  │  ├─ test_to_pydatetime.cpython-311.pyc
   │        │  │  │     │  │  ├─ test_tz_convert.cpython-311.pyc
   │        │  │  │     │  │  └─ test_tz_localize.cpython-311.pyc
   │        │  │  │     │  ├─ test_as_unit.py
   │        │  │  │     │  ├─ test_normalize.py
   │        │  │  │     │  ├─ test_replace.py
   │        │  │  │     │  ├─ test_round.py
   │        │  │  │     │  ├─ test_timestamp_method.py
   │        │  │  │     │  ├─ test_to_julian_date.py
   │        │  │  │     │  ├─ test_to_pydatetime.py
   │        │  │  │     │  ├─ test_tz_convert.py
   │        │  │  │     │  └─ test_tz_localize.py
   │        │  │  │     ├─ test_arithmetic.py
   │        │  │  │     ├─ test_comparisons.py
   │        │  │  │     ├─ test_constructors.py
   │        │  │  │     ├─ test_formats.py
   │        │  │  │     ├─ test_timestamp.py
   │        │  │  │     └─ test_timezones.py
   │        │  │  ├─ series
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test_api.cpython-311.pyc
   │        │  │  │  │  ├─ test_arithmetic.cpython-311.pyc
   │        │  │  │  │  ├─ test_constructors.cpython-311.pyc
   │        │  │  │  │  ├─ test_cumulative.cpython-311.pyc
   │        │  │  │  │  ├─ test_formats.cpython-311.pyc
   │        │  │  │  │  ├─ test_iteration.cpython-311.pyc
   │        │  │  │  │  ├─ test_logical_ops.cpython-311.pyc
   │        │  │  │  │  ├─ test_missing.cpython-311.pyc
   │        │  │  │  │  ├─ test_npfuncs.cpython-311.pyc
   │        │  │  │  │  ├─ test_reductions.cpython-311.pyc
   │        │  │  │  │  ├─ test_subclass.cpython-311.pyc
   │        │  │  │  │  ├─ test_ufunc.cpython-311.pyc
   │        │  │  │  │  ├─ test_unary.cpython-311.pyc
   │        │  │  │  │  └─ test_validate.cpython-311.pyc
   │        │  │  │  ├─ accessors
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_cat_accessor.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_dt_accessor.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_list_accessor.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_sparse_accessor.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_str_accessor.cpython-311.pyc
   │        │  │  │  │  │  └─ test_struct_accessor.cpython-311.pyc
   │        │  │  │  │  ├─ test_cat_accessor.py
   │        │  │  │  │  ├─ test_dt_accessor.py
   │        │  │  │  │  ├─ test_list_accessor.py
   │        │  │  │  │  ├─ test_sparse_accessor.py
   │        │  │  │  │  ├─ test_str_accessor.py
   │        │  │  │  │  └─ test_struct_accessor.py
   │        │  │  │  ├─ indexing
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_datetime.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_delitem.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_get.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_getitem.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_indexing.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_mask.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_set_value.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_setitem.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_take.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_where.cpython-311.pyc
   │        │  │  │  │  │  └─ test_xs.cpython-311.pyc
   │        │  │  │  │  ├─ test_datetime.py
   │        │  │  │  │  ├─ test_delitem.py
   │        │  │  │  │  ├─ test_get.py
   │        │  │  │  │  ├─ test_getitem.py
   │        │  │  │  │  ├─ test_indexing.py
   │        │  │  │  │  ├─ test_mask.py
   │        │  │  │  │  ├─ test_set_value.py
   │        │  │  │  │  ├─ test_setitem.py
   │        │  │  │  │  ├─ test_take.py
   │        │  │  │  │  ├─ test_where.py
   │        │  │  │  │  └─ test_xs.py
   │        │  │  │  ├─ methods
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_add_prefix_suffix.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_align.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_argsort.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_asof.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_astype.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_autocorr.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_between.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_case_when.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_clip.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_combine.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_combine_first.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_compare.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_convert_dtypes.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_copy.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_count.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_cov_corr.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_describe.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_diff.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_drop.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_drop_duplicates.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_dropna.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_dtypes.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_duplicated.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_equals.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_explode.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_fillna.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_get_numeric_data.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_head_tail.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_infer_objects.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_info.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_interpolate.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_is_monotonic.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_is_unique.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_isin.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_isna.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_item.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_map.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_matmul.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_nlargest.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_nunique.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_pct_change.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_pop.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_quantile.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_rank.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_reindex.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_reindex_like.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_rename.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_rename_axis.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_repeat.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_replace.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_reset_index.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_round.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_searchsorted.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_set_name.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_size.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_sort_index.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_sort_values.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_to_csv.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_to_dict.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_to_frame.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_to_numpy.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_tolist.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_truncate.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_tz_localize.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_unique.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_unstack.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_update.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_value_counts.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_values.cpython-311.pyc
   │        │  │  │  │  │  └─ test_view.cpython-311.pyc
   │        │  │  │  │  ├─ test_add_prefix_suffix.py
   │        │  │  │  │  ├─ test_align.py
   │        │  │  │  │  ├─ test_argsort.py
   │        │  │  │  │  ├─ test_asof.py
   │        │  │  │  │  ├─ test_astype.py
   │        │  │  │  │  ├─ test_autocorr.py
   │        │  │  │  │  ├─ test_between.py
   │        │  │  │  │  ├─ test_case_when.py
   │        │  │  │  │  ├─ test_clip.py
   │        │  │  │  │  ├─ test_combine.py
   │        │  │  │  │  ├─ test_combine_first.py
   │        │  │  │  │  ├─ test_compare.py
   │        │  │  │  │  ├─ test_convert_dtypes.py
   │        │  │  │  │  ├─ test_copy.py
   │        │  │  │  │  ├─ test_count.py
   │        │  │  │  │  ├─ test_cov_corr.py
   │        │  │  │  │  ├─ test_describe.py
   │        │  │  │  │  ├─ test_diff.py
   │        │  │  │  │  ├─ test_drop.py
   │        │  │  │  │  ├─ test_drop_duplicates.py
   │        │  │  │  │  ├─ test_dropna.py
   │        │  │  │  │  ├─ test_dtypes.py
   │        │  │  │  │  ├─ test_duplicated.py
   │        │  │  │  │  ├─ test_equals.py
   │        │  │  │  │  ├─ test_explode.py
   │        │  │  │  │  ├─ test_fillna.py
   │        │  │  │  │  ├─ test_get_numeric_data.py
   │        │  │  │  │  ├─ test_head_tail.py
   │        │  │  │  │  ├─ test_infer_objects.py
   │        │  │  │  │  ├─ test_info.py
   │        │  │  │  │  ├─ test_interpolate.py
   │        │  │  │  │  ├─ test_is_monotonic.py
   │        │  │  │  │  ├─ test_is_unique.py
   │        │  │  │  │  ├─ test_isin.py
   │        │  │  │  │  ├─ test_isna.py
   │        │  │  │  │  ├─ test_item.py
   │        │  │  │  │  ├─ test_map.py
   │        │  │  │  │  ├─ test_matmul.py
   │        │  │  │  │  ├─ test_nlargest.py
   │        │  │  │  │  ├─ test_nunique.py
   │        │  │  │  │  ├─ test_pct_change.py
   │        │  │  │  │  ├─ test_pop.py
   │        │  │  │  │  ├─ test_quantile.py
   │        │  │  │  │  ├─ test_rank.py
   │        │  │  │  │  ├─ test_reindex.py
   │        │  │  │  │  ├─ test_reindex_like.py
   │        │  │  │  │  ├─ test_rename.py
   │        │  │  │  │  ├─ test_rename_axis.py
   │        │  │  │  │  ├─ test_repeat.py
   │        │  │  │  │  ├─ test_replace.py
   │        │  │  │  │  ├─ test_reset_index.py
   │        │  │  │  │  ├─ test_round.py
   │        │  │  │  │  ├─ test_searchsorted.py
   │        │  │  │  │  ├─ test_set_name.py
   │        │  │  │  │  ├─ test_size.py
   │        │  │  │  │  ├─ test_sort_index.py
   │        │  │  │  │  ├─ test_sort_values.py
   │        │  │  │  │  ├─ test_to_csv.py
   │        │  │  │  │  ├─ test_to_dict.py
   │        │  │  │  │  ├─ test_to_frame.py
   │        │  │  │  │  ├─ test_to_numpy.py
   │        │  │  │  │  ├─ test_tolist.py
   │        │  │  │  │  ├─ test_truncate.py
   │        │  │  │  │  ├─ test_tz_localize.py
   │        │  │  │  │  ├─ test_unique.py
   │        │  │  │  │  ├─ test_unstack.py
   │        │  │  │  │  ├─ test_update.py
   │        │  │  │  │  ├─ test_value_counts.py
   │        │  │  │  │  ├─ test_values.py
   │        │  │  │  │  └─ test_view.py
   │        │  │  │  ├─ test_api.py
   │        │  │  │  ├─ test_arithmetic.py
   │        │  │  │  ├─ test_constructors.py
   │        │  │  │  ├─ test_cumulative.py
   │        │  │  │  ├─ test_formats.py
   │        │  │  │  ├─ test_iteration.py
   │        │  │  │  ├─ test_logical_ops.py
   │        │  │  │  ├─ test_missing.py
   │        │  │  │  ├─ test_npfuncs.py
   │        │  │  │  ├─ test_reductions.py
   │        │  │  │  ├─ test_subclass.py
   │        │  │  │  ├─ test_ufunc.py
   │        │  │  │  ├─ test_unary.py
   │        │  │  │  └─ test_validate.py
   │        │  │  ├─ strings
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ conftest.cpython-311.pyc
   │        │  │  │  │  ├─ test_api.cpython-311.pyc
   │        │  │  │  │  ├─ test_case_justify.cpython-311.pyc
   │        │  │  │  │  ├─ test_cat.cpython-311.pyc
   │        │  │  │  │  ├─ test_extract.cpython-311.pyc
   │        │  │  │  │  ├─ test_find_replace.cpython-311.pyc
   │        │  │  │  │  ├─ test_get_dummies.cpython-311.pyc
   │        │  │  │  │  ├─ test_split_partition.cpython-311.pyc
   │        │  │  │  │  ├─ test_string_array.cpython-311.pyc
   │        │  │  │  │  └─ test_strings.cpython-311.pyc
   │        │  │  │  ├─ conftest.py
   │        │  │  │  ├─ test_api.py
   │        │  │  │  ├─ test_case_justify.py
   │        │  │  │  ├─ test_cat.py
   │        │  │  │  ├─ test_extract.py
   │        │  │  │  ├─ test_find_replace.py
   │        │  │  │  ├─ test_get_dummies.py
   │        │  │  │  ├─ test_split_partition.py
   │        │  │  │  ├─ test_string_array.py
   │        │  │  │  └─ test_strings.py
   │        │  │  ├─ test_aggregation.py
   │        │  │  ├─ test_algos.py
   │        │  │  ├─ test_common.py
   │        │  │  ├─ test_downstream.py
   │        │  │  ├─ test_errors.py
   │        │  │  ├─ test_expressions.py
   │        │  │  ├─ test_flags.py
   │        │  │  ├─ test_multilevel.py
   │        │  │  ├─ test_nanops.py
   │        │  │  ├─ test_optional_dependency.py
   │        │  │  ├─ test_register_accessor.py
   │        │  │  ├─ test_sorting.py
   │        │  │  ├─ test_take.py
   │        │  │  ├─ tools
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test_to_datetime.cpython-311.pyc
   │        │  │  │  │  ├─ test_to_numeric.cpython-311.pyc
   │        │  │  │  │  ├─ test_to_time.cpython-311.pyc
   │        │  │  │  │  └─ test_to_timedelta.cpython-311.pyc
   │        │  │  │  ├─ test_to_datetime.py
   │        │  │  │  ├─ test_to_numeric.py
   │        │  │  │  ├─ test_to_time.py
   │        │  │  │  └─ test_to_timedelta.py
   │        │  │  ├─ tseries
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  │  ├─ frequencies
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_freq_code.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_frequencies.cpython-311.pyc
   │        │  │  │  │  │  └─ test_inference.cpython-311.pyc
   │        │  │  │  │  ├─ test_freq_code.py
   │        │  │  │  │  ├─ test_frequencies.py
   │        │  │  │  │  └─ test_inference.py
   │        │  │  │  ├─ holiday
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_calendar.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_federal.cpython-311.pyc
   │        │  │  │  │  │  ├─ test_holiday.cpython-311.pyc
   │        │  │  │  │  │  └─ test_observance.cpython-311.pyc
   │        │  │  │  │  ├─ test_calendar.py
   │        │  │  │  │  ├─ test_federal.py
   │        │  │  │  │  ├─ test_holiday.py
   │        │  │  │  │  └─ test_observance.py
   │        │  │  │  └─ offsets
   │        │  │  │     ├─ __init__.py
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │     │  ├─ common.cpython-311.pyc
   │        │  │  │     │  ├─ test_business_day.cpython-311.pyc
   │        │  │  │     │  ├─ test_business_hour.cpython-311.pyc
   │        │  │  │     │  ├─ test_business_month.cpython-311.pyc
   │        │  │  │     │  ├─ test_business_quarter.cpython-311.pyc
   │        │  │  │     │  ├─ test_business_year.cpython-311.pyc
   │        │  │  │     │  ├─ test_common.cpython-311.pyc
   │        │  │  │     │  ├─ test_custom_business_day.cpython-311.pyc
   │        │  │  │     │  ├─ test_custom_business_hour.cpython-311.pyc
   │        │  │  │     │  ├─ test_custom_business_month.cpython-311.pyc
   │        │  │  │     │  ├─ test_dst.cpython-311.pyc
   │        │  │  │     │  ├─ test_easter.cpython-311.pyc
   │        │  │  │     │  ├─ test_fiscal.cpython-311.pyc
   │        │  │  │     │  ├─ test_index.cpython-311.pyc
   │        │  │  │     │  ├─ test_month.cpython-311.pyc
   │        │  │  │     │  ├─ test_offsets.cpython-311.pyc
   │        │  │  │     │  ├─ test_offsets_properties.cpython-311.pyc
   │        │  │  │     │  ├─ test_quarter.cpython-311.pyc
   │        │  │  │     │  ├─ test_ticks.cpython-311.pyc
   │        │  │  │     │  ├─ test_week.cpython-311.pyc
   │        │  │  │     │  └─ test_year.cpython-311.pyc
   │        │  │  │     ├─ common.py
   │        │  │  │     ├─ test_business_day.py
   │        │  │  │     ├─ test_business_hour.py
   │        │  │  │     ├─ test_business_month.py
   │        │  │  │     ├─ test_business_quarter.py
   │        │  │  │     ├─ test_business_year.py
   │        │  │  │     ├─ test_common.py
   │        │  │  │     ├─ test_custom_business_day.py
   │        │  │  │     ├─ test_custom_business_hour.py
   │        │  │  │     ├─ test_custom_business_month.py
   │        │  │  │     ├─ test_dst.py
   │        │  │  │     ├─ test_easter.py
   │        │  │  │     ├─ test_fiscal.py
   │        │  │  │     ├─ test_index.py
   │        │  │  │     ├─ test_month.py
   │        │  │  │     ├─ test_offsets.py
   │        │  │  │     ├─ test_offsets_properties.py
   │        │  │  │     ├─ test_quarter.py
   │        │  │  │     ├─ test_ticks.py
   │        │  │  │     ├─ test_week.py
   │        │  │  │     └─ test_year.py
   │        │  │  ├─ tslibs
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test_api.cpython-311.pyc
   │        │  │  │  │  ├─ test_array_to_datetime.cpython-311.pyc
   │        │  │  │  │  ├─ test_ccalendar.cpython-311.pyc
   │        │  │  │  │  ├─ test_conversion.cpython-311.pyc
   │        │  │  │  │  ├─ test_fields.cpython-311.pyc
   │        │  │  │  │  ├─ test_libfrequencies.cpython-311.pyc
   │        │  │  │  │  ├─ test_liboffsets.cpython-311.pyc
   │        │  │  │  │  ├─ test_np_datetime.cpython-311.pyc
   │        │  │  │  │  ├─ test_npy_units.cpython-311.pyc
   │        │  │  │  │  ├─ test_parse_iso8601.cpython-311.pyc
   │        │  │  │  │  ├─ test_parsing.cpython-311.pyc
   │        │  │  │  │  ├─ test_period.cpython-311.pyc
   │        │  │  │  │  ├─ test_resolution.cpython-311.pyc
   │        │  │  │  │  ├─ test_strptime.cpython-311.pyc
   │        │  │  │  │  ├─ test_timedeltas.cpython-311.pyc
   │        │  │  │  │  ├─ test_timezones.cpython-311.pyc
   │        │  │  │  │  ├─ test_to_offset.cpython-311.pyc
   │        │  │  │  │  └─ test_tzconversion.cpython-311.pyc
   │        │  │  │  ├─ test_api.py
   │        │  │  │  ├─ test_array_to_datetime.py
   │        │  │  │  ├─ test_ccalendar.py
   │        │  │  │  ├─ test_conversion.py
   │        │  │  │  ├─ test_fields.py
   │        │  │  │  ├─ test_libfrequencies.py
   │        │  │  │  ├─ test_liboffsets.py
   │        │  │  │  ├─ test_np_datetime.py
   │        │  │  │  ├─ test_npy_units.py
   │        │  │  │  ├─ test_parse_iso8601.py
   │        │  │  │  ├─ test_parsing.py
   │        │  │  │  ├─ test_period.py
   │        │  │  │  ├─ test_resolution.py
   │        │  │  │  ├─ test_strptime.py
   │        │  │  │  ├─ test_timedeltas.py
   │        │  │  │  ├─ test_timezones.py
   │        │  │  │  ├─ test_to_offset.py
   │        │  │  │  └─ test_tzconversion.py
   │        │  │  ├─ util
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ conftest.cpython-311.pyc
   │        │  │  │  │  ├─ test_assert_almost_equal.cpython-311.pyc
   │        │  │  │  │  ├─ test_assert_attr_equal.cpython-311.pyc
   │        │  │  │  │  ├─ test_assert_categorical_equal.cpython-311.pyc
   │        │  │  │  │  ├─ test_assert_extension_array_equal.cpython-311.pyc
   │        │  │  │  │  ├─ test_assert_frame_equal.cpython-311.pyc
   │        │  │  │  │  ├─ test_assert_index_equal.cpython-311.pyc
   │        │  │  │  │  ├─ test_assert_interval_array_equal.cpython-311.pyc
   │        │  │  │  │  ├─ test_assert_numpy_array_equal.cpython-311.pyc
   │        │  │  │  │  ├─ test_assert_produces_warning.cpython-311.pyc
   │        │  │  │  │  ├─ test_assert_series_equal.cpython-311.pyc
   │        │  │  │  │  ├─ test_deprecate.cpython-311.pyc
   │        │  │  │  │  ├─ test_deprecate_kwarg.cpython-311.pyc
   │        │  │  │  │  ├─ test_deprecate_nonkeyword_arguments.cpython-311.pyc
   │        │  │  │  │  ├─ test_doc.cpython-311.pyc
   │        │  │  │  │  ├─ test_hashing.cpython-311.pyc
   │        │  │  │  │  ├─ test_numba.cpython-311.pyc
   │        │  │  │  │  ├─ test_rewrite_warning.cpython-311.pyc
   │        │  │  │  │  ├─ test_shares_memory.cpython-311.pyc
   │        │  │  │  │  ├─ test_show_versions.cpython-311.pyc
   │        │  │  │  │  ├─ test_util.cpython-311.pyc
   │        │  │  │  │  ├─ test_validate_args.cpython-311.pyc
   │        │  │  │  │  ├─ test_validate_args_and_kwargs.cpython-311.pyc
   │        │  │  │  │  ├─ test_validate_inclusive.cpython-311.pyc
   │        │  │  │  │  └─ test_validate_kwargs.cpython-311.pyc
   │        │  │  │  ├─ conftest.py
   │        │  │  │  ├─ test_assert_almost_equal.py
   │        │  │  │  ├─ test_assert_attr_equal.py
   │        │  │  │  ├─ test_assert_categorical_equal.py
   │        │  │  │  ├─ test_assert_extension_array_equal.py
   │        │  │  │  ├─ test_assert_frame_equal.py
   │        │  │  │  ├─ test_assert_index_equal.py
   │        │  │  │  ├─ test_assert_interval_array_equal.py
   │        │  │  │  ├─ test_assert_numpy_array_equal.py
   │        │  │  │  ├─ test_assert_produces_warning.py
   │        │  │  │  ├─ test_assert_series_equal.py
   │        │  │  │  ├─ test_deprecate.py
   │        │  │  │  ├─ test_deprecate_kwarg.py
   │        │  │  │  ├─ test_deprecate_nonkeyword_arguments.py
   │        │  │  │  ├─ test_doc.py
   │        │  │  │  ├─ test_hashing.py
   │        │  │  │  ├─ test_numba.py
   │        │  │  │  ├─ test_rewrite_warning.py
   │        │  │  │  ├─ test_shares_memory.py
   │        │  │  │  ├─ test_show_versions.py
   │        │  │  │  ├─ test_util.py
   │        │  │  │  ├─ test_validate_args.py
   │        │  │  │  ├─ test_validate_args_and_kwargs.py
   │        │  │  │  ├─ test_validate_inclusive.py
   │        │  │  │  └─ test_validate_kwargs.py
   │        │  │  └─ window
   │        │  │     ├─ __init__.py
   │        │  │     ├─ __pycache__
   │        │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │     │  ├─ conftest.cpython-311.pyc
   │        │  │     │  ├─ test_api.cpython-311.pyc
   │        │  │     │  ├─ test_apply.cpython-311.pyc
   │        │  │     │  ├─ test_base_indexer.cpython-311.pyc
   │        │  │     │  ├─ test_cython_aggregations.cpython-311.pyc
   │        │  │     │  ├─ test_dtypes.cpython-311.pyc
   │        │  │     │  ├─ test_ewm.cpython-311.pyc
   │        │  │     │  ├─ test_expanding.cpython-311.pyc
   │        │  │     │  ├─ test_groupby.cpython-311.pyc
   │        │  │     │  ├─ test_numba.cpython-311.pyc
   │        │  │     │  ├─ test_online.cpython-311.pyc
   │        │  │     │  ├─ test_pairwise.cpython-311.pyc
   │        │  │     │  ├─ test_rolling.cpython-311.pyc
   │        │  │     │  ├─ test_rolling_functions.cpython-311.pyc
   │        │  │     │  ├─ test_rolling_quantile.cpython-311.pyc
   │        │  │     │  ├─ test_rolling_skew_kurt.cpython-311.pyc
   │        │  │     │  ├─ test_timeseries_window.cpython-311.pyc
   │        │  │     │  └─ test_win_type.cpython-311.pyc
   │        │  │     ├─ conftest.py
   │        │  │     ├─ moments
   │        │  │     │  ├─ __init__.py
   │        │  │     │  ├─ __pycache__
   │        │  │     │  │  ├─ __init__.cpython-311.pyc
   │        │  │     │  │  ├─ conftest.cpython-311.pyc
   │        │  │     │  │  ├─ test_moments_consistency_ewm.cpython-311.pyc
   │        │  │     │  │  ├─ test_moments_consistency_expanding.cpython-311.pyc
   │        │  │     │  │  └─ test_moments_consistency_rolling.cpython-311.pyc
   │        │  │     │  ├─ conftest.py
   │        │  │     │  ├─ test_moments_consistency_ewm.py
   │        │  │     │  ├─ test_moments_consistency_expanding.py
   │        │  │     │  └─ test_moments_consistency_rolling.py
   │        │  │     ├─ test_api.py
   │        │  │     ├─ test_apply.py
   │        │  │     ├─ test_base_indexer.py
   │        │  │     ├─ test_cython_aggregations.py
   │        │  │     ├─ test_dtypes.py
   │        │  │     ├─ test_ewm.py
   │        │  │     ├─ test_expanding.py
   │        │  │     ├─ test_groupby.py
   │        │  │     ├─ test_numba.py
   │        │  │     ├─ test_online.py
   │        │  │     ├─ test_pairwise.py
   │        │  │     ├─ test_rolling.py
   │        │  │     ├─ test_rolling_functions.py
   │        │  │     ├─ test_rolling_quantile.py
   │        │  │     ├─ test_rolling_skew_kurt.py
   │        │  │     ├─ test_timeseries_window.py
   │        │  │     └─ test_win_type.py
   │        │  ├─ tseries
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ api.cpython-311.pyc
   │        │  │  │  ├─ frequencies.cpython-311.pyc
   │        │  │  │  ├─ holiday.cpython-311.pyc
   │        │  │  │  └─ offsets.cpython-311.pyc
   │        │  │  ├─ api.py
   │        │  │  ├─ frequencies.py
   │        │  │  ├─ holiday.py
   │        │  │  └─ offsets.py
   │        │  └─ util
   │        │     ├─ __init__.py
   │        │     ├─ __pycache__
   │        │     │  ├─ __init__.cpython-311.pyc
   │        │     │  ├─ _decorators.cpython-311.pyc
   │        │     │  ├─ _doctools.cpython-311.pyc
   │        │     │  ├─ _exceptions.cpython-311.pyc
   │        │     │  ├─ _print_versions.cpython-311.pyc
   │        │     │  ├─ _test_decorators.cpython-311.pyc
   │        │     │  ├─ _tester.cpython-311.pyc
   │        │     │  └─ _validators.cpython-311.pyc
   │        │     ├─ _decorators.py
   │        │     ├─ _doctools.py
   │        │     ├─ _exceptions.py
   │        │     ├─ _print_versions.py
   │        │     ├─ _test_decorators.py
   │        │     ├─ _tester.py
   │        │     ├─ _validators.py
   │        │     └─ version
   │        │        ├─ __init__.py
   │        │        └─ __pycache__
   │        │           └─ __init__.cpython-311.pyc
   │        ├─ pandas-2.2.3.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ LICENSE
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  └─ entry_points.txt
   │        ├─ pillow-11.2.1.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  ├─ licenses
   │        │  │  └─ LICENSE
   │        │  ├─ top_level.txt
   │        │  └─ zip-safe
   │        ├─ pip
   │        │  ├─ __init__.py
   │        │  ├─ __main__.py
   │        │  ├─ __pip-runner__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ __main__.cpython-311.pyc
   │        │  │  └─ __pip-runner__.cpython-311.pyc
   │        │  ├─ _internal
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ build_env.cpython-311.pyc
   │        │  │  │  ├─ cache.cpython-311.pyc
   │        │  │  │  ├─ configuration.cpython-311.pyc
   │        │  │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  │  ├─ main.cpython-311.pyc
   │        │  │  │  ├─ pyproject.cpython-311.pyc
   │        │  │  │  ├─ self_outdated_check.cpython-311.pyc
   │        │  │  │  └─ wheel_builder.cpython-311.pyc
   │        │  │  ├─ build_env.py
   │        │  │  ├─ cache.py
   │        │  │  ├─ cli
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ autocompletion.cpython-311.pyc
   │        │  │  │  │  ├─ base_command.cpython-311.pyc
   │        │  │  │  │  ├─ cmdoptions.cpython-311.pyc
   │        │  │  │  │  ├─ command_context.cpython-311.pyc
   │        │  │  │  │  ├─ index_command.cpython-311.pyc
   │        │  │  │  │  ├─ main.cpython-311.pyc
   │        │  │  │  │  ├─ main_parser.cpython-311.pyc
   │        │  │  │  │  ├─ parser.cpython-311.pyc
   │        │  │  │  │  ├─ progress_bars.cpython-311.pyc
   │        │  │  │  │  ├─ req_command.cpython-311.pyc
   │        │  │  │  │  ├─ spinners.cpython-311.pyc
   │        │  │  │  │  └─ status_codes.cpython-311.pyc
   │        │  │  │  ├─ autocompletion.py
   │        │  │  │  ├─ base_command.py
   │        │  │  │  ├─ cmdoptions.py
   │        │  │  │  ├─ command_context.py
   │        │  │  │  ├─ index_command.py
   │        │  │  │  ├─ main.py
   │        │  │  │  ├─ main_parser.py
   │        │  │  │  ├─ parser.py
   │        │  │  │  ├─ progress_bars.py
   │        │  │  │  ├─ req_command.py
   │        │  │  │  ├─ spinners.py
   │        │  │  │  └─ status_codes.py
   │        │  │  ├─ commands
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ cache.cpython-311.pyc
   │        │  │  │  │  ├─ check.cpython-311.pyc
   │        │  │  │  │  ├─ completion.cpython-311.pyc
   │        │  │  │  │  ├─ configuration.cpython-311.pyc
   │        │  │  │  │  ├─ debug.cpython-311.pyc
   │        │  │  │  │  ├─ download.cpython-311.pyc
   │        │  │  │  │  ├─ freeze.cpython-311.pyc
   │        │  │  │  │  ├─ hash.cpython-311.pyc
   │        │  │  │  │  ├─ help.cpython-311.pyc
   │        │  │  │  │  ├─ index.cpython-311.pyc
   │        │  │  │  │  ├─ inspect.cpython-311.pyc
   │        │  │  │  │  ├─ install.cpython-311.pyc
   │        │  │  │  │  ├─ list.cpython-311.pyc
   │        │  │  │  │  ├─ lock.cpython-311.pyc
   │        │  │  │  │  ├─ search.cpython-311.pyc
   │        │  │  │  │  ├─ show.cpython-311.pyc
   │        │  │  │  │  ├─ uninstall.cpython-311.pyc
   │        │  │  │  │  └─ wheel.cpython-311.pyc
   │        │  │  │  ├─ cache.py
   │        │  │  │  ├─ check.py
   │        │  │  │  ├─ completion.py
   │        │  │  │  ├─ configuration.py
   │        │  │  │  ├─ debug.py
   │        │  │  │  ├─ download.py
   │        │  │  │  ├─ freeze.py
   │        │  │  │  ├─ hash.py
   │        │  │  │  ├─ help.py
   │        │  │  │  ├─ index.py
   │        │  │  │  ├─ inspect.py
   │        │  │  │  ├─ install.py
   │        │  │  │  ├─ list.py
   │        │  │  │  ├─ lock.py
   │        │  │  │  ├─ search.py
   │        │  │  │  ├─ show.py
   │        │  │  │  ├─ uninstall.py
   │        │  │  │  └─ wheel.py
   │        │  │  ├─ configuration.py
   │        │  │  ├─ distributions
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  ├─ installed.cpython-311.pyc
   │        │  │  │  │  ├─ sdist.cpython-311.pyc
   │        │  │  │  │  └─ wheel.cpython-311.pyc
   │        │  │  │  ├─ base.py
   │        │  │  │  ├─ installed.py
   │        │  │  │  ├─ sdist.py
   │        │  │  │  └─ wheel.py
   │        │  │  ├─ exceptions.py
   │        │  │  ├─ index
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ collector.cpython-311.pyc
   │        │  │  │  │  ├─ package_finder.cpython-311.pyc
   │        │  │  │  │  └─ sources.cpython-311.pyc
   │        │  │  │  ├─ collector.py
   │        │  │  │  ├─ package_finder.py
   │        │  │  │  └─ sources.py
   │        │  │  ├─ locations
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ _distutils.cpython-311.pyc
   │        │  │  │  │  ├─ _sysconfig.cpython-311.pyc
   │        │  │  │  │  └─ base.cpython-311.pyc
   │        │  │  │  ├─ _distutils.py
   │        │  │  │  ├─ _sysconfig.py
   │        │  │  │  └─ base.py
   │        │  │  ├─ main.py
   │        │  │  ├─ metadata
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ _json.cpython-311.pyc
   │        │  │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  │  └─ pkg_resources.cpython-311.pyc
   │        │  │  │  ├─ _json.py
   │        │  │  │  ├─ base.py
   │        │  │  │  ├─ importlib
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ _compat.cpython-311.pyc
   │        │  │  │  │  │  ├─ _dists.cpython-311.pyc
   │        │  │  │  │  │  └─ _envs.cpython-311.pyc
   │        │  │  │  │  ├─ _compat.py
   │        │  │  │  │  ├─ _dists.py
   │        │  │  │  │  └─ _envs.py
   │        │  │  │  └─ pkg_resources.py
   │        │  │  ├─ models
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ candidate.cpython-311.pyc
   │        │  │  │  │  ├─ direct_url.cpython-311.pyc
   │        │  │  │  │  ├─ format_control.cpython-311.pyc
   │        │  │  │  │  ├─ index.cpython-311.pyc
   │        │  │  │  │  ├─ installation_report.cpython-311.pyc
   │        │  │  │  │  ├─ link.cpython-311.pyc
   │        │  │  │  │  ├─ pylock.cpython-311.pyc
   │        │  │  │  │  ├─ scheme.cpython-311.pyc
   │        │  │  │  │  ├─ search_scope.cpython-311.pyc
   │        │  │  │  │  ├─ selection_prefs.cpython-311.pyc
   │        │  │  │  │  ├─ target_python.cpython-311.pyc
   │        │  │  │  │  └─ wheel.cpython-311.pyc
   │        │  │  │  ├─ candidate.py
   │        │  │  │  ├─ direct_url.py
   │        │  │  │  ├─ format_control.py
   │        │  │  │  ├─ index.py
   │        │  │  │  ├─ installation_report.py
   │        │  │  │  ├─ link.py
   │        │  │  │  ├─ pylock.py
   │        │  │  │  ├─ scheme.py
   │        │  │  │  ├─ search_scope.py
   │        │  │  │  ├─ selection_prefs.py
   │        │  │  │  ├─ target_python.py
   │        │  │  │  └─ wheel.py
   │        │  │  ├─ network
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ auth.cpython-311.pyc
   │        │  │  │  │  ├─ cache.cpython-311.pyc
   │        │  │  │  │  ├─ download.cpython-311.pyc
   │        │  │  │  │  ├─ lazy_wheel.cpython-311.pyc
   │        │  │  │  │  ├─ session.cpython-311.pyc
   │        │  │  │  │  ├─ utils.cpython-311.pyc
   │        │  │  │  │  └─ xmlrpc.cpython-311.pyc
   │        │  │  │  ├─ auth.py
   │        │  │  │  ├─ cache.py
   │        │  │  │  ├─ download.py
   │        │  │  │  ├─ lazy_wheel.py
   │        │  │  │  ├─ session.py
   │        │  │  │  ├─ utils.py
   │        │  │  │  └─ xmlrpc.py
   │        │  │  ├─ operations
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ check.cpython-311.pyc
   │        │  │  │  │  ├─ freeze.cpython-311.pyc
   │        │  │  │  │  └─ prepare.cpython-311.pyc
   │        │  │  │  ├─ build
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ build_tracker.cpython-311.pyc
   │        │  │  │  │  │  ├─ metadata.cpython-311.pyc
   │        │  │  │  │  │  ├─ metadata_editable.cpython-311.pyc
   │        │  │  │  │  │  ├─ metadata_legacy.cpython-311.pyc
   │        │  │  │  │  │  ├─ wheel.cpython-311.pyc
   │        │  │  │  │  │  ├─ wheel_editable.cpython-311.pyc
   │        │  │  │  │  │  └─ wheel_legacy.cpython-311.pyc
   │        │  │  │  │  ├─ build_tracker.py
   │        │  │  │  │  ├─ metadata.py
   │        │  │  │  │  ├─ metadata_editable.py
   │        │  │  │  │  ├─ metadata_legacy.py
   │        │  │  │  │  ├─ wheel.py
   │        │  │  │  │  ├─ wheel_editable.py
   │        │  │  │  │  └─ wheel_legacy.py
   │        │  │  │  ├─ check.py
   │        │  │  │  ├─ freeze.py
   │        │  │  │  ├─ install
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ editable_legacy.cpython-311.pyc
   │        │  │  │  │  │  └─ wheel.cpython-311.pyc
   │        │  │  │  │  ├─ editable_legacy.py
   │        │  │  │  │  └─ wheel.py
   │        │  │  │  └─ prepare.py
   │        │  │  ├─ pyproject.py
   │        │  │  ├─ req
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ constructors.cpython-311.pyc
   │        │  │  │  │  ├─ req_dependency_group.cpython-311.pyc
   │        │  │  │  │  ├─ req_file.cpython-311.pyc
   │        │  │  │  │  ├─ req_install.cpython-311.pyc
   │        │  │  │  │  ├─ req_set.cpython-311.pyc
   │        │  │  │  │  └─ req_uninstall.cpython-311.pyc
   │        │  │  │  ├─ constructors.py
   │        │  │  │  ├─ req_dependency_group.py
   │        │  │  │  ├─ req_file.py
   │        │  │  │  ├─ req_install.py
   │        │  │  │  ├─ req_set.py
   │        │  │  │  └─ req_uninstall.py
   │        │  │  ├─ resolution
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  └─ base.cpython-311.pyc
   │        │  │  │  ├─ base.py
   │        │  │  │  ├─ legacy
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ resolver.cpython-311.pyc
   │        │  │  │  │  └─ resolver.py
   │        │  │  │  └─ resolvelib
   │        │  │  │     ├─ __init__.py
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │     │  ├─ base.cpython-311.pyc
   │        │  │  │     │  ├─ candidates.cpython-311.pyc
   │        │  │  │     │  ├─ factory.cpython-311.pyc
   │        │  │  │     │  ├─ found_candidates.cpython-311.pyc
   │        │  │  │     │  ├─ provider.cpython-311.pyc
   │        │  │  │     │  ├─ reporter.cpython-311.pyc
   │        │  │  │     │  ├─ requirements.cpython-311.pyc
   │        │  │  │     │  └─ resolver.cpython-311.pyc
   │        │  │  │     ├─ base.py
   │        │  │  │     ├─ candidates.py
   │        │  │  │     ├─ factory.py
   │        │  │  │     ├─ found_candidates.py
   │        │  │  │     ├─ provider.py
   │        │  │  │     ├─ reporter.py
   │        │  │  │     ├─ requirements.py
   │        │  │  │     └─ resolver.py
   │        │  │  ├─ self_outdated_check.py
   │        │  │  ├─ utils
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ _jaraco_text.cpython-311.pyc
   │        │  │  │  │  ├─ _log.cpython-311.pyc
   │        │  │  │  │  ├─ appdirs.cpython-311.pyc
   │        │  │  │  │  ├─ compat.cpython-311.pyc
   │        │  │  │  │  ├─ compatibility_tags.cpython-311.pyc
   │        │  │  │  │  ├─ datetime.cpython-311.pyc
   │        │  │  │  │  ├─ deprecation.cpython-311.pyc
   │        │  │  │  │  ├─ direct_url_helpers.cpython-311.pyc
   │        │  │  │  │  ├─ egg_link.cpython-311.pyc
   │        │  │  │  │  ├─ entrypoints.cpython-311.pyc
   │        │  │  │  │  ├─ filesystem.cpython-311.pyc
   │        │  │  │  │  ├─ filetypes.cpython-311.pyc
   │        │  │  │  │  ├─ glibc.cpython-311.pyc
   │        │  │  │  │  ├─ hashes.cpython-311.pyc
   │        │  │  │  │  ├─ logging.cpython-311.pyc
   │        │  │  │  │  ├─ misc.cpython-311.pyc
   │        │  │  │  │  ├─ packaging.cpython-311.pyc
   │        │  │  │  │  ├─ retry.cpython-311.pyc
   │        │  │  │  │  ├─ setuptools_build.cpython-311.pyc
   │        │  │  │  │  ├─ subprocess.cpython-311.pyc
   │        │  │  │  │  ├─ temp_dir.cpython-311.pyc
   │        │  │  │  │  ├─ unpacking.cpython-311.pyc
   │        │  │  │  │  ├─ urls.cpython-311.pyc
   │        │  │  │  │  ├─ virtualenv.cpython-311.pyc
   │        │  │  │  │  └─ wheel.cpython-311.pyc
   │        │  │  │  ├─ _jaraco_text.py
   │        │  │  │  ├─ _log.py
   │        │  │  │  ├─ appdirs.py
   │        │  │  │  ├─ compat.py
   │        │  │  │  ├─ compatibility_tags.py
   │        │  │  │  ├─ datetime.py
   │        │  │  │  ├─ deprecation.py
   │        │  │  │  ├─ direct_url_helpers.py
   │        │  │  │  ├─ egg_link.py
   │        │  │  │  ├─ entrypoints.py
   │        │  │  │  ├─ filesystem.py
   │        │  │  │  ├─ filetypes.py
   │        │  │  │  ├─ glibc.py
   │        │  │  │  ├─ hashes.py
   │        │  │  │  ├─ logging.py
   │        │  │  │  ├─ misc.py
   │        │  │  │  ├─ packaging.py
   │        │  │  │  ├─ retry.py
   │        │  │  │  ├─ setuptools_build.py
   │        │  │  │  ├─ subprocess.py
   │        │  │  │  ├─ temp_dir.py
   │        │  │  │  ├─ unpacking.py
   │        │  │  │  ├─ urls.py
   │        │  │  │  ├─ virtualenv.py
   │        │  │  │  └─ wheel.py
   │        │  │  ├─ vcs
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ bazaar.cpython-311.pyc
   │        │  │  │  │  ├─ git.cpython-311.pyc
   │        │  │  │  │  ├─ mercurial.cpython-311.pyc
   │        │  │  │  │  ├─ subversion.cpython-311.pyc
   │        │  │  │  │  └─ versioncontrol.cpython-311.pyc
   │        │  │  │  ├─ bazaar.py
   │        │  │  │  ├─ git.py
   │        │  │  │  ├─ mercurial.py
   │        │  │  │  ├─ subversion.py
   │        │  │  │  └─ versioncontrol.py
   │        │  │  └─ wheel_builder.py
   │        │  ├─ _vendor
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  └─ typing_extensions.cpython-311.pyc
   │        │  │  ├─ cachecontrol
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ _cmd.cpython-311.pyc
   │        │  │  │  │  ├─ adapter.cpython-311.pyc
   │        │  │  │  │  ├─ cache.cpython-311.pyc
   │        │  │  │  │  ├─ controller.cpython-311.pyc
   │        │  │  │  │  ├─ filewrapper.cpython-311.pyc
   │        │  │  │  │  ├─ heuristics.cpython-311.pyc
   │        │  │  │  │  ├─ serialize.cpython-311.pyc
   │        │  │  │  │  └─ wrapper.cpython-311.pyc
   │        │  │  │  ├─ _cmd.py
   │        │  │  │  ├─ adapter.py
   │        │  │  │  ├─ cache.py
   │        │  │  │  ├─ caches
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ file_cache.cpython-311.pyc
   │        │  │  │  │  │  └─ redis_cache.cpython-311.pyc
   │        │  │  │  │  ├─ file_cache.py
   │        │  │  │  │  └─ redis_cache.py
   │        │  │  │  ├─ controller.py
   │        │  │  │  ├─ filewrapper.py
   │        │  │  │  ├─ heuristics.py
   │        │  │  │  ├─ serialize.py
   │        │  │  │  └─ wrapper.py
   │        │  │  ├─ certifi
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __main__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ __main__.cpython-311.pyc
   │        │  │  │  │  └─ core.cpython-311.pyc
   │        │  │  │  ├─ cacert.pem
   │        │  │  │  └─ core.py
   │        │  │  ├─ dependency_groups
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __main__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ __main__.cpython-311.pyc
   │        │  │  │  │  ├─ _implementation.cpython-311.pyc
   │        │  │  │  │  ├─ _lint_dependency_groups.cpython-311.pyc
   │        │  │  │  │  ├─ _pip_wrapper.cpython-311.pyc
   │        │  │  │  │  └─ _toml_compat.cpython-311.pyc
   │        │  │  │  ├─ _implementation.py
   │        │  │  │  ├─ _lint_dependency_groups.py
   │        │  │  │  ├─ _pip_wrapper.py
   │        │  │  │  └─ _toml_compat.py
   │        │  │  ├─ distlib
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ compat.cpython-311.pyc
   │        │  │  │  │  ├─ database.cpython-311.pyc
   │        │  │  │  │  ├─ index.cpython-311.pyc
   │        │  │  │  │  ├─ locators.cpython-311.pyc
   │        │  │  │  │  ├─ manifest.cpython-311.pyc
   │        │  │  │  │  ├─ markers.cpython-311.pyc
   │        │  │  │  │  ├─ metadata.cpython-311.pyc
   │        │  │  │  │  ├─ resources.cpython-311.pyc
   │        │  │  │  │  ├─ scripts.cpython-311.pyc
   │        │  │  │  │  ├─ util.cpython-311.pyc
   │        │  │  │  │  ├─ version.cpython-311.pyc
   │        │  │  │  │  └─ wheel.cpython-311.pyc
   │        │  │  │  ├─ compat.py
   │        │  │  │  ├─ database.py
   │        │  │  │  ├─ index.py
   │        │  │  │  ├─ locators.py
   │        │  │  │  ├─ manifest.py
   │        │  │  │  ├─ markers.py
   │        │  │  │  ├─ metadata.py
   │        │  │  │  ├─ resources.py
   │        │  │  │  ├─ scripts.py
   │        │  │  │  ├─ t32.exe
   │        │  │  │  ├─ t64-arm.exe
   │        │  │  │  ├─ t64.exe
   │        │  │  │  ├─ util.py
   │        │  │  │  ├─ version.py
   │        │  │  │  ├─ w32.exe
   │        │  │  │  ├─ w64-arm.exe
   │        │  │  │  ├─ w64.exe
   │        │  │  │  └─ wheel.py
   │        │  │  ├─ distro
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __main__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ __main__.cpython-311.pyc
   │        │  │  │  │  └─ distro.cpython-311.pyc
   │        │  │  │  └─ distro.py
   │        │  │  ├─ idna
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ codec.cpython-311.pyc
   │        │  │  │  │  ├─ compat.cpython-311.pyc
   │        │  │  │  │  ├─ core.cpython-311.pyc
   │        │  │  │  │  ├─ idnadata.cpython-311.pyc
   │        │  │  │  │  ├─ intranges.cpython-311.pyc
   │        │  │  │  │  ├─ package_data.cpython-311.pyc
   │        │  │  │  │  └─ uts46data.cpython-311.pyc
   │        │  │  │  ├─ codec.py
   │        │  │  │  ├─ compat.py
   │        │  │  │  ├─ core.py
   │        │  │  │  ├─ idnadata.py
   │        │  │  │  ├─ intranges.py
   │        │  │  │  ├─ package_data.py
   │        │  │  │  └─ uts46data.py
   │        │  │  ├─ msgpack
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  │  │  ├─ ext.cpython-311.pyc
   │        │  │  │  │  └─ fallback.cpython-311.pyc
   │        │  │  │  ├─ exceptions.py
   │        │  │  │  ├─ ext.py
   │        │  │  │  └─ fallback.py
   │        │  │  ├─ packaging
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ _elffile.cpython-311.pyc
   │        │  │  │  │  ├─ _manylinux.cpython-311.pyc
   │        │  │  │  │  ├─ _musllinux.cpython-311.pyc
   │        │  │  │  │  ├─ _parser.cpython-311.pyc
   │        │  │  │  │  ├─ _structures.cpython-311.pyc
   │        │  │  │  │  ├─ _tokenizer.cpython-311.pyc
   │        │  │  │  │  ├─ markers.cpython-311.pyc
   │        │  │  │  │  ├─ metadata.cpython-311.pyc
   │        │  │  │  │  ├─ requirements.cpython-311.pyc
   │        │  │  │  │  ├─ specifiers.cpython-311.pyc
   │        │  │  │  │  ├─ tags.cpython-311.pyc
   │        │  │  │  │  ├─ utils.cpython-311.pyc
   │        │  │  │  │  └─ version.cpython-311.pyc
   │        │  │  │  ├─ _elffile.py
   │        │  │  │  ├─ _manylinux.py
   │        │  │  │  ├─ _musllinux.py
   │        │  │  │  ├─ _parser.py
   │        │  │  │  ├─ _structures.py
   │        │  │  │  ├─ _tokenizer.py
   │        │  │  │  ├─ licenses
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ _spdx.cpython-311.pyc
   │        │  │  │  │  └─ _spdx.py
   │        │  │  │  ├─ markers.py
   │        │  │  │  ├─ metadata.py
   │        │  │  │  ├─ requirements.py
   │        │  │  │  ├─ specifiers.py
   │        │  │  │  ├─ tags.py
   │        │  │  │  ├─ utils.py
   │        │  │  │  └─ version.py
   │        │  │  ├─ pkg_resources
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ platformdirs
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __main__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ __main__.cpython-311.pyc
   │        │  │  │  │  ├─ android.cpython-311.pyc
   │        │  │  │  │  ├─ api.cpython-311.pyc
   │        │  │  │  │  ├─ macos.cpython-311.pyc
   │        │  │  │  │  ├─ unix.cpython-311.pyc
   │        │  │  │  │  ├─ version.cpython-311.pyc
   │        │  │  │  │  └─ windows.cpython-311.pyc
   │        │  │  │  ├─ android.py
   │        │  │  │  ├─ api.py
   │        │  │  │  ├─ macos.py
   │        │  │  │  ├─ unix.py
   │        │  │  │  ├─ version.py
   │        │  │  │  └─ windows.py
   │        │  │  ├─ pygments
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __main__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ __main__.cpython-311.pyc
   │        │  │  │  │  ├─ console.cpython-311.pyc
   │        │  │  │  │  ├─ filter.cpython-311.pyc
   │        │  │  │  │  ├─ formatter.cpython-311.pyc
   │        │  │  │  │  ├─ lexer.cpython-311.pyc
   │        │  │  │  │  ├─ modeline.cpython-311.pyc
   │        │  │  │  │  ├─ plugin.cpython-311.pyc
   │        │  │  │  │  ├─ regexopt.cpython-311.pyc
   │        │  │  │  │  ├─ scanner.cpython-311.pyc
   │        │  │  │  │  ├─ sphinxext.cpython-311.pyc
   │        │  │  │  │  ├─ style.cpython-311.pyc
   │        │  │  │  │  ├─ token.cpython-311.pyc
   │        │  │  │  │  ├─ unistring.cpython-311.pyc
   │        │  │  │  │  └─ util.cpython-311.pyc
   │        │  │  │  ├─ console.py
   │        │  │  │  ├─ filter.py
   │        │  │  │  ├─ filters
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  └─ __pycache__
   │        │  │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  │  ├─ formatter.py
   │        │  │  │  ├─ formatters
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ _mapping.cpython-311.pyc
   │        │  │  │  │  └─ _mapping.py
   │        │  │  │  ├─ lexer.py
   │        │  │  │  ├─ lexers
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ _mapping.cpython-311.pyc
   │        │  │  │  │  │  └─ python.cpython-311.pyc
   │        │  │  │  │  ├─ _mapping.py
   │        │  │  │  │  └─ python.py
   │        │  │  │  ├─ modeline.py
   │        │  │  │  ├─ plugin.py
   │        │  │  │  ├─ regexopt.py
   │        │  │  │  ├─ scanner.py
   │        │  │  │  ├─ sphinxext.py
   │        │  │  │  ├─ style.py
   │        │  │  │  ├─ styles
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ _mapping.cpython-311.pyc
   │        │  │  │  │  └─ _mapping.py
   │        │  │  │  ├─ token.py
   │        │  │  │  ├─ unistring.py
   │        │  │  │  └─ util.py
   │        │  │  ├─ pyproject_hooks
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  └─ _impl.cpython-311.pyc
   │        │  │  │  ├─ _impl.py
   │        │  │  │  └─ _in_process
   │        │  │  │     ├─ __init__.py
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │     │  └─ _in_process.cpython-311.pyc
   │        │  │  │     └─ _in_process.py
   │        │  │  ├─ requests
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ __version__.cpython-311.pyc
   │        │  │  │  │  ├─ _internal_utils.cpython-311.pyc
   │        │  │  │  │  ├─ adapters.cpython-311.pyc
   │        │  │  │  │  ├─ api.cpython-311.pyc
   │        │  │  │  │  ├─ auth.cpython-311.pyc
   │        │  │  │  │  ├─ certs.cpython-311.pyc
   │        │  │  │  │  ├─ compat.cpython-311.pyc
   │        │  │  │  │  ├─ cookies.cpython-311.pyc
   │        │  │  │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  │  │  ├─ help.cpython-311.pyc
   │        │  │  │  │  ├─ hooks.cpython-311.pyc
   │        │  │  │  │  ├─ models.cpython-311.pyc
   │        │  │  │  │  ├─ packages.cpython-311.pyc
   │        │  │  │  │  ├─ sessions.cpython-311.pyc
   │        │  │  │  │  ├─ status_codes.cpython-311.pyc
   │        │  │  │  │  ├─ structures.cpython-311.pyc
   │        │  │  │  │  └─ utils.cpython-311.pyc
   │        │  │  │  ├─ __version__.py
   │        │  │  │  ├─ _internal_utils.py
   │        │  │  │  ├─ adapters.py
   │        │  │  │  ├─ api.py
   │        │  │  │  ├─ auth.py
   │        │  │  │  ├─ certs.py
   │        │  │  │  ├─ compat.py
   │        │  │  │  ├─ cookies.py
   │        │  │  │  ├─ exceptions.py
   │        │  │  │  ├─ help.py
   │        │  │  │  ├─ hooks.py
   │        │  │  │  ├─ models.py
   │        │  │  │  ├─ packages.py
   │        │  │  │  ├─ sessions.py
   │        │  │  │  ├─ status_codes.py
   │        │  │  │  ├─ structures.py
   │        │  │  │  └─ utils.py
   │        │  │  ├─ resolvelib
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ providers.cpython-311.pyc
   │        │  │  │  │  ├─ reporters.cpython-311.pyc
   │        │  │  │  │  └─ structs.cpython-311.pyc
   │        │  │  │  ├─ providers.py
   │        │  │  │  ├─ reporters.py
   │        │  │  │  ├─ resolvers
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ abstract.cpython-311.pyc
   │        │  │  │  │  │  ├─ criterion.cpython-311.pyc
   │        │  │  │  │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  │  │  │  └─ resolution.cpython-311.pyc
   │        │  │  │  │  ├─ abstract.py
   │        │  │  │  │  ├─ criterion.py
   │        │  │  │  │  ├─ exceptions.py
   │        │  │  │  │  └─ resolution.py
   │        │  │  │  └─ structs.py
   │        │  │  ├─ rich
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __main__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ __main__.cpython-311.pyc
   │        │  │  │  │  ├─ _cell_widths.cpython-311.pyc
   │        │  │  │  │  ├─ _emoji_codes.cpython-311.pyc
   │        │  │  │  │  ├─ _emoji_replace.cpython-311.pyc
   │        │  │  │  │  ├─ _export_format.cpython-311.pyc
   │        │  │  │  │  ├─ _extension.cpython-311.pyc
   │        │  │  │  │  ├─ _fileno.cpython-311.pyc
   │        │  │  │  │  ├─ _inspect.cpython-311.pyc
   │        │  │  │  │  ├─ _log_render.cpython-311.pyc
   │        │  │  │  │  ├─ _loop.cpython-311.pyc
   │        │  │  │  │  ├─ _null_file.cpython-311.pyc
   │        │  │  │  │  ├─ _palettes.cpython-311.pyc
   │        │  │  │  │  ├─ _pick.cpython-311.pyc
   │        │  │  │  │  ├─ _ratio.cpython-311.pyc
   │        │  │  │  │  ├─ _spinners.cpython-311.pyc
   │        │  │  │  │  ├─ _stack.cpython-311.pyc
   │        │  │  │  │  ├─ _timer.cpython-311.pyc
   │        │  │  │  │  ├─ _win32_console.cpython-311.pyc
   │        │  │  │  │  ├─ _windows.cpython-311.pyc
   │        │  │  │  │  ├─ _windows_renderer.cpython-311.pyc
   │        │  │  │  │  ├─ _wrap.cpython-311.pyc
   │        │  │  │  │  ├─ abc.cpython-311.pyc
   │        │  │  │  │  ├─ align.cpython-311.pyc
   │        │  │  │  │  ├─ ansi.cpython-311.pyc
   │        │  │  │  │  ├─ bar.cpython-311.pyc
   │        │  │  │  │  ├─ box.cpython-311.pyc
   │        │  │  │  │  ├─ cells.cpython-311.pyc
   │        │  │  │  │  ├─ color.cpython-311.pyc
   │        │  │  │  │  ├─ color_triplet.cpython-311.pyc
   │        │  │  │  │  ├─ columns.cpython-311.pyc
   │        │  │  │  │  ├─ console.cpython-311.pyc
   │        │  │  │  │  ├─ constrain.cpython-311.pyc
   │        │  │  │  │  ├─ containers.cpython-311.pyc
   │        │  │  │  │  ├─ control.cpython-311.pyc
   │        │  │  │  │  ├─ default_styles.cpython-311.pyc
   │        │  │  │  │  ├─ diagnose.cpython-311.pyc
   │        │  │  │  │  ├─ emoji.cpython-311.pyc
   │        │  │  │  │  ├─ errors.cpython-311.pyc
   │        │  │  │  │  ├─ file_proxy.cpython-311.pyc
   │        │  │  │  │  ├─ filesize.cpython-311.pyc
   │        │  │  │  │  ├─ highlighter.cpython-311.pyc
   │        │  │  │  │  ├─ json.cpython-311.pyc
   │        │  │  │  │  ├─ jupyter.cpython-311.pyc
   │        │  │  │  │  ├─ layout.cpython-311.pyc
   │        │  │  │  │  ├─ live.cpython-311.pyc
   │        │  │  │  │  ├─ live_render.cpython-311.pyc
   │        │  │  │  │  ├─ logging.cpython-311.pyc
   │        │  │  │  │  ├─ markup.cpython-311.pyc
   │        │  │  │  │  ├─ measure.cpython-311.pyc
   │        │  │  │  │  ├─ padding.cpython-311.pyc
   │        │  │  │  │  ├─ pager.cpython-311.pyc
   │        │  │  │  │  ├─ palette.cpython-311.pyc
   │        │  │  │  │  ├─ panel.cpython-311.pyc
   │        │  │  │  │  ├─ pretty.cpython-311.pyc
   │        │  │  │  │  ├─ progress.cpython-311.pyc
   │        │  │  │  │  ├─ progress_bar.cpython-311.pyc
   │        │  │  │  │  ├─ prompt.cpython-311.pyc
   │        │  │  │  │  ├─ protocol.cpython-311.pyc
   │        │  │  │  │  ├─ region.cpython-311.pyc
   │        │  │  │  │  ├─ repr.cpython-311.pyc
   │        │  │  │  │  ├─ rule.cpython-311.pyc
   │        │  │  │  │  ├─ scope.cpython-311.pyc
   │        │  │  │  │  ├─ screen.cpython-311.pyc
   │        │  │  │  │  ├─ segment.cpython-311.pyc
   │        │  │  │  │  ├─ spinner.cpython-311.pyc
   │        │  │  │  │  ├─ status.cpython-311.pyc
   │        │  │  │  │  ├─ style.cpython-311.pyc
   │        │  │  │  │  ├─ styled.cpython-311.pyc
   │        │  │  │  │  ├─ syntax.cpython-311.pyc
   │        │  │  │  │  ├─ table.cpython-311.pyc
   │        │  │  │  │  ├─ terminal_theme.cpython-311.pyc
   │        │  │  │  │  ├─ text.cpython-311.pyc
   │        │  │  │  │  ├─ theme.cpython-311.pyc
   │        │  │  │  │  ├─ themes.cpython-311.pyc
   │        │  │  │  │  ├─ traceback.cpython-311.pyc
   │        │  │  │  │  └─ tree.cpython-311.pyc
   │        │  │  │  ├─ _cell_widths.py
   │        │  │  │  ├─ _emoji_codes.py
   │        │  │  │  ├─ _emoji_replace.py
   │        │  │  │  ├─ _export_format.py
   │        │  │  │  ├─ _extension.py
   │        │  │  │  ├─ _fileno.py
   │        │  │  │  ├─ _inspect.py
   │        │  │  │  ├─ _log_render.py
   │        │  │  │  ├─ _loop.py
   │        │  │  │  ├─ _null_file.py
   │        │  │  │  ├─ _palettes.py
   │        │  │  │  ├─ _pick.py
   │        │  │  │  ├─ _ratio.py
   │        │  │  │  ├─ _spinners.py
   │        │  │  │  ├─ _stack.py
   │        │  │  │  ├─ _timer.py
   │        │  │  │  ├─ _win32_console.py
   │        │  │  │  ├─ _windows.py
   │        │  │  │  ├─ _windows_renderer.py
   │        │  │  │  ├─ _wrap.py
   │        │  │  │  ├─ abc.py
   │        │  │  │  ├─ align.py
   │        │  │  │  ├─ ansi.py
   │        │  │  │  ├─ bar.py
   │        │  │  │  ├─ box.py
   │        │  │  │  ├─ cells.py
   │        │  │  │  ├─ color.py
   │        │  │  │  ├─ color_triplet.py
   │        │  │  │  ├─ columns.py
   │        │  │  │  ├─ console.py
   │        │  │  │  ├─ constrain.py
   │        │  │  │  ├─ containers.py
   │        │  │  │  ├─ control.py
   │        │  │  │  ├─ default_styles.py
   │        │  │  │  ├─ diagnose.py
   │        │  │  │  ├─ emoji.py
   │        │  │  │  ├─ errors.py
   │        │  │  │  ├─ file_proxy.py
   │        │  │  │  ├─ filesize.py
   │        │  │  │  ├─ highlighter.py
   │        │  │  │  ├─ json.py
   │        │  │  │  ├─ jupyter.py
   │        │  │  │  ├─ layout.py
   │        │  │  │  ├─ live.py
   │        │  │  │  ├─ live_render.py
   │        │  │  │  ├─ logging.py
   │        │  │  │  ├─ markup.py
   │        │  │  │  ├─ measure.py
   │        │  │  │  ├─ padding.py
   │        │  │  │  ├─ pager.py
   │        │  │  │  ├─ palette.py
   │        │  │  │  ├─ panel.py
   │        │  │  │  ├─ pretty.py
   │        │  │  │  ├─ progress.py
   │        │  │  │  ├─ progress_bar.py
   │        │  │  │  ├─ prompt.py
   │        │  │  │  ├─ protocol.py
   │        │  │  │  ├─ region.py
   │        │  │  │  ├─ repr.py
   │        │  │  │  ├─ rule.py
   │        │  │  │  ├─ scope.py
   │        │  │  │  ├─ screen.py
   │        │  │  │  ├─ segment.py
   │        │  │  │  ├─ spinner.py
   │        │  │  │  ├─ status.py
   │        │  │  │  ├─ style.py
   │        │  │  │  ├─ styled.py
   │        │  │  │  ├─ syntax.py
   │        │  │  │  ├─ table.py
   │        │  │  │  ├─ terminal_theme.py
   │        │  │  │  ├─ text.py
   │        │  │  │  ├─ theme.py
   │        │  │  │  ├─ themes.py
   │        │  │  │  ├─ traceback.py
   │        │  │  │  └─ tree.py
   │        │  │  ├─ tomli
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ _parser.cpython-311.pyc
   │        │  │  │  │  ├─ _re.cpython-311.pyc
   │        │  │  │  │  └─ _types.cpython-311.pyc
   │        │  │  │  ├─ _parser.py
   │        │  │  │  ├─ _re.py
   │        │  │  │  └─ _types.py
   │        │  │  ├─ tomli_w
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  └─ _writer.cpython-311.pyc
   │        │  │  │  └─ _writer.py
   │        │  │  ├─ truststore
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ _api.cpython-311.pyc
   │        │  │  │  │  ├─ _macos.cpython-311.pyc
   │        │  │  │  │  ├─ _openssl.cpython-311.pyc
   │        │  │  │  │  ├─ _ssl_constants.cpython-311.pyc
   │        │  │  │  │  └─ _windows.cpython-311.pyc
   │        │  │  │  ├─ _api.py
   │        │  │  │  ├─ _macos.py
   │        │  │  │  ├─ _openssl.py
   │        │  │  │  ├─ _ssl_constants.py
   │        │  │  │  └─ _windows.py
   │        │  │  ├─ typing_extensions.py
   │        │  │  ├─ urllib3
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ _collections.cpython-311.pyc
   │        │  │  │  │  ├─ _version.cpython-311.pyc
   │        │  │  │  │  ├─ connection.cpython-311.pyc
   │        │  │  │  │  ├─ connectionpool.cpython-311.pyc
   │        │  │  │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  │  │  ├─ fields.cpython-311.pyc
   │        │  │  │  │  ├─ filepost.cpython-311.pyc
   │        │  │  │  │  ├─ poolmanager.cpython-311.pyc
   │        │  │  │  │  ├─ request.cpython-311.pyc
   │        │  │  │  │  └─ response.cpython-311.pyc
   │        │  │  │  ├─ _collections.py
   │        │  │  │  ├─ _version.py
   │        │  │  │  ├─ connection.py
   │        │  │  │  ├─ connectionpool.py
   │        │  │  │  ├─ contrib
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ _appengine_environ.cpython-311.pyc
   │        │  │  │  │  │  ├─ appengine.cpython-311.pyc
   │        │  │  │  │  │  ├─ ntlmpool.cpython-311.pyc
   │        │  │  │  │  │  ├─ pyopenssl.cpython-311.pyc
   │        │  │  │  │  │  ├─ securetransport.cpython-311.pyc
   │        │  │  │  │  │  └─ socks.cpython-311.pyc
   │        │  │  │  │  ├─ _appengine_environ.py
   │        │  │  │  │  ├─ _securetransport
   │        │  │  │  │  │  ├─ __init__.py
   │        │  │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ bindings.cpython-311.pyc
   │        │  │  │  │  │  │  └─ low_level.cpython-311.pyc
   │        │  │  │  │  │  ├─ bindings.py
   │        │  │  │  │  │  └─ low_level.py
   │        │  │  │  │  ├─ appengine.py
   │        │  │  │  │  ├─ ntlmpool.py
   │        │  │  │  │  ├─ pyopenssl.py
   │        │  │  │  │  ├─ securetransport.py
   │        │  │  │  │  └─ socks.py
   │        │  │  │  ├─ exceptions.py
   │        │  │  │  ├─ fields.py
   │        │  │  │  ├─ filepost.py
   │        │  │  │  ├─ packages
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ six.cpython-311.pyc
   │        │  │  │  │  ├─ backports
   │        │  │  │  │  │  ├─ __init__.py
   │        │  │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ makefile.cpython-311.pyc
   │        │  │  │  │  │  │  └─ weakref_finalize.cpython-311.pyc
   │        │  │  │  │  │  ├─ makefile.py
   │        │  │  │  │  │  └─ weakref_finalize.py
   │        │  │  │  │  └─ six.py
   │        │  │  │  ├─ poolmanager.py
   │        │  │  │  ├─ request.py
   │        │  │  │  ├─ response.py
   │        │  │  │  └─ util
   │        │  │  │     ├─ __init__.py
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │     │  ├─ connection.cpython-311.pyc
   │        │  │  │     │  ├─ proxy.cpython-311.pyc
   │        │  │  │     │  ├─ queue.cpython-311.pyc
   │        │  │  │     │  ├─ request.cpython-311.pyc
   │        │  │  │     │  ├─ response.cpython-311.pyc
   │        │  │  │     │  ├─ retry.cpython-311.pyc
   │        │  │  │     │  ├─ ssl_.cpython-311.pyc
   │        │  │  │     │  ├─ ssl_match_hostname.cpython-311.pyc
   │        │  │  │     │  ├─ ssltransport.cpython-311.pyc
   │        │  │  │     │  ├─ timeout.cpython-311.pyc
   │        │  │  │     │  ├─ url.cpython-311.pyc
   │        │  │  │     │  └─ wait.cpython-311.pyc
   │        │  │  │     ├─ connection.py
   │        │  │  │     ├─ proxy.py
   │        │  │  │     ├─ queue.py
   │        │  │  │     ├─ request.py
   │        │  │  │     ├─ response.py
   │        │  │  │     ├─ retry.py
   │        │  │  │     ├─ ssl_.py
   │        │  │  │     ├─ ssl_match_hostname.py
   │        │  │  │     ├─ ssltransport.py
   │        │  │  │     ├─ timeout.py
   │        │  │  │     ├─ url.py
   │        │  │  │     └─ wait.py
   │        │  │  └─ vendor.txt
   │        │  └─ py.typed
   │        ├─ pip-25.1.1.dist-info
   │        │  ├─ AUTHORS.txt
   │        │  ├─ INSTALLER
   │        │  ├─ LICENSE.txt
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  ├─ entry_points.txt
   │        │  └─ top_level.txt
   │        ├─ pkg_resources
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  └─ __init__.cpython-311.pyc
   │        │  ├─ api_tests.txt
   │        │  ├─ py.typed
   │        │  └─ tests
   │        │     ├─ __init__.py
   │        │     ├─ __pycache__
   │        │     │  ├─ __init__.cpython-311.pyc
   │        │     │  ├─ test_find_distributions.cpython-311.pyc
   │        │     │  ├─ test_integration_zope_interface.cpython-311.pyc
   │        │     │  ├─ test_markers.cpython-311.pyc
   │        │     │  ├─ test_pkg_resources.cpython-311.pyc
   │        │     │  ├─ test_resources.cpython-311.pyc
   │        │     │  └─ test_working_set.cpython-311.pyc
   │        │     ├─ data
   │        │     │  ├─ my-test-package-source
   │        │     │  │  ├─ __pycache__
   │        │     │  │  │  └─ setup.cpython-311.pyc
   │        │     │  │  ├─ setup.cfg
   │        │     │  │  └─ setup.py
   │        │     │  ├─ my-test-package-zip
   │        │     │  │  └─ my-test-package.zip
   │        │     │  ├─ my-test-package_unpacked-egg
   │        │     │  │  └─ my_test_package-1.0-py3.7.egg
   │        │     │  │     └─ EGG-INFO
   │        │     │  │        ├─ PKG-INFO
   │        │     │  │        ├─ SOURCES.txt
   │        │     │  │        ├─ dependency_links.txt
   │        │     │  │        ├─ top_level.txt
   │        │     │  │        └─ zip-safe
   │        │     │  └─ my-test-package_zipped-egg
   │        │     │     └─ my_test_package-1.0-py3.7.egg
   │        │     ├─ test_find_distributions.py
   │        │     ├─ test_integration_zope_interface.py
   │        │     ├─ test_markers.py
   │        │     ├─ test_pkg_resources.py
   │        │     ├─ test_resources.py
   │        │     └─ test_working_set.py
   │        ├─ protobuf-6.31.1.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ LICENSE
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  └─ WHEEL
   │        ├─ pyarrow
   │        │  ├─ __init__.pxd
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ _compute_docstrings.cpython-311.pyc
   │        │  │  ├─ _generated_version.cpython-311.pyc
   │        │  │  ├─ acero.cpython-311.pyc
   │        │  │  ├─ benchmark.cpython-311.pyc
   │        │  │  ├─ cffi.cpython-311.pyc
   │        │  │  ├─ compute.cpython-311.pyc
   │        │  │  ├─ conftest.cpython-311.pyc
   │        │  │  ├─ csv.cpython-311.pyc
   │        │  │  ├─ cuda.cpython-311.pyc
   │        │  │  ├─ dataset.cpython-311.pyc
   │        │  │  ├─ feather.cpython-311.pyc
   │        │  │  ├─ flight.cpython-311.pyc
   │        │  │  ├─ fs.cpython-311.pyc
   │        │  │  ├─ ipc.cpython-311.pyc
   │        │  │  ├─ json.cpython-311.pyc
   │        │  │  ├─ jvm.cpython-311.pyc
   │        │  │  ├─ orc.cpython-311.pyc
   │        │  │  ├─ pandas_compat.cpython-311.pyc
   │        │  │  ├─ substrait.cpython-311.pyc
   │        │  │  ├─ types.cpython-311.pyc
   │        │  │  └─ util.cpython-311.pyc
   │        │  ├─ _acero.cpython-311-darwin.so
   │        │  ├─ _acero.pxd
   │        │  ├─ _acero.pyx
   │        │  ├─ _azurefs.cpython-311-darwin.so
   │        │  ├─ _azurefs.pyx
   │        │  ├─ _compute.cpython-311-darwin.so
   │        │  ├─ _compute.pxd
   │        │  ├─ _compute.pyx
   │        │  ├─ _compute_docstrings.py
   │        │  ├─ _csv.cpython-311-darwin.so
   │        │  ├─ _csv.pxd
   │        │  ├─ _csv.pyx
   │        │  ├─ _cuda.pxd
   │        │  ├─ _cuda.pyx
   │        │  ├─ _dataset.cpython-311-darwin.so
   │        │  ├─ _dataset.pxd
   │        │  ├─ _dataset.pyx
   │        │  ├─ _dataset_orc.cpython-311-darwin.so
   │        │  ├─ _dataset_orc.pyx
   │        │  ├─ _dataset_parquet.cpython-311-darwin.so
   │        │  ├─ _dataset_parquet.pxd
   │        │  ├─ _dataset_parquet.pyx
   │        │  ├─ _dataset_parquet_encryption.cpython-311-darwin.so
   │        │  ├─ _dataset_parquet_encryption.pyx
   │        │  ├─ _dlpack.pxi
   │        │  ├─ _feather.cpython-311-darwin.so
   │        │  ├─ _feather.pyx
   │        │  ├─ _flight.cpython-311-darwin.so
   │        │  ├─ _flight.pyx
   │        │  ├─ _fs.cpython-311-darwin.so
   │        │  ├─ _fs.pxd
   │        │  ├─ _fs.pyx
   │        │  ├─ _gcsfs.cpython-311-darwin.so
   │        │  ├─ _gcsfs.pyx
   │        │  ├─ _generated_version.py
   │        │  ├─ _hdfs.cpython-311-darwin.so
   │        │  ├─ _hdfs.pyx
   │        │  ├─ _json.cpython-311-darwin.so
   │        │  ├─ _json.pxd
   │        │  ├─ _json.pyx
   │        │  ├─ _orc.cpython-311-darwin.so
   │        │  ├─ _orc.pxd
   │        │  ├─ _orc.pyx
   │        │  ├─ _parquet.cpython-311-darwin.so
   │        │  ├─ _parquet.pxd
   │        │  ├─ _parquet.pyx
   │        │  ├─ _parquet_encryption.cpython-311-darwin.so
   │        │  ├─ _parquet_encryption.pxd
   │        │  ├─ _parquet_encryption.pyx
   │        │  ├─ _pyarrow_cpp_tests.cpython-311-darwin.so
   │        │  ├─ _pyarrow_cpp_tests.pxd
   │        │  ├─ _pyarrow_cpp_tests.pyx
   │        │  ├─ _s3fs.cpython-311-darwin.so
   │        │  ├─ _s3fs.pyx
   │        │  ├─ _substrait.cpython-311-darwin.so
   │        │  ├─ _substrait.pyx
   │        │  ├─ acero.py
   │        │  ├─ array.pxi
   │        │  ├─ benchmark.pxi
   │        │  ├─ benchmark.py
   │        │  ├─ builder.pxi
   │        │  ├─ cffi.py
   │        │  ├─ compat.pxi
   │        │  ├─ compute.py
   │        │  ├─ config.pxi
   │        │  ├─ conftest.py
   │        │  ├─ csv.py
   │        │  ├─ cuda.py
   │        │  ├─ dataset.py
   │        │  ├─ device.pxi
   │        │  ├─ error.pxi
   │        │  ├─ feather.py
   │        │  ├─ flight.py
   │        │  ├─ fs.py
   │        │  ├─ gandiva.pyx
   │        │  ├─ include
   │        │  │  ├─ arrow
   │        │  │  │  ├─ acero
   │        │  │  │  │  ├─ accumulation_queue.h
   │        │  │  │  │  ├─ aggregate_node.h
   │        │  │  │  │  ├─ api.h
   │        │  │  │  │  ├─ asof_join_node.h
   │        │  │  │  │  ├─ backpressure_handler.h
   │        │  │  │  │  ├─ benchmark_util.h
   │        │  │  │  │  ├─ bloom_filter.h
   │        │  │  │  │  ├─ exec_plan.h
   │        │  │  │  │  ├─ hash_join.h
   │        │  │  │  │  ├─ hash_join_dict.h
   │        │  │  │  │  ├─ hash_join_node.h
   │        │  │  │  │  ├─ map_node.h
   │        │  │  │  │  ├─ options.h
   │        │  │  │  │  ├─ order_by_impl.h
   │        │  │  │  │  ├─ partition_util.h
   │        │  │  │  │  ├─ pch.h
   │        │  │  │  │  ├─ query_context.h
   │        │  │  │  │  ├─ schema_util.h
   │        │  │  │  │  ├─ task_util.h
   │        │  │  │  │  ├─ test_nodes.h
   │        │  │  │  │  ├─ time_series_util.h
   │        │  │  │  │  ├─ tpch_node.h
   │        │  │  │  │  ├─ type_fwd.h
   │        │  │  │  │  ├─ util.h
   │        │  │  │  │  └─ visibility.h
   │        │  │  │  ├─ adapters
   │        │  │  │  │  ├─ orc
   │        │  │  │  │  │  ├─ adapter.h
   │        │  │  │  │  │  └─ options.h
   │        │  │  │  │  └─ tensorflow
   │        │  │  │  │     └─ convert.h
   │        │  │  │  ├─ api.h
   │        │  │  │  ├─ array
   │        │  │  │  │  ├─ array_base.h
   │        │  │  │  │  ├─ array_binary.h
   │        │  │  │  │  ├─ array_decimal.h
   │        │  │  │  │  ├─ array_dict.h
   │        │  │  │  │  ├─ array_nested.h
   │        │  │  │  │  ├─ array_primitive.h
   │        │  │  │  │  ├─ array_run_end.h
   │        │  │  │  │  ├─ builder_adaptive.h
   │        │  │  │  │  ├─ builder_base.h
   │        │  │  │  │  ├─ builder_binary.h
   │        │  │  │  │  ├─ builder_decimal.h
   │        │  │  │  │  ├─ builder_dict.h
   │        │  │  │  │  ├─ builder_nested.h
   │        │  │  │  │  ├─ builder_primitive.h
   │        │  │  │  │  ├─ builder_run_end.h
   │        │  │  │  │  ├─ builder_time.h
   │        │  │  │  │  ├─ builder_union.h
   │        │  │  │  │  ├─ concatenate.h
   │        │  │  │  │  ├─ data.h
   │        │  │  │  │  ├─ diff.h
   │        │  │  │  │  ├─ statistics.h
   │        │  │  │  │  ├─ util.h
   │        │  │  │  │  └─ validate.h
   │        │  │  │  ├─ array.h
   │        │  │  │  ├─ buffer.h
   │        │  │  │  ├─ buffer_builder.h
   │        │  │  │  ├─ builder.h
   │        │  │  │  ├─ c
   │        │  │  │  │  ├─ abi.h
   │        │  │  │  │  ├─ bridge.h
   │        │  │  │  │  ├─ dlpack.h
   │        │  │  │  │  ├─ dlpack_abi.h
   │        │  │  │  │  └─ helpers.h
   │        │  │  │  ├─ chunk_resolver.h
   │        │  │  │  ├─ chunked_array.h
   │        │  │  │  ├─ compare.h
   │        │  │  │  ├─ compute
   │        │  │  │  │  ├─ api.h
   │        │  │  │  │  ├─ api_aggregate.h
   │        │  │  │  │  ├─ api_scalar.h
   │        │  │  │  │  ├─ api_vector.h
   │        │  │  │  │  ├─ cast.h
   │        │  │  │  │  ├─ exec.h
   │        │  │  │  │  ├─ expression.h
   │        │  │  │  │  ├─ function.h
   │        │  │  │  │  ├─ function_options.h
   │        │  │  │  │  ├─ kernel.h
   │        │  │  │  │  ├─ ordering.h
   │        │  │  │  │  ├─ registry.h
   │        │  │  │  │  ├─ row
   │        │  │  │  │  │  └─ grouper.h
   │        │  │  │  │  ├─ type_fwd.h
   │        │  │  │  │  └─ util.h
   │        │  │  │  ├─ config.h
   │        │  │  │  ├─ csv
   │        │  │  │  │  ├─ api.h
   │        │  │  │  │  ├─ chunker.h
   │        │  │  │  │  ├─ column_builder.h
   │        │  │  │  │  ├─ column_decoder.h
   │        │  │  │  │  ├─ converter.h
   │        │  │  │  │  ├─ invalid_row.h
   │        │  │  │  │  ├─ options.h
   │        │  │  │  │  ├─ parser.h
   │        │  │  │  │  ├─ reader.h
   │        │  │  │  │  ├─ test_common.h
   │        │  │  │  │  ├─ type_fwd.h
   │        │  │  │  │  └─ writer.h
   │        │  │  │  ├─ dataset
   │        │  │  │  │  ├─ api.h
   │        │  │  │  │  ├─ dataset.h
   │        │  │  │  │  ├─ dataset_writer.h
   │        │  │  │  │  ├─ discovery.h
   │        │  │  │  │  ├─ file_base.h
   │        │  │  │  │  ├─ file_csv.h
   │        │  │  │  │  ├─ file_ipc.h
   │        │  │  │  │  ├─ file_json.h
   │        │  │  │  │  ├─ file_orc.h
   │        │  │  │  │  ├─ file_parquet.h
   │        │  │  │  │  ├─ parquet_encryption_config.h
   │        │  │  │  │  ├─ partition.h
   │        │  │  │  │  ├─ pch.h
   │        │  │  │  │  ├─ plan.h
   │        │  │  │  │  ├─ projector.h
   │        │  │  │  │  ├─ scanner.h
   │        │  │  │  │  ├─ type_fwd.h
   │        │  │  │  │  └─ visibility.h
   │        │  │  │  ├─ datum.h
   │        │  │  │  ├─ device.h
   │        │  │  │  ├─ device_allocation_type_set.h
   │        │  │  │  ├─ engine
   │        │  │  │  │  ├─ api.h
   │        │  │  │  │  ├─ pch.h
   │        │  │  │  │  └─ substrait
   │        │  │  │  │     ├─ api.h
   │        │  │  │  │     ├─ extension_set.h
   │        │  │  │  │     ├─ extension_types.h
   │        │  │  │  │     ├─ options.h
   │        │  │  │  │     ├─ relation.h
   │        │  │  │  │     ├─ serde.h
   │        │  │  │  │     ├─ test_plan_builder.h
   │        │  │  │  │     ├─ test_util.h
   │        │  │  │  │     ├─ type_fwd.h
   │        │  │  │  │     ├─ util.h
   │        │  │  │  │     └─ visibility.h
   │        │  │  │  ├─ extension
   │        │  │  │  │  ├─ bool8.h
   │        │  │  │  │  ├─ fixed_shape_tensor.h
   │        │  │  │  │  ├─ json.h
   │        │  │  │  │  ├─ opaque.h
   │        │  │  │  │  └─ uuid.h
   │        │  │  │  ├─ extension_type.h
   │        │  │  │  ├─ filesystem
   │        │  │  │  │  ├─ api.h
   │        │  │  │  │  ├─ azurefs.h
   │        │  │  │  │  ├─ filesystem.h
   │        │  │  │  │  ├─ filesystem_library.h
   │        │  │  │  │  ├─ gcsfs.h
   │        │  │  │  │  ├─ hdfs.h
   │        │  │  │  │  ├─ localfs.h
   │        │  │  │  │  ├─ mockfs.h
   │        │  │  │  │  ├─ path_util.h
   │        │  │  │  │  ├─ s3_test_util.h
   │        │  │  │  │  ├─ s3fs.h
   │        │  │  │  │  ├─ test_util.h
   │        │  │  │  │  └─ type_fwd.h
   │        │  │  │  ├─ flight
   │        │  │  │  │  ├─ api.h
   │        │  │  │  │  ├─ client.h
   │        │  │  │  │  ├─ client_auth.h
   │        │  │  │  │  ├─ client_cookie_middleware.h
   │        │  │  │  │  ├─ client_middleware.h
   │        │  │  │  │  ├─ client_tracing_middleware.h
   │        │  │  │  │  ├─ middleware.h
   │        │  │  │  │  ├─ otel_logging.h
   │        │  │  │  │  ├─ pch.h
   │        │  │  │  │  ├─ platform.h
   │        │  │  │  │  ├─ server.h
   │        │  │  │  │  ├─ server_auth.h
   │        │  │  │  │  ├─ server_middleware.h
   │        │  │  │  │  ├─ server_tracing_middleware.h
   │        │  │  │  │  ├─ test_auth_handlers.h
   │        │  │  │  │  ├─ test_definitions.h
   │        │  │  │  │  ├─ test_flight_server.h
   │        │  │  │  │  ├─ test_util.h
   │        │  │  │  │  ├─ transport.h
   │        │  │  │  │  ├─ transport_server.h
   │        │  │  │  │  ├─ type_fwd.h
   │        │  │  │  │  ├─ types.h
   │        │  │  │  │  ├─ types_async.h
   │        │  │  │  │  └─ visibility.h
   │        │  │  │  ├─ io
   │        │  │  │  │  ├─ api.h
   │        │  │  │  │  ├─ buffered.h
   │        │  │  │  │  ├─ caching.h
   │        │  │  │  │  ├─ compressed.h
   │        │  │  │  │  ├─ concurrency.h
   │        │  │  │  │  ├─ file.h
   │        │  │  │  │  ├─ hdfs.h
   │        │  │  │  │  ├─ interfaces.h
   │        │  │  │  │  ├─ memory.h
   │        │  │  │  │  ├─ mman.h
   │        │  │  │  │  ├─ slow.h
   │        │  │  │  │  ├─ stdio.h
   │        │  │  │  │  ├─ test_common.h
   │        │  │  │  │  ├─ transform.h
   │        │  │  │  │  └─ type_fwd.h
   │        │  │  │  ├─ ipc
   │        │  │  │  │  ├─ api.h
   │        │  │  │  │  ├─ dictionary.h
   │        │  │  │  │  ├─ feather.h
   │        │  │  │  │  ├─ json_simple.h
   │        │  │  │  │  ├─ message.h
   │        │  │  │  │  ├─ options.h
   │        │  │  │  │  ├─ reader.h
   │        │  │  │  │  ├─ test_common.h
   │        │  │  │  │  ├─ type_fwd.h
   │        │  │  │  │  ├─ util.h
   │        │  │  │  │  └─ writer.h
   │        │  │  │  ├─ json
   │        │  │  │  │  ├─ api.h
   │        │  │  │  │  ├─ chunked_builder.h
   │        │  │  │  │  ├─ chunker.h
   │        │  │  │  │  ├─ converter.h
   │        │  │  │  │  ├─ object_parser.h
   │        │  │  │  │  ├─ object_writer.h
   │        │  │  │  │  ├─ options.h
   │        │  │  │  │  ├─ parser.h
   │        │  │  │  │  ├─ rapidjson_defs.h
   │        │  │  │  │  ├─ reader.h
   │        │  │  │  │  ├─ test_common.h
   │        │  │  │  │  └─ type_fwd.h
   │        │  │  │  ├─ memory_pool.h
   │        │  │  │  ├─ memory_pool_test.h
   │        │  │  │  ├─ pch.h
   │        │  │  │  ├─ pretty_print.h
   │        │  │  │  ├─ python
   │        │  │  │  │  ├─ api.h
   │        │  │  │  │  ├─ arrow_to_pandas.h
   │        │  │  │  │  ├─ async.h
   │        │  │  │  │  ├─ benchmark.h
   │        │  │  │  │  ├─ common.h
   │        │  │  │  │  ├─ csv.h
   │        │  │  │  │  ├─ datetime.h
   │        │  │  │  │  ├─ decimal.h
   │        │  │  │  │  ├─ extension_type.h
   │        │  │  │  │  ├─ filesystem.h
   │        │  │  │  │  ├─ flight.h
   │        │  │  │  │  ├─ gdb.h
   │        │  │  │  │  ├─ helpers.h
   │        │  │  │  │  ├─ inference.h
   │        │  │  │  │  ├─ io.h
   │        │  │  │  │  ├─ ipc.h
   │        │  │  │  │  ├─ iterators.h
   │        │  │  │  │  ├─ lib.h
   │        │  │  │  │  ├─ lib_api.h
   │        │  │  │  │  ├─ numpy_convert.h
   │        │  │  │  │  ├─ numpy_init.h
   │        │  │  │  │  ├─ numpy_interop.h
   │        │  │  │  │  ├─ numpy_to_arrow.h
   │        │  │  │  │  ├─ parquet_encryption.h
   │        │  │  │  │  ├─ pch.h
   │        │  │  │  │  ├─ platform.h
   │        │  │  │  │  ├─ pyarrow.h
   │        │  │  │  │  ├─ pyarrow_api.h
   │        │  │  │  │  ├─ pyarrow_lib.h
   │        │  │  │  │  ├─ python_test.h
   │        │  │  │  │  ├─ python_to_arrow.h
   │        │  │  │  │  ├─ type_traits.h
   │        │  │  │  │  ├─ udf.h
   │        │  │  │  │  ├─ vendored
   │        │  │  │  │  │  └─ pythoncapi_compat.h
   │        │  │  │  │  └─ visibility.h
   │        │  │  │  ├─ record_batch.h
   │        │  │  │  ├─ result.h
   │        │  │  │  ├─ scalar.h
   │        │  │  │  ├─ sparse_tensor.h
   │        │  │  │  ├─ status.h
   │        │  │  │  ├─ stl.h
   │        │  │  │  ├─ stl_allocator.h
   │        │  │  │  ├─ stl_iterator.h
   │        │  │  │  ├─ table.h
   │        │  │  │  ├─ table_builder.h
   │        │  │  │  ├─ tensor
   │        │  │  │  │  └─ converter.h
   │        │  │  │  ├─ tensor.h
   │        │  │  │  ├─ testing
   │        │  │  │  │  ├─ async_test_util.h
   │        │  │  │  │  ├─ builder.h
   │        │  │  │  │  ├─ executor_util.h
   │        │  │  │  │  ├─ extension_type.h
   │        │  │  │  │  ├─ fixed_width_test_util.h
   │        │  │  │  │  ├─ future_util.h
   │        │  │  │  │  ├─ generator.h
   │        │  │  │  │  ├─ gtest_compat.h
   │        │  │  │  │  ├─ gtest_util.h
   │        │  │  │  │  ├─ matchers.h
   │        │  │  │  │  ├─ math.h
   │        │  │  │  │  ├─ pch.h
   │        │  │  │  │  ├─ process.h
   │        │  │  │  │  ├─ random.h
   │        │  │  │  │  ├─ uniform_real.h
   │        │  │  │  │  ├─ util.h
   │        │  │  │  │  └─ visibility.h
   │        │  │  │  ├─ type.h
   │        │  │  │  ├─ type_fwd.h
   │        │  │  │  ├─ type_traits.h
   │        │  │  │  ├─ util
   │        │  │  │  │  ├─ algorithm.h
   │        │  │  │  │  ├─ align_util.h
   │        │  │  │  │  ├─ aligned_storage.h
   │        │  │  │  │  ├─ async_generator.h
   │        │  │  │  │  ├─ async_generator_fwd.h
   │        │  │  │  │  ├─ async_util.h
   │        │  │  │  │  ├─ base64.h
   │        │  │  │  │  ├─ basic_decimal.h
   │        │  │  │  │  ├─ benchmark_util.h
   │        │  │  │  │  ├─ binary_view_util.h
   │        │  │  │  │  ├─ bit_block_counter.h
   │        │  │  │  │  ├─ bit_run_reader.h
   │        │  │  │  │  ├─ bit_util.h
   │        │  │  │  │  ├─ bitmap.h
   │        │  │  │  │  ├─ bitmap_builders.h
   │        │  │  │  │  ├─ bitmap_generate.h
   │        │  │  │  │  ├─ bitmap_ops.h
   │        │  │  │  │  ├─ bitmap_reader.h
   │        │  │  │  │  ├─ bitmap_visit.h
   │        │  │  │  │  ├─ bitmap_writer.h
   │        │  │  │  │  ├─ bitset_stack.h
   │        │  │  │  │  ├─ bpacking.h
   │        │  │  │  │  ├─ bpacking64_default.h
   │        │  │  │  │  ├─ bpacking_avx2.h
   │        │  │  │  │  ├─ bpacking_avx512.h
   │        │  │  │  │  ├─ bpacking_default.h
   │        │  │  │  │  ├─ bpacking_neon.h
   │        │  │  │  │  ├─ byte_size.h
   │        │  │  │  │  ├─ cancel.h
   │        │  │  │  │  ├─ checked_cast.h
   │        │  │  │  │  ├─ compare.h
   │        │  │  │  │  ├─ compression.h
   │        │  │  │  │  ├─ concurrent_map.h
   │        │  │  │  │  ├─ config.h
   │        │  │  │  │  ├─ converter.h
   │        │  │  │  │  ├─ counting_semaphore.h
   │        │  │  │  │  ├─ cpu_info.h
   │        │  │  │  │  ├─ crc32.h
   │        │  │  │  │  ├─ debug.h
   │        │  │  │  │  ├─ decimal.h
   │        │  │  │  │  ├─ delimiting.h
   │        │  │  │  │  ├─ dict_util.h
   │        │  │  │  │  ├─ dispatch.h
   │        │  │  │  │  ├─ double_conversion.h
   │        │  │  │  │  ├─ endian.h
   │        │  │  │  │  ├─ float16.h
   │        │  │  │  │  ├─ formatting.h
   │        │  │  │  │  ├─ functional.h
   │        │  │  │  │  ├─ future.h
   │        │  │  │  │  ├─ hash_util.h
   │        │  │  │  │  ├─ hashing.h
   │        │  │  │  │  ├─ int_util.h
   │        │  │  │  │  ├─ int_util_overflow.h
   │        │  │  │  │  ├─ io_util.h
   │        │  │  │  │  ├─ iterator.h
   │        │  │  │  │  ├─ key_value_metadata.h
   │        │  │  │  │  ├─ launder.h
   │        │  │  │  │  ├─ list_util.h
   │        │  │  │  │  ├─ logger.h
   │        │  │  │  │  ├─ logging.h
   │        │  │  │  │  ├─ macros.h
   │        │  │  │  │  ├─ map.h
   │        │  │  │  │  ├─ math_constants.h
   │        │  │  │  │  ├─ memory.h
   │        │  │  │  │  ├─ mutex.h
   │        │  │  │  │  ├─ parallel.h
   │        │  │  │  │  ├─ pcg_random.h
   │        │  │  │  │  ├─ prefetch.h
   │        │  │  │  │  ├─ print.h
   │        │  │  │  │  ├─ queue.h
   │        │  │  │  │  ├─ range.h
   │        │  │  │  │  ├─ ree_util.h
   │        │  │  │  │  ├─ regex.h
   │        │  │  │  │  ├─ rows_to_batches.h
   │        │  │  │  │  ├─ simd.h
   │        │  │  │  │  ├─ small_vector.h
   │        │  │  │  │  ├─ sort.h
   │        │  │  │  │  ├─ spaced.h
   │        │  │  │  │  ├─ span.h
   │        │  │  │  │  ├─ stopwatch.h
   │        │  │  │  │  ├─ string.h
   │        │  │  │  │  ├─ string_builder.h
   │        │  │  │  │  ├─ task_group.h
   │        │  │  │  │  ├─ tdigest.h
   │        │  │  │  │  ├─ test_common.h
   │        │  │  │  │  ├─ thread_pool.h
   │        │  │  │  │  ├─ time.h
   │        │  │  │  │  ├─ tracing.h
   │        │  │  │  │  ├─ trie.h
   │        │  │  │  │  ├─ type_fwd.h
   │        │  │  │  │  ├─ type_traits.h
   │        │  │  │  │  ├─ ubsan.h
   │        │  │  │  │  ├─ union_util.h
   │        │  │  │  │  ├─ unreachable.h
   │        │  │  │  │  ├─ uri.h
   │        │  │  │  │  ├─ utf8.h
   │        │  │  │  │  ├─ value_parsing.h
   │        │  │  │  │  ├─ vector.h
   │        │  │  │  │  ├─ visibility.h
   │        │  │  │  │  ├─ windows_compatibility.h
   │        │  │  │  │  └─ windows_fixup.h
   │        │  │  │  ├─ vendored
   │        │  │  │  │  ├─ ProducerConsumerQueue.h
   │        │  │  │  │  ├─ datetime
   │        │  │  │  │  │  ├─ date.h
   │        │  │  │  │  │  ├─ ios.h
   │        │  │  │  │  │  ├─ tz.h
   │        │  │  │  │  │  ├─ tz_private.h
   │        │  │  │  │  │  └─ visibility.h
   │        │  │  │  │  ├─ datetime.h
   │        │  │  │  │  ├─ double-conversion
   │        │  │  │  │  │  ├─ bignum-dtoa.h
   │        │  │  │  │  │  ├─ bignum.h
   │        │  │  │  │  │  ├─ cached-powers.h
   │        │  │  │  │  │  ├─ diy-fp.h
   │        │  │  │  │  │  ├─ double-conversion.h
   │        │  │  │  │  │  ├─ double-to-string.h
   │        │  │  │  │  │  ├─ fast-dtoa.h
   │        │  │  │  │  │  ├─ fixed-dtoa.h
   │        │  │  │  │  │  ├─ ieee.h
   │        │  │  │  │  │  ├─ string-to-double.h
   │        │  │  │  │  │  ├─ strtod.h
   │        │  │  │  │  │  └─ utils.h
   │        │  │  │  │  ├─ pcg
   │        │  │  │  │  │  ├─ pcg_extras.hpp
   │        │  │  │  │  │  ├─ pcg_random.hpp
   │        │  │  │  │  │  └─ pcg_uint128.hpp
   │        │  │  │  │  ├─ portable-snippets
   │        │  │  │  │  │  ├─ debug-trap.h
   │        │  │  │  │  │  └─ safe-math.h
   │        │  │  │  │  ├─ strptime.h
   │        │  │  │  │  ├─ xxhash
   │        │  │  │  │  │  └─ xxhash.h
   │        │  │  │  │  └─ xxhash.h
   │        │  │  │  ├─ visit_array_inline.h
   │        │  │  │  ├─ visit_data_inline.h
   │        │  │  │  ├─ visit_scalar_inline.h
   │        │  │  │  ├─ visit_type_inline.h
   │        │  │  │  ├─ visitor.h
   │        │  │  │  └─ visitor_generate.h
   │        │  │  └─ parquet
   │        │  │     ├─ api
   │        │  │     │  ├─ io.h
   │        │  │     │  ├─ reader.h
   │        │  │     │  ├─ schema.h
   │        │  │     │  └─ writer.h
   │        │  │     ├─ arrow
   │        │  │     │  ├─ reader.h
   │        │  │     │  ├─ schema.h
   │        │  │     │  ├─ test_util.h
   │        │  │     │  └─ writer.h
   │        │  │     ├─ benchmark_util.h
   │        │  │     ├─ bloom_filter.h
   │        │  │     ├─ bloom_filter_reader.h
   │        │  │     ├─ column_page.h
   │        │  │     ├─ column_reader.h
   │        │  │     ├─ column_scanner.h
   │        │  │     ├─ column_writer.h
   │        │  │     ├─ encoding.h
   │        │  │     ├─ encryption
   │        │  │     │  ├─ crypto_factory.h
   │        │  │     │  ├─ encryption.h
   │        │  │     │  ├─ file_key_material_store.h
   │        │  │     │  ├─ file_key_unwrapper.h
   │        │  │     │  ├─ file_key_wrapper.h
   │        │  │     │  ├─ file_system_key_material_store.h
   │        │  │     │  ├─ key_encryption_key.h
   │        │  │     │  ├─ key_material.h
   │        │  │     │  ├─ key_metadata.h
   │        │  │     │  ├─ key_toolkit.h
   │        │  │     │  ├─ kms_client.h
   │        │  │     │  ├─ kms_client_factory.h
   │        │  │     │  ├─ local_wrap_kms_client.h
   │        │  │     │  ├─ test_encryption_util.h
   │        │  │     │  ├─ test_in_memory_kms.h
   │        │  │     │  ├─ two_level_cache_with_expiration.h
   │        │  │     │  └─ type_fwd.h
   │        │  │     ├─ exception.h
   │        │  │     ├─ file_reader.h
   │        │  │     ├─ file_writer.h
   │        │  │     ├─ hasher.h
   │        │  │     ├─ level_comparison.h
   │        │  │     ├─ level_comparison_inc.h
   │        │  │     ├─ level_conversion.h
   │        │  │     ├─ level_conversion_inc.h
   │        │  │     ├─ metadata.h
   │        │  │     ├─ page_index.h
   │        │  │     ├─ parquet_version.h
   │        │  │     ├─ pch.h
   │        │  │     ├─ platform.h
   │        │  │     ├─ printer.h
   │        │  │     ├─ properties.h
   │        │  │     ├─ schema.h
   │        │  │     ├─ size_statistics.h
   │        │  │     ├─ statistics.h
   │        │  │     ├─ stream_reader.h
   │        │  │     ├─ stream_writer.h
   │        │  │     ├─ test_util.h
   │        │  │     ├─ type_fwd.h
   │        │  │     ├─ types.h
   │        │  │     ├─ windows_compatibility.h
   │        │  │     ├─ windows_fixup.h
   │        │  │     └─ xxhasher.h
   │        │  ├─ includes
   │        │  │  ├─ __init__.pxd
   │        │  │  ├─ common.pxd
   │        │  │  ├─ libarrow.pxd
   │        │  │  ├─ libarrow_acero.pxd
   │        │  │  ├─ libarrow_cuda.pxd
   │        │  │  ├─ libarrow_dataset.pxd
   │        │  │  ├─ libarrow_dataset_parquet.pxd
   │        │  │  ├─ libarrow_feather.pxd
   │        │  │  ├─ libarrow_flight.pxd
   │        │  │  ├─ libarrow_fs.pxd
   │        │  │  ├─ libarrow_python.pxd
   │        │  │  ├─ libarrow_substrait.pxd
   │        │  │  ├─ libgandiva.pxd
   │        │  │  └─ libparquet_encryption.pxd
   │        │  ├─ interchange
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ buffer.cpython-311.pyc
   │        │  │  │  ├─ column.cpython-311.pyc
   │        │  │  │  ├─ dataframe.cpython-311.pyc
   │        │  │  │  └─ from_dataframe.cpython-311.pyc
   │        │  │  ├─ buffer.py
   │        │  │  ├─ column.py
   │        │  │  ├─ dataframe.py
   │        │  │  └─ from_dataframe.py
   │        │  ├─ io.pxi
   │        │  ├─ ipc.pxi
   │        │  ├─ ipc.py
   │        │  ├─ json.py
   │        │  ├─ jvm.py
   │        │  ├─ lib.cpython-311-darwin.so
   │        │  ├─ lib.h
   │        │  ├─ lib.pxd
   │        │  ├─ lib.pyx
   │        │  ├─ lib_api.h
   │        │  ├─ libarrow.2000.dylib
   │        │  ├─ libarrow_acero.2000.dylib
   │        │  ├─ libarrow_dataset.2000.dylib
   │        │  ├─ libarrow_flight.2000.dylib
   │        │  ├─ libarrow_python.2000.0.0.dylib
   │        │  ├─ libarrow_python.2000.dylib
   │        │  ├─ libarrow_python.dylib
   │        │  ├─ libarrow_python_flight.2000.0.0.dylib
   │        │  ├─ libarrow_python_flight.2000.dylib
   │        │  ├─ libarrow_python_flight.dylib
   │        │  ├─ libarrow_python_parquet_encryption.2000.0.0.dylib
   │        │  ├─ libarrow_python_parquet_encryption.2000.dylib
   │        │  ├─ libarrow_python_parquet_encryption.dylib
   │        │  ├─ libarrow_substrait.2000.dylib
   │        │  ├─ libparquet.2000.dylib
   │        │  ├─ memory.pxi
   │        │  ├─ orc.py
   │        │  ├─ pandas-shim.pxi
   │        │  ├─ pandas_compat.py
   │        │  ├─ parquet
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ core.cpython-311.pyc
   │        │  │  │  └─ encryption.cpython-311.pyc
   │        │  │  ├─ core.py
   │        │  │  └─ encryption.py
   │        │  ├─ public-api.pxi
   │        │  ├─ scalar.pxi
   │        │  ├─ src
   │        │  │  └─ arrow
   │        │  │     └─ python
   │        │  │        ├─ CMakeLists.txt
   │        │  │        ├─ api.h
   │        │  │        ├─ arrow_to_pandas.cc
   │        │  │        ├─ arrow_to_pandas.h
   │        │  │        ├─ arrow_to_python_internal.h
   │        │  │        ├─ async.h
   │        │  │        ├─ benchmark.cc
   │        │  │        ├─ benchmark.h
   │        │  │        ├─ common.cc
   │        │  │        ├─ common.h
   │        │  │        ├─ csv.cc
   │        │  │        ├─ csv.h
   │        │  │        ├─ datetime.cc
   │        │  │        ├─ datetime.h
   │        │  │        ├─ decimal.cc
   │        │  │        ├─ decimal.h
   │        │  │        ├─ extension_type.cc
   │        │  │        ├─ extension_type.h
   │        │  │        ├─ filesystem.cc
   │        │  │        ├─ filesystem.h
   │        │  │        ├─ flight.cc
   │        │  │        ├─ flight.h
   │        │  │        ├─ gdb.cc
   │        │  │        ├─ gdb.h
   │        │  │        ├─ helpers.cc
   │        │  │        ├─ helpers.h
   │        │  │        ├─ inference.cc
   │        │  │        ├─ inference.h
   │        │  │        ├─ io.cc
   │        │  │        ├─ io.h
   │        │  │        ├─ ipc.cc
   │        │  │        ├─ ipc.h
   │        │  │        ├─ iterators.h
   │        │  │        ├─ numpy_convert.cc
   │        │  │        ├─ numpy_convert.h
   │        │  │        ├─ numpy_init.cc
   │        │  │        ├─ numpy_init.h
   │        │  │        ├─ numpy_internal.h
   │        │  │        ├─ numpy_interop.h
   │        │  │        ├─ numpy_to_arrow.cc
   │        │  │        ├─ numpy_to_arrow.h
   │        │  │        ├─ parquet_encryption.cc
   │        │  │        ├─ parquet_encryption.h
   │        │  │        ├─ pch.h
   │        │  │        ├─ platform.h
   │        │  │        ├─ pyarrow.cc
   │        │  │        ├─ pyarrow.h
   │        │  │        ├─ pyarrow_api.h
   │        │  │        ├─ pyarrow_lib.h
   │        │  │        ├─ python_test.cc
   │        │  │        ├─ python_test.h
   │        │  │        ├─ python_to_arrow.cc
   │        │  │        ├─ python_to_arrow.h
   │        │  │        ├─ type_traits.h
   │        │  │        ├─ udf.cc
   │        │  │        ├─ udf.h
   │        │  │        ├─ vendored
   │        │  │        │  ├─ CMakeLists.txt
   │        │  │        │  └─ pythoncapi_compat.h
   │        │  │        └─ visibility.h
   │        │  ├─ substrait.py
   │        │  ├─ table.pxi
   │        │  ├─ tensor.pxi
   │        │  ├─ tests
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ arrow_16597.cpython-311.pyc
   │        │  │  │  ├─ arrow_39313.cpython-311.pyc
   │        │  │  │  ├─ arrow_7980.cpython-311.pyc
   │        │  │  │  ├─ conftest.cpython-311.pyc
   │        │  │  │  ├─ pandas_examples.cpython-311.pyc
   │        │  │  │  ├─ pandas_threaded_import.cpython-311.pyc
   │        │  │  │  ├─ read_record_batch.cpython-311.pyc
   │        │  │  │  ├─ strategies.cpython-311.pyc
   │        │  │  │  ├─ test_acero.cpython-311.pyc
   │        │  │  │  ├─ test_adhoc_memory_leak.cpython-311.pyc
   │        │  │  │  ├─ test_array.cpython-311.pyc
   │        │  │  │  ├─ test_builder.cpython-311.pyc
   │        │  │  │  ├─ test_cffi.cpython-311.pyc
   │        │  │  │  ├─ test_compute.cpython-311.pyc
   │        │  │  │  ├─ test_convert_builtin.cpython-311.pyc
   │        │  │  │  ├─ test_cpp_internals.cpython-311.pyc
   │        │  │  │  ├─ test_csv.cpython-311.pyc
   │        │  │  │  ├─ test_cuda.cpython-311.pyc
   │        │  │  │  ├─ test_cuda_numba_interop.cpython-311.pyc
   │        │  │  │  ├─ test_cython.cpython-311.pyc
   │        │  │  │  ├─ test_dataset.cpython-311.pyc
   │        │  │  │  ├─ test_dataset_encryption.cpython-311.pyc
   │        │  │  │  ├─ test_deprecations.cpython-311.pyc
   │        │  │  │  ├─ test_device.cpython-311.pyc
   │        │  │  │  ├─ test_dlpack.cpython-311.pyc
   │        │  │  │  ├─ test_exec_plan.cpython-311.pyc
   │        │  │  │  ├─ test_extension_type.cpython-311.pyc
   │        │  │  │  ├─ test_feather.cpython-311.pyc
   │        │  │  │  ├─ test_flight.cpython-311.pyc
   │        │  │  │  ├─ test_flight_async.cpython-311.pyc
   │        │  │  │  ├─ test_fs.cpython-311.pyc
   │        │  │  │  ├─ test_gandiva.cpython-311.pyc
   │        │  │  │  ├─ test_gdb.cpython-311.pyc
   │        │  │  │  ├─ test_io.cpython-311.pyc
   │        │  │  │  ├─ test_ipc.cpython-311.pyc
   │        │  │  │  ├─ test_json.cpython-311.pyc
   │        │  │  │  ├─ test_jvm.cpython-311.pyc
   │        │  │  │  ├─ test_memory.cpython-311.pyc
   │        │  │  │  ├─ test_misc.cpython-311.pyc
   │        │  │  │  ├─ test_orc.cpython-311.pyc
   │        │  │  │  ├─ test_pandas.cpython-311.pyc
   │        │  │  │  ├─ test_scalars.cpython-311.pyc
   │        │  │  │  ├─ test_schema.cpython-311.pyc
   │        │  │  │  ├─ test_sparse_tensor.cpython-311.pyc
   │        │  │  │  ├─ test_strategies.cpython-311.pyc
   │        │  │  │  ├─ test_substrait.cpython-311.pyc
   │        │  │  │  ├─ test_table.cpython-311.pyc
   │        │  │  │  ├─ test_tensor.cpython-311.pyc
   │        │  │  │  ├─ test_types.cpython-311.pyc
   │        │  │  │  ├─ test_udf.cpython-311.pyc
   │        │  │  │  ├─ test_util.cpython-311.pyc
   │        │  │  │  ├─ test_without_numpy.cpython-311.pyc
   │        │  │  │  ├─ util.cpython-311.pyc
   │        │  │  │  └─ wsgi_examples.cpython-311.pyc
   │        │  │  ├─ arrow_16597.py
   │        │  │  ├─ arrow_39313.py
   │        │  │  ├─ arrow_7980.py
   │        │  │  ├─ bound_function_visit_strings.pyx
   │        │  │  ├─ conftest.py
   │        │  │  ├─ data
   │        │  │  │  ├─ feather
   │        │  │  │  │  └─ v0.17.0.version.2-compression.lz4.feather
   │        │  │  │  ├─ orc
   │        │  │  │  │  ├─ README.md
   │        │  │  │  │  ├─ TestOrcFile.emptyFile.jsn.gz
   │        │  │  │  │  ├─ TestOrcFile.emptyFile.orc
   │        │  │  │  │  ├─ TestOrcFile.test1.jsn.gz
   │        │  │  │  │  ├─ TestOrcFile.test1.orc
   │        │  │  │  │  ├─ TestOrcFile.testDate1900.jsn.gz
   │        │  │  │  │  ├─ TestOrcFile.testDate1900.orc
   │        │  │  │  │  ├─ decimal.jsn.gz
   │        │  │  │  │  └─ decimal.orc
   │        │  │  │  └─ parquet
   │        │  │  │     ├─ v0.7.1.all-named-index.parquet
   │        │  │  │     ├─ v0.7.1.column-metadata-handling.parquet
   │        │  │  │     ├─ v0.7.1.parquet
   │        │  │  │     └─ v0.7.1.some-named-index.parquet
   │        │  │  ├─ extensions.pyx
   │        │  │  ├─ interchange
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test_conversion.cpython-311.pyc
   │        │  │  │  │  └─ test_interchange_spec.cpython-311.pyc
   │        │  │  │  ├─ test_conversion.py
   │        │  │  │  └─ test_interchange_spec.py
   │        │  │  ├─ pandas_examples.py
   │        │  │  ├─ pandas_threaded_import.py
   │        │  │  ├─ parquet
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ common.cpython-311.pyc
   │        │  │  │  │  ├─ conftest.cpython-311.pyc
   │        │  │  │  │  ├─ encryption.cpython-311.pyc
   │        │  │  │  │  ├─ test_basic.cpython-311.pyc
   │        │  │  │  │  ├─ test_compliant_nested_type.cpython-311.pyc
   │        │  │  │  │  ├─ test_data_types.cpython-311.pyc
   │        │  │  │  │  ├─ test_dataset.cpython-311.pyc
   │        │  │  │  │  ├─ test_datetime.cpython-311.pyc
   │        │  │  │  │  ├─ test_encryption.cpython-311.pyc
   │        │  │  │  │  ├─ test_metadata.cpython-311.pyc
   │        │  │  │  │  ├─ test_pandas.cpython-311.pyc
   │        │  │  │  │  ├─ test_parquet_file.cpython-311.pyc
   │        │  │  │  │  └─ test_parquet_writer.cpython-311.pyc
   │        │  │  │  ├─ common.py
   │        │  │  │  ├─ conftest.py
   │        │  │  │  ├─ encryption.py
   │        │  │  │  ├─ test_basic.py
   │        │  │  │  ├─ test_compliant_nested_type.py
   │        │  │  │  ├─ test_data_types.py
   │        │  │  │  ├─ test_dataset.py
   │        │  │  │  ├─ test_datetime.py
   │        │  │  │  ├─ test_encryption.py
   │        │  │  │  ├─ test_metadata.py
   │        │  │  │  ├─ test_pandas.py
   │        │  │  │  ├─ test_parquet_file.py
   │        │  │  │  └─ test_parquet_writer.py
   │        │  │  ├─ pyarrow_cython_example.pyx
   │        │  │  ├─ read_record_batch.py
   │        │  │  ├─ strategies.py
   │        │  │  ├─ test_acero.py
   │        │  │  ├─ test_adhoc_memory_leak.py
   │        │  │  ├─ test_array.py
   │        │  │  ├─ test_builder.py
   │        │  │  ├─ test_cffi.py
   │        │  │  ├─ test_compute.py
   │        │  │  ├─ test_convert_builtin.py
   │        │  │  ├─ test_cpp_internals.py
   │        │  │  ├─ test_csv.py
   │        │  │  ├─ test_cuda.py
   │        │  │  ├─ test_cuda_numba_interop.py
   │        │  │  ├─ test_cython.py
   │        │  │  ├─ test_dataset.py
   │        │  │  ├─ test_dataset_encryption.py
   │        │  │  ├─ test_deprecations.py
   │        │  │  ├─ test_device.py
   │        │  │  ├─ test_dlpack.py
   │        │  │  ├─ test_exec_plan.py
   │        │  │  ├─ test_extension_type.py
   │        │  │  ├─ test_feather.py
   │        │  │  ├─ test_flight.py
   │        │  │  ├─ test_flight_async.py
   │        │  │  ├─ test_fs.py
   │        │  │  ├─ test_gandiva.py
   │        │  │  ├─ test_gdb.py
   │        │  │  ├─ test_io.py
   │        │  │  ├─ test_ipc.py
   │        │  │  ├─ test_json.py
   │        │  │  ├─ test_jvm.py
   │        │  │  ├─ test_memory.py
   │        │  │  ├─ test_misc.py
   │        │  │  ├─ test_orc.py
   │        │  │  ├─ test_pandas.py
   │        │  │  ├─ test_scalars.py
   │        │  │  ├─ test_schema.py
   │        │  │  ├─ test_sparse_tensor.py
   │        │  │  ├─ test_strategies.py
   │        │  │  ├─ test_substrait.py
   │        │  │  ├─ test_table.py
   │        │  │  ├─ test_tensor.py
   │        │  │  ├─ test_types.py
   │        │  │  ├─ test_udf.py
   │        │  │  ├─ test_util.py
   │        │  │  ├─ test_without_numpy.py
   │        │  │  ├─ util.py
   │        │  │  └─ wsgi_examples.py
   │        │  ├─ types.pxi
   │        │  ├─ types.py
   │        │  ├─ util.py
   │        │  └─ vendored
   │        │     ├─ __init__.py
   │        │     ├─ __pycache__
   │        │     │  ├─ __init__.cpython-311.pyc
   │        │     │  ├─ docscrape.cpython-311.pyc
   │        │     │  └─ version.cpython-311.pyc
   │        │     ├─ docscrape.py
   │        │     └─ version.py
   │        ├─ pyarrow-20.0.0.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  ├─ licenses
   │        │  │  ├─ LICENSE.txt
   │        │  │  └─ NOTICE.txt
   │        │  └─ top_level.txt
   │        ├─ pydeck
   │        │  ├─ .DS_Store
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ _version.cpython-311.pyc
   │        │  │  ├─ frontend_semver.cpython-311.pyc
   │        │  │  └─ settings.cpython-311.pyc
   │        │  ├─ _version.py
   │        │  ├─ bindings
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ base_map_provider.cpython-311.pyc
   │        │  │  │  ├─ deck.cpython-311.pyc
   │        │  │  │  ├─ json_tools.cpython-311.pyc
   │        │  │  │  ├─ layer.cpython-311.pyc
   │        │  │  │  ├─ light_settings.cpython-311.pyc
   │        │  │  │  ├─ map_styles.cpython-311.pyc
   │        │  │  │  ├─ view.cpython-311.pyc
   │        │  │  │  └─ view_state.cpython-311.pyc
   │        │  │  ├─ base_map_provider.py
   │        │  │  ├─ deck.py
   │        │  │  ├─ json_tools.py
   │        │  │  ├─ layer.py
   │        │  │  ├─ light_settings.py
   │        │  │  ├─ map_styles.py
   │        │  │  ├─ view.py
   │        │  │  └─ view_state.py
   │        │  ├─ data_utils
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ binary_transfer.cpython-311.pyc
   │        │  │  │  ├─ color_scales.cpython-311.pyc
   │        │  │  │  ├─ type_checking.cpython-311.pyc
   │        │  │  │  └─ viewport_helpers.cpython-311.pyc
   │        │  │  ├─ binary_transfer.py
   │        │  │  ├─ color_scales.py
   │        │  │  ├─ type_checking.py
   │        │  │  └─ viewport_helpers.py
   │        │  ├─ exceptions
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  └─ exceptions.cpython-311.pyc
   │        │  │  └─ exceptions.py
   │        │  ├─ frontend_semver.py
   │        │  ├─ io
   │        │  │  ├─ .DS_Store
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  └─ html.cpython-311.pyc
   │        │  │  ├─ html.py
   │        │  │  └─ templates
   │        │  │     ├─ index.j2
   │        │  │     └─ style.j2
   │        │  ├─ nbextension
   │        │  │  ├─ .DS_Store
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  └─ static
   │        │  │     ├─ .DS_Store
   │        │  │     ├─ extensionRequires.js
   │        │  │     ├─ index.js
   │        │  │     └─ index.js.map
   │        │  ├─ settings.py
   │        │  ├─ types
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ base.cpython-311.pyc
   │        │  │  │  ├─ function.cpython-311.pyc
   │        │  │  │  ├─ image.cpython-311.pyc
   │        │  │  │  └─ string.cpython-311.pyc
   │        │  │  ├─ base.py
   │        │  │  ├─ function.py
   │        │  │  ├─ image.py
   │        │  │  └─ string.py
   │        │  └─ widget
   │        │     ├─ __init__.py
   │        │     ├─ __pycache__
   │        │     │  ├─ __init__.cpython-311.pyc
   │        │     │  ├─ _frontend.cpython-311.pyc
   │        │     │  ├─ debounce.cpython-311.pyc
   │        │     │  └─ widget.cpython-311.pyc
   │        │     ├─ _frontend.py
   │        │     ├─ debounce.py
   │        │     └─ widget.py
   │        ├─ pydeck-0.9.1.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ LICENSE.txt
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  └─ top_level.txt
   │        ├─ python_dateutil-2.9.0.post0.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ LICENSE
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  ├─ top_level.txt
   │        │  └─ zip-safe
   │        ├─ pytz
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  ├─ lazy.cpython-311.pyc
   │        │  │  ├─ reference.cpython-311.pyc
   │        │  │  ├─ tzfile.cpython-311.pyc
   │        │  │  └─ tzinfo.cpython-311.pyc
   │        │  ├─ exceptions.py
   │        │  ├─ lazy.py
   │        │  ├─ reference.py
   │        │  ├─ tzfile.py
   │        │  ├─ tzinfo.py
   │        │  └─ zoneinfo
   │        │     ├─ Africa
   │        │     │  ├─ Abidjan
   │        │     │  ├─ Accra
   │        │     │  ├─ Addis_Ababa
   │        │     │  ├─ Algiers
   │        │     │  ├─ Asmara
   │        │     │  ├─ Asmera
   │        │     │  ├─ Bamako
   │        │     │  ├─ Bangui
   │        │     │  ├─ Banjul
   │        │     │  ├─ Bissau
   │        │     │  ├─ Blantyre
   │        │     │  ├─ Brazzaville
   │        │     │  ├─ Bujumbura
   │        │     │  ├─ Cairo
   │        │     │  ├─ Casablanca
   │        │     │  ├─ Ceuta
   │        │     │  ├─ Conakry
   │        │     │  ├─ Dakar
   │        │     │  ├─ Dar_es_Salaam
   │        │     │  ├─ Djibouti
   │        │     │  ├─ Douala
   │        │     │  ├─ El_Aaiun
   │        │     │  ├─ Freetown
   │        │     │  ├─ Gaborone
   │        │     │  ├─ Harare
   │        │     │  ├─ Johannesburg
   │        │     │  ├─ Juba
   │        │     │  ├─ Kampala
   │        │     │  ├─ Khartoum
   │        │     │  ├─ Kigali
   │        │     │  ├─ Kinshasa
   │        │     │  ├─ Lagos
   │        │     │  ├─ Libreville
   │        │     │  ├─ Lome
   │        │     │  ├─ Luanda
   │        │     │  ├─ Lubumbashi
   │        │     │  ├─ Lusaka
   │        │     │  ├─ Malabo
   │        │     │  ├─ Maputo
   │        │     │  ├─ Maseru
   │        │     │  ├─ Mbabane
   │        │     │  ├─ Mogadishu
   │        │     │  ├─ Monrovia
   │        │     │  ├─ Nairobi
   │        │     │  ├─ Ndjamena
   │        │     │  ├─ Niamey
   │        │     │  ├─ Nouakchott
   │        │     │  ├─ Ouagadougou
   │        │     │  ├─ Porto-Novo
   │        │     │  ├─ Sao_Tome
   │        │     │  ├─ Timbuktu
   │        │     │  ├─ Tripoli
   │        │     │  ├─ Tunis
   │        │     │  └─ Windhoek
   │        │     ├─ America
   │        │     │  ├─ Adak
   │        │     │  ├─ Anchorage
   │        │     │  ├─ Anguilla
   │        │     │  ├─ Antigua
   │        │     │  ├─ Araguaina
   │        │     │  ├─ Argentina
   │        │     │  │  ├─ Buenos_Aires
   │        │     │  │  ├─ Catamarca
   │        │     │  │  ├─ ComodRivadavia
   │        │     │  │  ├─ Cordoba
   │        │     │  │  ├─ Jujuy
   │        │     │  │  ├─ La_Rioja
   │        │     │  │  ├─ Mendoza
   │        │     │  │  ├─ Rio_Gallegos
   │        │     │  │  ├─ Salta
   │        │     │  │  ├─ San_Juan
   │        │     │  │  ├─ San_Luis
   │        │     │  │  ├─ Tucuman
   │        │     │  │  └─ Ushuaia
   │        │     │  ├─ Aruba
   │        │     │  ├─ Asuncion
   │        │     │  ├─ Atikokan
   │        │     │  ├─ Atka
   │        │     │  ├─ Bahia
   │        │     │  ├─ Bahia_Banderas
   │        │     │  ├─ Barbados
   │        │     │  ├─ Belem
   │        │     │  ├─ Belize
   │        │     │  ├─ Blanc-Sablon
   │        │     │  ├─ Boa_Vista
   │        │     │  ├─ Bogota
   │        │     │  ├─ Boise
   │        │     │  ├─ Buenos_Aires
   │        │     │  ├─ Cambridge_Bay
   │        │     │  ├─ Campo_Grande
   │        │     │  ├─ Cancun
   │        │     │  ├─ Caracas
   │        │     │  ├─ Catamarca
   │        │     │  ├─ Cayenne
   │        │     │  ├─ Cayman
   │        │     │  ├─ Chicago
   │        │     │  ├─ Chihuahua
   │        │     │  ├─ Ciudad_Juarez
   │        │     │  ├─ Coral_Harbour
   │        │     │  ├─ Cordoba
   │        │     │  ├─ Costa_Rica
   │        │     │  ├─ Coyhaique
   │        │     │  ├─ Creston
   │        │     │  ├─ Cuiaba
   │        │     │  ├─ Curacao
   │        │     │  ├─ Danmarkshavn
   │        │     │  ├─ Dawson
   │        │     │  ├─ Dawson_Creek
   │        │     │  ├─ Denver
   │        │     │  ├─ Detroit
   │        │     │  ├─ Dominica
   │        │     │  ├─ Edmonton
   │        │     │  ├─ Eirunepe
   │        │     │  ├─ El_Salvador
   │        │     │  ├─ Ensenada
   │        │     │  ├─ Fort_Nelson
   │        │     │  ├─ Fort_Wayne
   │        │     │  ├─ Fortaleza
   │        │     │  ├─ Glace_Bay
   │        │     │  ├─ Godthab
   │        │     │  ├─ Goose_Bay
   │        │     │  ├─ Grand_Turk
   │        │     │  ├─ Grenada
   │        │     │  ├─ Guadeloupe
   │        │     │  ├─ Guatemala
   │        │     │  ├─ Guayaquil
   │        │     │  ├─ Guyana
   │        │     │  ├─ Halifax
   │        │     │  ├─ Havana
   │        │     │  ├─ Hermosillo
   │        │     │  ├─ Indiana
   │        │     │  │  ├─ Indianapolis
   │        │     │  │  ├─ Knox
   │        │     │  │  ├─ Marengo
   │        │     │  │  ├─ Petersburg
   │        │     │  │  ├─ Tell_City
   │        │     │  │  ├─ Vevay
   │        │     │  │  ├─ Vincennes
   │        │     │  │  └─ Winamac
   │        │     │  ├─ Indianapolis
   │        │     │  ├─ Inuvik
   │        │     │  ├─ Iqaluit
   │        │     │  ├─ Jamaica
   │        │     │  ├─ Jujuy
   │        │     │  ├─ Juneau
   │        │     │  ├─ Kentucky
   │        │     │  │  ├─ Louisville
   │        │     │  │  └─ Monticello
   │        │     │  ├─ Knox_IN
   │        │     │  ├─ Kralendijk
   │        │     │  ├─ La_Paz
   │        │     │  ├─ Lima
   │        │     │  ├─ Los_Angeles
   │        │     │  ├─ Louisville
   │        │     │  ├─ Lower_Princes
   │        │     │  ├─ Maceio
   │        │     │  ├─ Managua
   │        │     │  ├─ Manaus
   │        │     │  ├─ Marigot
   │        │     │  ├─ Martinique
   │        │     │  ├─ Matamoros
   │        │     │  ├─ Mazatlan
   │        │     │  ├─ Mendoza
   │        │     │  ├─ Menominee
   │        │     │  ├─ Merida
   │        │     │  ├─ Metlakatla
   │        │     │  ├─ Mexico_City
   │        │     │  ├─ Miquelon
   │        │     │  ├─ Moncton
   │        │     │  ├─ Monterrey
   │        │     │  ├─ Montevideo
   │        │     │  ├─ Montreal
   │        │     │  ├─ Montserrat
   │        │     │  ├─ Nassau
   │        │     │  ├─ New_York
   │        │     │  ├─ Nipigon
   │        │     │  ├─ Nome
   │        │     │  ├─ Noronha
   │        │     │  ├─ North_Dakota
   │        │     │  │  ├─ Beulah
   │        │     │  │  ├─ Center
   │        │     │  │  └─ New_Salem
   │        │     │  ├─ Nuuk
   │        │     │  ├─ Ojinaga
   │        │     │  ├─ Panama
   │        │     │  ├─ Pangnirtung
   │        │     │  ├─ Paramaribo
   │        │     │  ├─ Phoenix
   │        │     │  ├─ Port-au-Prince
   │        │     │  ├─ Port_of_Spain
   │        │     │  ├─ Porto_Acre
   │        │     │  ├─ Porto_Velho
   │        │     │  ├─ Puerto_Rico
   │        │     │  ├─ Punta_Arenas
   │        │     │  ├─ Rainy_River
   │        │     │  ├─ Rankin_Inlet
   │        │     │  ├─ Recife
   │        │     │  ├─ Regina
   │        │     │  ├─ Resolute
   │        │     │  ├─ Rio_Branco
   │        │     │  ├─ Rosario
   │        │     │  ├─ Santa_Isabel
   │        │     │  ├─ Santarem
   │        │     │  ├─ Santiago
   │        │     │  ├─ Santo_Domingo
   │        │     │  ├─ Sao_Paulo
   │        │     │  ├─ Scoresbysund
   │        │     │  ├─ Shiprock
   │        │     │  ├─ Sitka
   │        │     │  ├─ St_Barthelemy
   │        │     │  ├─ St_Johns
   │        │     │  ├─ St_Kitts
   │        │     │  ├─ St_Lucia
   │        │     │  ├─ St_Thomas
   │        │     │  ├─ St_Vincent
   │        │     │  ├─ Swift_Current
   │        │     │  ├─ Tegucigalpa
   │        │     │  ├─ Thule
   │        │     │  ├─ Thunder_Bay
   │        │     │  ├─ Tijuana
   │        │     │  ├─ Toronto
   │        │     │  ├─ Tortola
   │        │     │  ├─ Vancouver
   │        │     │  ├─ Virgin
   │        │     │  ├─ Whitehorse
   │        │     │  ├─ Winnipeg
   │        │     │  ├─ Yakutat
   │        │     │  └─ Yellowknife
   │        │     ├─ Antarctica
   │        │     │  ├─ Casey
   │        │     │  ├─ Davis
   │        │     │  ├─ DumontDUrville
   │        │     │  ├─ Macquarie
   │        │     │  ├─ Mawson
   │        │     │  ├─ McMurdo
   │        │     │  ├─ Palmer
   │        │     │  ├─ Rothera
   │        │     │  ├─ South_Pole
   │        │     │  ├─ Syowa
   │        │     │  ├─ Troll
   │        │     │  └─ Vostok
   │        │     ├─ Arctic
   │        │     │  └─ Longyearbyen
   │        │     ├─ Asia
   │        │     │  ├─ Aden
   │        │     │  ├─ Almaty
   │        │     │  ├─ Amman
   │        │     │  ├─ Anadyr
   │        │     │  ├─ Aqtau
   │        │     │  ├─ Aqtobe
   │        │     │  ├─ Ashgabat
   │        │     │  ├─ Ashkhabad
   │        │     │  ├─ Atyrau
   │        │     │  ├─ Baghdad
   │        │     │  ├─ Bahrain
   │        │     │  ├─ Baku
   │        │     │  ├─ Bangkok
   │        │     │  ├─ Barnaul
   │        │     │  ├─ Beirut
   │        │     │  ├─ Bishkek
   │        │     │  ├─ Brunei
   │        │     │  ├─ Calcutta
   │        │     │  ├─ Chita
   │        │     │  ├─ Choibalsan
   │        │     │  ├─ Chongqing
   │        │     │  ├─ Chungking
   │        │     │  ├─ Colombo
   │        │     │  ├─ Dacca
   │        │     │  ├─ Damascus
   │        │     │  ├─ Dhaka
   │        │     │  ├─ Dili
   │        │     │  ├─ Dubai
   │        │     │  ├─ Dushanbe
   │        │     │  ├─ Famagusta
   │        │     │  ├─ Gaza
   │        │     │  ├─ Harbin
   │        │     │  ├─ Hebron
   │        │     │  ├─ Ho_Chi_Minh
   │        │     │  ├─ Hong_Kong
   │        │     │  ├─ Hovd
   │        │     │  ├─ Irkutsk
   │        │     │  ├─ Istanbul
   │        │     │  ├─ Jakarta
   │        │     │  ├─ Jayapura
   │        │     │  ├─ Jerusalem
   │        │     │  ├─ Kabul
   │        │     │  ├─ Kamchatka
   │        │     │  ├─ Karachi
   │        │     │  ├─ Kashgar
   │        │     │  ├─ Kathmandu
   │        │     │  ├─ Katmandu
   │        │     │  ├─ Khandyga
   │        │     │  ├─ Kolkata
   │        │     │  ├─ Krasnoyarsk
   │        │     │  ├─ Kuala_Lumpur
   │        │     │  ├─ Kuching
   │        │     │  ├─ Kuwait
   │        │     │  ├─ Macao
   │        │     │  ├─ Macau
   │        │     │  ├─ Magadan
   │        │     │  ├─ Makassar
   │        │     │  ├─ Manila
   │        │     │  ├─ Muscat
   │        │     │  ├─ Nicosia
   │        │     │  ├─ Novokuznetsk
   │        │     │  ├─ Novosibirsk
   │        │     │  ├─ Omsk
   │        │     │  ├─ Oral
   │        │     │  ├─ Phnom_Penh
   │        │     │  ├─ Pontianak
   │        │     │  ├─ Pyongyang
   │        │     │  ├─ Qatar
   │        │     │  ├─ Qostanay
   │        │     │  ├─ Qyzylorda
   │        │     │  ├─ Rangoon
   │        │     │  ├─ Riyadh
   │        │     │  ├─ Saigon
   │        │     │  ├─ Sakhalin
   │        │     │  ├─ Samarkand
   │        │     │  ├─ Seoul
   │        │     │  ├─ Shanghai
   │        │     │  ├─ Singapore
   │        │     │  ├─ Srednekolymsk
   │        │     │  ├─ Taipei
   │        │     │  ├─ Tashkent
   │        │     │  ├─ Tbilisi
   │        │     │  ├─ Tehran
   │        │     │  ├─ Tel_Aviv
   │        │     │  ├─ Thimbu
   │        │     │  ├─ Thimphu
   │        │     │  ├─ Tokyo
   │        │     │  ├─ Tomsk
   │        │     │  ├─ Ujung_Pandang
   │        │     │  ├─ Ulaanbaatar
   │        │     │  ├─ Ulan_Bator
   │        │     │  ├─ Urumqi
   │        │     │  ├─ Ust-Nera
   │        │     │  ├─ Vientiane
   │        │     │  ├─ Vladivostok
   │        │     │  ├─ Yakutsk
   │        │     │  ├─ Yangon
   │        │     │  ├─ Yekaterinburg
   │        │     │  └─ Yerevan
   │        │     ├─ Atlantic
   │        │     │  ├─ Azores
   │        │     │  ├─ Bermuda
   │        │     │  ├─ Canary
   │        │     │  ├─ Cape_Verde
   │        │     │  ├─ Faeroe
   │        │     │  ├─ Faroe
   │        │     │  ├─ Jan_Mayen
   │        │     │  ├─ Madeira
   │        │     │  ├─ Reykjavik
   │        │     │  ├─ South_Georgia
   │        │     │  ├─ St_Helena
   │        │     │  └─ Stanley
   │        │     ├─ Australia
   │        │     │  ├─ ACT
   │        │     │  ├─ Adelaide
   │        │     │  ├─ Brisbane
   │        │     │  ├─ Broken_Hill
   │        │     │  ├─ Canberra
   │        │     │  ├─ Currie
   │        │     │  ├─ Darwin
   │        │     │  ├─ Eucla
   │        │     │  ├─ Hobart
   │        │     │  ├─ LHI
   │        │     │  ├─ Lindeman
   │        │     │  ├─ Lord_Howe
   │        │     │  ├─ Melbourne
   │        │     │  ├─ NSW
   │        │     │  ├─ North
   │        │     │  ├─ Perth
   │        │     │  ├─ Queensland
   │        │     │  ├─ South
   │        │     │  ├─ Sydney
   │        │     │  ├─ Tasmania
   │        │     │  ├─ Victoria
   │        │     │  ├─ West
   │        │     │  └─ Yancowinna
   │        │     ├─ Brazil
   │        │     │  ├─ Acre
   │        │     │  ├─ DeNoronha
   │        │     │  ├─ East
   │        │     │  └─ West
   │        │     ├─ CET
   │        │     ├─ CST6CDT
   │        │     ├─ Canada
   │        │     │  ├─ Atlantic
   │        │     │  ├─ Central
   │        │     │  ├─ Eastern
   │        │     │  ├─ Mountain
   │        │     │  ├─ Newfoundland
   │        │     │  ├─ Pacific
   │        │     │  ├─ Saskatchewan
   │        │     │  └─ Yukon
   │        │     ├─ Chile
   │        │     │  ├─ Continental
   │        │     │  └─ EasterIsland
   │        │     ├─ Cuba
   │        │     ├─ EET
   │        │     ├─ EST
   │        │     ├─ EST5EDT
   │        │     ├─ Egypt
   │        │     ├─ Eire
   │        │     ├─ Etc
   │        │     │  ├─ GMT
   │        │     │  ├─ GMT+0
   │        │     │  ├─ GMT+1
   │        │     │  ├─ GMT+10
   │        │     │  ├─ GMT+11
   │        │     │  ├─ GMT+12
   │        │     │  ├─ GMT+2
   │        │     │  ├─ GMT+3
   │        │     │  ├─ GMT+4
   │        │     │  ├─ GMT+5
   │        │     │  ├─ GMT+6
   │        │     │  ├─ GMT+7
   │        │     │  ├─ GMT+8
   │        │     │  ├─ GMT+9
   │        │     │  ├─ GMT-0
   │        │     │  ├─ GMT-1
   │        │     │  ├─ GMT-10
   │        │     │  ├─ GMT-11
   │        │     │  ├─ GMT-12
   │        │     │  ├─ GMT-13
   │        │     │  ├─ GMT-14
   │        │     │  ├─ GMT-2
   │        │     │  ├─ GMT-3
   │        │     │  ├─ GMT-4
   │        │     │  ├─ GMT-5
   │        │     │  ├─ GMT-6
   │        │     │  ├─ GMT-7
   │        │     │  ├─ GMT-8
   │        │     │  ├─ GMT-9
   │        │     │  ├─ GMT0
   │        │     │  ├─ Greenwich
   │        │     │  ├─ UCT
   │        │     │  ├─ UTC
   │        │     │  ├─ Universal
   │        │     │  └─ Zulu
   │        │     ├─ Europe
   │        │     │  ├─ Amsterdam
   │        │     │  ├─ Andorra
   │        │     │  ├─ Astrakhan
   │        │     │  ├─ Athens
   │        │     │  ├─ Belfast
   │        │     │  ├─ Belgrade
   │        │     │  ├─ Berlin
   │        │     │  ├─ Bratislava
   │        │     │  ├─ Brussels
   │        │     │  ├─ Bucharest
   │        │     │  ├─ Budapest
   │        │     │  ├─ Busingen
   │        │     │  ├─ Chisinau
   │        │     │  ├─ Copenhagen
   │        │     │  ├─ Dublin
   │        │     │  ├─ Gibraltar
   │        │     │  ├─ Guernsey
   │        │     │  ├─ Helsinki
   │        │     │  ├─ Isle_of_Man
   │        │     │  ├─ Istanbul
   │        │     │  ├─ Jersey
   │        │     │  ├─ Kaliningrad
   │        │     │  ├─ Kiev
   │        │     │  ├─ Kirov
   │        │     │  ├─ Kyiv
   │        │     │  ├─ Lisbon
   │        │     │  ├─ Ljubljana
   │        │     │  ├─ London
   │        │     │  ├─ Luxembourg
   │        │     │  ├─ Madrid
   │        │     │  ├─ Malta
   │        │     │  ├─ Mariehamn
   │        │     │  ├─ Minsk
   │        │     │  ├─ Monaco
   │        │     │  ├─ Moscow
   │        │     │  ├─ Nicosia
   │        │     │  ├─ Oslo
   │        │     │  ├─ Paris
   │        │     │  ├─ Podgorica
   │        │     │  ├─ Prague
   │        │     │  ├─ Riga
   │        │     │  ├─ Rome
   │        │     │  ├─ Samara
   │        │     │  ├─ San_Marino
   │        │     │  ├─ Sarajevo
   │        │     │  ├─ Saratov
   │        │     │  ├─ Simferopol
   │        │     │  ├─ Skopje
   │        │     │  ├─ Sofia
   │        │     │  ├─ Stockholm
   │        │     │  ├─ Tallinn
   │        │     │  ├─ Tirane
   │        │     │  ├─ Tiraspol
   │        │     │  ├─ Ulyanovsk
   │        │     │  ├─ Uzhgorod
   │        │     │  ├─ Vaduz
   │        │     │  ├─ Vatican
   │        │     │  ├─ Vienna
   │        │     │  ├─ Vilnius
   │        │     │  ├─ Volgograd
   │        │     │  ├─ Warsaw
   │        │     │  ├─ Zagreb
   │        │     │  ├─ Zaporozhye
   │        │     │  └─ Zurich
   │        │     ├─ Factory
   │        │     ├─ GB
   │        │     ├─ GB-Eire
   │        │     ├─ GMT
   │        │     ├─ GMT+0
   │        │     ├─ GMT-0
   │        │     ├─ GMT0
   │        │     ├─ Greenwich
   │        │     ├─ HST
   │        │     ├─ Hongkong
   │        │     ├─ Iceland
   │        │     ├─ Indian
   │        │     │  ├─ Antananarivo
   │        │     │  ├─ Chagos
   │        │     │  ├─ Christmas
   │        │     │  ├─ Cocos
   │        │     │  ├─ Comoro
   │        │     │  ├─ Kerguelen
   │        │     │  ├─ Mahe
   │        │     │  ├─ Maldives
   │        │     │  ├─ Mauritius
   │        │     │  ├─ Mayotte
   │        │     │  └─ Reunion
   │        │     ├─ Iran
   │        │     ├─ Israel
   │        │     ├─ Jamaica
   │        │     ├─ Japan
   │        │     ├─ Kwajalein
   │        │     ├─ Libya
   │        │     ├─ MET
   │        │     ├─ MST
   │        │     ├─ MST7MDT
   │        │     ├─ Mexico
   │        │     │  ├─ BajaNorte
   │        │     │  ├─ BajaSur
   │        │     │  └─ General
   │        │     ├─ NZ
   │        │     ├─ NZ-CHAT
   │        │     ├─ Navajo
   │        │     ├─ PRC
   │        │     ├─ PST8PDT
   │        │     ├─ Pacific
   │        │     │  ├─ Apia
   │        │     │  ├─ Auckland
   │        │     │  ├─ Bougainville
   │        │     │  ├─ Chatham
   │        │     │  ├─ Chuuk
   │        │     │  ├─ Easter
   │        │     │  ├─ Efate
   │        │     │  ├─ Enderbury
   │        │     │  ├─ Fakaofo
   │        │     │  ├─ Fiji
   │        │     │  ├─ Funafuti
   │        │     │  ├─ Galapagos
   │        │     │  ├─ Gambier
   │        │     │  ├─ Guadalcanal
   │        │     │  ├─ Guam
   │        │     │  ├─ Honolulu
   │        │     │  ├─ Johnston
   │        │     │  ├─ Kanton
   │        │     │  ├─ Kiritimati
   │        │     │  ├─ Kosrae
   │        │     │  ├─ Kwajalein
   │        │     │  ├─ Majuro
   │        │     │  ├─ Marquesas
   │        │     │  ├─ Midway
   │        │     │  ├─ Nauru
   │        │     │  ├─ Niue
   │        │     │  ├─ Norfolk
   │        │     │  ├─ Noumea
   │        │     │  ├─ Pago_Pago
   │        │     │  ├─ Palau
   │        │     │  ├─ Pitcairn
   │        │     │  ├─ Pohnpei
   │        │     │  ├─ Ponape
   │        │     │  ├─ Port_Moresby
   │        │     │  ├─ Rarotonga
   │        │     │  ├─ Saipan
   │        │     │  ├─ Samoa
   │        │     │  ├─ Tahiti
   │        │     │  ├─ Tarawa
   │        │     │  ├─ Tongatapu
   │        │     │  ├─ Truk
   │        │     │  ├─ Wake
   │        │     │  ├─ Wallis
   │        │     │  └─ Yap
   │        │     ├─ Poland
   │        │     ├─ Portugal
   │        │     ├─ ROC
   │        │     ├─ ROK
   │        │     ├─ Singapore
   │        │     ├─ Turkey
   │        │     ├─ UCT
   │        │     ├─ US
   │        │     │  ├─ Alaska
   │        │     │  ├─ Aleutian
   │        │     │  ├─ Arizona
   │        │     │  ├─ Central
   │        │     │  ├─ East-Indiana
   │        │     │  ├─ Eastern
   │        │     │  ├─ Hawaii
   │        │     │  ├─ Indiana-Starke
   │        │     │  ├─ Michigan
   │        │     │  ├─ Mountain
   │        │     │  ├─ Pacific
   │        │     │  └─ Samoa
   │        │     ├─ UTC
   │        │     ├─ Universal
   │        │     ├─ W-SU
   │        │     ├─ WET
   │        │     ├─ Zulu
   │        │     ├─ iso3166.tab
   │        │     ├─ leapseconds
   │        │     ├─ tzdata.zi
   │        │     ├─ zone.tab
   │        │     ├─ zone1970.tab
   │        │     └─ zonenow.tab
   │        ├─ pytz-2025.2.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ LICENSE.txt
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  ├─ top_level.txt
   │        │  └─ zip-safe
   │        ├─ referencing
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ _attrs.cpython-311.pyc
   │        │  │  ├─ _core.cpython-311.pyc
   │        │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  ├─ jsonschema.cpython-311.pyc
   │        │  │  ├─ retrieval.cpython-311.pyc
   │        │  │  └─ typing.cpython-311.pyc
   │        │  ├─ _attrs.py
   │        │  ├─ _attrs.pyi
   │        │  ├─ _core.py
   │        │  ├─ exceptions.py
   │        │  ├─ jsonschema.py
   │        │  ├─ py.typed
   │        │  ├─ retrieval.py
   │        │  ├─ tests
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ test_core.cpython-311.pyc
   │        │  │  │  ├─ test_exceptions.cpython-311.pyc
   │        │  │  │  ├─ test_jsonschema.cpython-311.pyc
   │        │  │  │  ├─ test_referencing_suite.cpython-311.pyc
   │        │  │  │  └─ test_retrieval.cpython-311.pyc
   │        │  │  ├─ test_core.py
   │        │  │  ├─ test_exceptions.py
   │        │  │  ├─ test_jsonschema.py
   │        │  │  ├─ test_referencing_suite.py
   │        │  │  └─ test_retrieval.py
   │        │  └─ typing.py
   │        ├─ referencing-0.36.2.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  └─ licenses
   │        │     └─ COPYING
   │        ├─ requests
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ __version__.cpython-311.pyc
   │        │  │  ├─ _internal_utils.cpython-311.pyc
   │        │  │  ├─ adapters.cpython-311.pyc
   │        │  │  ├─ api.cpython-311.pyc
   │        │  │  ├─ auth.cpython-311.pyc
   │        │  │  ├─ certs.cpython-311.pyc
   │        │  │  ├─ compat.cpython-311.pyc
   │        │  │  ├─ cookies.cpython-311.pyc
   │        │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  ├─ help.cpython-311.pyc
   │        │  │  ├─ hooks.cpython-311.pyc
   │        │  │  ├─ models.cpython-311.pyc
   │        │  │  ├─ packages.cpython-311.pyc
   │        │  │  ├─ sessions.cpython-311.pyc
   │        │  │  ├─ status_codes.cpython-311.pyc
   │        │  │  ├─ structures.cpython-311.pyc
   │        │  │  └─ utils.cpython-311.pyc
   │        │  ├─ __version__.py
   │        │  ├─ _internal_utils.py
   │        │  ├─ adapters.py
   │        │  ├─ api.py
   │        │  ├─ auth.py
   │        │  ├─ certs.py
   │        │  ├─ compat.py
   │        │  ├─ cookies.py
   │        │  ├─ exceptions.py
   │        │  ├─ help.py
   │        │  ├─ hooks.py
   │        │  ├─ models.py
   │        │  ├─ packages.py
   │        │  ├─ sessions.py
   │        │  ├─ status_codes.py
   │        │  ├─ structures.py
   │        │  └─ utils.py
   │        ├─ requests-2.32.3.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ LICENSE
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  └─ top_level.txt
   │        ├─ rest_framework
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ apps.cpython-311.pyc
   │        │  │  ├─ authentication.cpython-311.pyc
   │        │  │  ├─ checks.cpython-311.pyc
   │        │  │  ├─ compat.cpython-311.pyc
   │        │  │  ├─ decorators.cpython-311.pyc
   │        │  │  ├─ documentation.cpython-311.pyc
   │        │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  ├─ fields.cpython-311.pyc
   │        │  │  ├─ filters.cpython-311.pyc
   │        │  │  ├─ generics.cpython-311.pyc
   │        │  │  ├─ metadata.cpython-311.pyc
   │        │  │  ├─ mixins.cpython-311.pyc
   │        │  │  ├─ negotiation.cpython-311.pyc
   │        │  │  ├─ pagination.cpython-311.pyc
   │        │  │  ├─ parsers.cpython-311.pyc
   │        │  │  ├─ permissions.cpython-311.pyc
   │        │  │  ├─ relations.cpython-311.pyc
   │        │  │  ├─ renderers.cpython-311.pyc
   │        │  │  ├─ request.cpython-311.pyc
   │        │  │  ├─ response.cpython-311.pyc
   │        │  │  ├─ reverse.cpython-311.pyc
   │        │  │  ├─ routers.cpython-311.pyc
   │        │  │  ├─ serializers.cpython-311.pyc
   │        │  │  ├─ settings.cpython-311.pyc
   │        │  │  ├─ status.cpython-311.pyc
   │        │  │  ├─ test.cpython-311.pyc
   │        │  │  ├─ throttling.cpython-311.pyc
   │        │  │  ├─ urlpatterns.cpython-311.pyc
   │        │  │  ├─ urls.cpython-311.pyc
   │        │  │  ├─ validators.cpython-311.pyc
   │        │  │  ├─ versioning.cpython-311.pyc
   │        │  │  ├─ views.cpython-311.pyc
   │        │  │  └─ viewsets.cpython-311.pyc
   │        │  ├─ apps.py
   │        │  ├─ authentication.py
   │        │  ├─ authtoken
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ admin.cpython-311.pyc
   │        │  │  │  ├─ apps.cpython-311.pyc
   │        │  │  │  ├─ models.cpython-311.pyc
   │        │  │  │  ├─ serializers.cpython-311.pyc
   │        │  │  │  └─ views.cpython-311.pyc
   │        │  │  ├─ admin.py
   │        │  │  ├─ apps.py
   │        │  │  ├─ management
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  │  └─ commands
   │        │  │  │     ├─ __init__.py
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │     │  └─ drf_create_token.cpython-311.pyc
   │        │  │  │     └─ drf_create_token.py
   │        │  │  ├─ migrations
   │        │  │  │  ├─ 0001_initial.py
   │        │  │  │  ├─ 0002_auto_20160226_1747.py
   │        │  │  │  ├─ 0003_tokenproxy.py
   │        │  │  │  ├─ 0004_alter_tokenproxy_options.py
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     ├─ 0001_initial.cpython-311.pyc
   │        │  │  │     ├─ 0002_auto_20160226_1747.cpython-311.pyc
   │        │  │  │     ├─ 0003_tokenproxy.cpython-311.pyc
   │        │  │  │     ├─ 0004_alter_tokenproxy_options.cpython-311.pyc
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ models.py
   │        │  │  ├─ serializers.py
   │        │  │  └─ views.py
   │        │  ├─ checks.py
   │        │  ├─ compat.py
   │        │  ├─ decorators.py
   │        │  ├─ documentation.py
   │        │  ├─ exceptions.py
   │        │  ├─ fields.py
   │        │  ├─ filters.py
   │        │  ├─ generics.py
   │        │  ├─ locale
   │        │  │  ├─ ach
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ ar
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ az
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ be
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ bg
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ ca
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ ca_ES
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ cs
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ da
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ de
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ el
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ el_GR
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ en
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ en_AU
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ en_CA
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ en_US
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ es
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ et
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ fa
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ fa_IR
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ fi
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ fr
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ fr_CA
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ gl
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ gl_ES
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ he_IL
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ hu
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ hy
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ id
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ it
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ ja
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ ko_KR
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ lt
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ lv
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ mk
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ nb
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ ne_NP
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ nl
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ nn
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ no
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ pl
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ pt
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ pt_BR
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ pt_PT
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ ro
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ ru
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ ru_RU
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ sk
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ sl
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ sv
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ th
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ tr
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ tr_TR
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ uk
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ vi
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ zh_CN
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ zh_Hans
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  ├─ zh_Hant
   │        │  │  │  └─ LC_MESSAGES
   │        │  │  │     └─ django.mo
   │        │  │  └─ zh_TW
   │        │  │     └─ LC_MESSAGES
   │        │  │        └─ django.mo
   │        │  ├─ management
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  └─ commands
   │        │  │     ├─ __init__.py
   │        │  │     ├─ __pycache__
   │        │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │     │  └─ generateschema.cpython-311.pyc
   │        │  │     └─ generateschema.py
   │        │  ├─ metadata.py
   │        │  ├─ mixins.py
   │        │  ├─ negotiation.py
   │        │  ├─ pagination.py
   │        │  ├─ parsers.py
   │        │  ├─ permissions.py
   │        │  ├─ relations.py
   │        │  ├─ renderers.py
   │        │  ├─ request.py
   │        │  ├─ response.py
   │        │  ├─ reverse.py
   │        │  ├─ routers.py
   │        │  ├─ schemas
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ coreapi.cpython-311.pyc
   │        │  │  │  ├─ generators.cpython-311.pyc
   │        │  │  │  ├─ inspectors.cpython-311.pyc
   │        │  │  │  ├─ openapi.cpython-311.pyc
   │        │  │  │  ├─ utils.cpython-311.pyc
   │        │  │  │  └─ views.cpython-311.pyc
   │        │  │  ├─ coreapi.py
   │        │  │  ├─ generators.py
   │        │  │  ├─ inspectors.py
   │        │  │  ├─ openapi.py
   │        │  │  ├─ utils.py
   │        │  │  └─ views.py
   │        │  ├─ serializers.py
   │        │  ├─ settings.py
   │        │  ├─ static
   │        │  │  └─ rest_framework
   │        │  │     ├─ css
   │        │  │     │  ├─ bootstrap-theme.min.css
   │        │  │     │  ├─ bootstrap-theme.min.css.map
   │        │  │     │  ├─ bootstrap-tweaks.css
   │        │  │     │  ├─ bootstrap.min.css
   │        │  │     │  ├─ bootstrap.min.css.map
   │        │  │     │  ├─ default.css
   │        │  │     │  ├─ font-awesome-4.0.3.css
   │        │  │     │  └─ prettify.css
   │        │  │     ├─ docs
   │        │  │     │  ├─ css
   │        │  │     │  │  ├─ base.css
   │        │  │     │  │  ├─ highlight.css
   │        │  │     │  │  └─ jquery.json-view.min.css
   │        │  │     │  ├─ img
   │        │  │     │  │  ├─ favicon.ico
   │        │  │     │  │  └─ grid.png
   │        │  │     │  └─ js
   │        │  │     │     ├─ api.js
   │        │  │     │     ├─ highlight.pack.js
   │        │  │     │     └─ jquery.json-view.min.js
   │        │  │     ├─ fonts
   │        │  │     │  ├─ fontawesome-webfont.eot
   │        │  │     │  ├─ fontawesome-webfont.svg
   │        │  │     │  ├─ fontawesome-webfont.ttf
   │        │  │     │  ├─ fontawesome-webfont.woff
   │        │  │     │  ├─ glyphicons-halflings-regular.eot
   │        │  │     │  ├─ glyphicons-halflings-regular.svg
   │        │  │     │  ├─ glyphicons-halflings-regular.ttf
   │        │  │     │  ├─ glyphicons-halflings-regular.woff
   │        │  │     │  └─ glyphicons-halflings-regular.woff2
   │        │  │     ├─ img
   │        │  │     │  ├─ glyphicons-halflings-white.png
   │        │  │     │  ├─ glyphicons-halflings.png
   │        │  │     │  └─ grid.png
   │        │  │     └─ js
   │        │  │        ├─ ajax-form.js
   │        │  │        ├─ bootstrap.min.js
   │        │  │        ├─ coreapi-0.1.1.js
   │        │  │        ├─ csrf.js
   │        │  │        ├─ default.js
   │        │  │        ├─ jquery-3.7.1.min.js
   │        │  │        ├─ load-ajax-form.js
   │        │  │        └─ prettify-min.js
   │        │  ├─ status.py
   │        │  ├─ templates
   │        │  │  └─ rest_framework
   │        │  │     ├─ admin
   │        │  │     │  ├─ detail.html
   │        │  │     │  ├─ dict_value.html
   │        │  │     │  ├─ list.html
   │        │  │     │  ├─ list_value.html
   │        │  │     │  └─ simple_list_value.html
   │        │  │     ├─ admin.html
   │        │  │     ├─ api.html
   │        │  │     ├─ base.html
   │        │  │     ├─ docs
   │        │  │     │  ├─ auth
   │        │  │     │  │  ├─ basic.html
   │        │  │     │  │  ├─ session.html
   │        │  │     │  │  └─ token.html
   │        │  │     │  ├─ document.html
   │        │  │     │  ├─ error.html
   │        │  │     │  ├─ index.html
   │        │  │     │  ├─ interact.html
   │        │  │     │  ├─ langs
   │        │  │     │  │  ├─ javascript-intro.html
   │        │  │     │  │  ├─ javascript.html
   │        │  │     │  │  ├─ python-intro.html
   │        │  │     │  │  ├─ python.html
   │        │  │     │  │  ├─ shell-intro.html
   │        │  │     │  │  └─ shell.html
   │        │  │     │  ├─ link.html
   │        │  │     │  └─ sidebar.html
   │        │  │     ├─ filters
   │        │  │     │  ├─ base.html
   │        │  │     │  ├─ ordering.html
   │        │  │     │  └─ search.html
   │        │  │     ├─ horizontal
   │        │  │     │  ├─ checkbox.html
   │        │  │     │  ├─ checkbox_multiple.html
   │        │  │     │  ├─ dict_field.html
   │        │  │     │  ├─ fieldset.html
   │        │  │     │  ├─ form.html
   │        │  │     │  ├─ input.html
   │        │  │     │  ├─ list_field.html
   │        │  │     │  ├─ list_fieldset.html
   │        │  │     │  ├─ radio.html
   │        │  │     │  ├─ select.html
   │        │  │     │  ├─ select_multiple.html
   │        │  │     │  └─ textarea.html
   │        │  │     ├─ inline
   │        │  │     │  ├─ checkbox.html
   │        │  │     │  ├─ checkbox_multiple.html
   │        │  │     │  ├─ dict_field.html
   │        │  │     │  ├─ fieldset.html
   │        │  │     │  ├─ form.html
   │        │  │     │  ├─ input.html
   │        │  │     │  ├─ list_field.html
   │        │  │     │  ├─ list_fieldset.html
   │        │  │     │  ├─ radio.html
   │        │  │     │  ├─ select.html
   │        │  │     │  ├─ select_multiple.html
   │        │  │     │  └─ textarea.html
   │        │  │     ├─ login.html
   │        │  │     ├─ login_base.html
   │        │  │     ├─ pagination
   │        │  │     │  ├─ numbers.html
   │        │  │     │  └─ previous_and_next.html
   │        │  │     ├─ raw_data_form.html
   │        │  │     ├─ schema.js
   │        │  │     └─ vertical
   │        │  │        ├─ checkbox.html
   │        │  │        ├─ checkbox_multiple.html
   │        │  │        ├─ dict_field.html
   │        │  │        ├─ fieldset.html
   │        │  │        ├─ form.html
   │        │  │        ├─ input.html
   │        │  │        ├─ list_field.html
   │        │  │        ├─ list_fieldset.html
   │        │  │        ├─ radio.html
   │        │  │        ├─ select.html
   │        │  │        ├─ select_multiple.html
   │        │  │        └─ textarea.html
   │        │  ├─ templatetags
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  └─ rest_framework.cpython-311.pyc
   │        │  │  └─ rest_framework.py
   │        │  ├─ test.py
   │        │  ├─ throttling.py
   │        │  ├─ urlpatterns.py
   │        │  ├─ urls.py
   │        │  ├─ utils
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ breadcrumbs.cpython-311.pyc
   │        │  │  │  ├─ encoders.cpython-311.pyc
   │        │  │  │  ├─ field_mapping.cpython-311.pyc
   │        │  │  │  ├─ formatting.cpython-311.pyc
   │        │  │  │  ├─ html.cpython-311.pyc
   │        │  │  │  ├─ humanize_datetime.cpython-311.pyc
   │        │  │  │  ├─ json.cpython-311.pyc
   │        │  │  │  ├─ mediatypes.cpython-311.pyc
   │        │  │  │  ├─ model_meta.cpython-311.pyc
   │        │  │  │  ├─ representation.cpython-311.pyc
   │        │  │  │  ├─ serializer_helpers.cpython-311.pyc
   │        │  │  │  ├─ timezone.cpython-311.pyc
   │        │  │  │  └─ urls.cpython-311.pyc
   │        │  │  ├─ breadcrumbs.py
   │        │  │  ├─ encoders.py
   │        │  │  ├─ field_mapping.py
   │        │  │  ├─ formatting.py
   │        │  │  ├─ html.py
   │        │  │  ├─ humanize_datetime.py
   │        │  │  ├─ json.py
   │        │  │  ├─ mediatypes.py
   │        │  │  ├─ model_meta.py
   │        │  │  ├─ representation.py
   │        │  │  ├─ serializer_helpers.py
   │        │  │  ├─ timezone.py
   │        │  │  └─ urls.py
   │        │  ├─ validators.py
   │        │  ├─ versioning.py
   │        │  ├─ views.py
   │        │  └─ viewsets.py
   │        ├─ rpds
   │        │  ├─ __init__.py
   │        │  ├─ __init__.pyi
   │        │  ├─ __pycache__
   │        │  │  └─ __init__.cpython-311.pyc
   │        │  ├─ py.typed
   │        │  └─ rpds.cpython-311-darwin.so
   │        ├─ rpds_py-0.25.1.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  └─ licenses
   │        │     └─ LICENSE
   │        ├─ setuptools
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ _core_metadata.cpython-311.pyc
   │        │  │  ├─ _entry_points.cpython-311.pyc
   │        │  │  ├─ _imp.cpython-311.pyc
   │        │  │  ├─ _importlib.cpython-311.pyc
   │        │  │  ├─ _itertools.cpython-311.pyc
   │        │  │  ├─ _normalization.cpython-311.pyc
   │        │  │  ├─ _path.cpython-311.pyc
   │        │  │  ├─ _reqs.cpython-311.pyc
   │        │  │  ├─ _scripts.cpython-311.pyc
   │        │  │  ├─ _shutil.cpython-311.pyc
   │        │  │  ├─ _static.cpython-311.pyc
   │        │  │  ├─ archive_util.cpython-311.pyc
   │        │  │  ├─ build_meta.cpython-311.pyc
   │        │  │  ├─ depends.cpython-311.pyc
   │        │  │  ├─ discovery.cpython-311.pyc
   │        │  │  ├─ dist.cpython-311.pyc
   │        │  │  ├─ errors.cpython-311.pyc
   │        │  │  ├─ extension.cpython-311.pyc
   │        │  │  ├─ glob.cpython-311.pyc
   │        │  │  ├─ installer.cpython-311.pyc
   │        │  │  ├─ launch.cpython-311.pyc
   │        │  │  ├─ logging.cpython-311.pyc
   │        │  │  ├─ modified.cpython-311.pyc
   │        │  │  ├─ monkey.cpython-311.pyc
   │        │  │  ├─ msvc.cpython-311.pyc
   │        │  │  ├─ namespaces.cpython-311.pyc
   │        │  │  ├─ unicode_utils.cpython-311.pyc
   │        │  │  ├─ version.cpython-311.pyc
   │        │  │  ├─ warnings.cpython-311.pyc
   │        │  │  ├─ wheel.cpython-311.pyc
   │        │  │  └─ windows_support.cpython-311.pyc
   │        │  ├─ _core_metadata.py
   │        │  ├─ _distutils
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _log.cpython-311.pyc
   │        │  │  │  ├─ _macos_compat.cpython-311.pyc
   │        │  │  │  ├─ _modified.cpython-311.pyc
   │        │  │  │  ├─ _msvccompiler.cpython-311.pyc
   │        │  │  │  ├─ archive_util.cpython-311.pyc
   │        │  │  │  ├─ ccompiler.cpython-311.pyc
   │        │  │  │  ├─ cmd.cpython-311.pyc
   │        │  │  │  ├─ core.cpython-311.pyc
   │        │  │  │  ├─ cygwinccompiler.cpython-311.pyc
   │        │  │  │  ├─ debug.cpython-311.pyc
   │        │  │  │  ├─ dep_util.cpython-311.pyc
   │        │  │  │  ├─ dir_util.cpython-311.pyc
   │        │  │  │  ├─ dist.cpython-311.pyc
   │        │  │  │  ├─ errors.cpython-311.pyc
   │        │  │  │  ├─ extension.cpython-311.pyc
   │        │  │  │  ├─ fancy_getopt.cpython-311.pyc
   │        │  │  │  ├─ file_util.cpython-311.pyc
   │        │  │  │  ├─ filelist.cpython-311.pyc
   │        │  │  │  ├─ log.cpython-311.pyc
   │        │  │  │  ├─ spawn.cpython-311.pyc
   │        │  │  │  ├─ sysconfig.cpython-311.pyc
   │        │  │  │  ├─ text_file.cpython-311.pyc
   │        │  │  │  ├─ unixccompiler.cpython-311.pyc
   │        │  │  │  ├─ util.cpython-311.pyc
   │        │  │  │  ├─ version.cpython-311.pyc
   │        │  │  │  ├─ versionpredicate.cpython-311.pyc
   │        │  │  │  └─ zosccompiler.cpython-311.pyc
   │        │  │  ├─ _log.py
   │        │  │  ├─ _macos_compat.py
   │        │  │  ├─ _modified.py
   │        │  │  ├─ _msvccompiler.py
   │        │  │  ├─ archive_util.py
   │        │  │  ├─ ccompiler.py
   │        │  │  ├─ cmd.py
   │        │  │  ├─ command
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ _framework_compat.cpython-311.pyc
   │        │  │  │  │  ├─ bdist.cpython-311.pyc
   │        │  │  │  │  ├─ bdist_dumb.cpython-311.pyc
   │        │  │  │  │  ├─ bdist_rpm.cpython-311.pyc
   │        │  │  │  │  ├─ build.cpython-311.pyc
   │        │  │  │  │  ├─ build_clib.cpython-311.pyc
   │        │  │  │  │  ├─ build_ext.cpython-311.pyc
   │        │  │  │  │  ├─ build_py.cpython-311.pyc
   │        │  │  │  │  ├─ build_scripts.cpython-311.pyc
   │        │  │  │  │  ├─ check.cpython-311.pyc
   │        │  │  │  │  ├─ clean.cpython-311.pyc
   │        │  │  │  │  ├─ config.cpython-311.pyc
   │        │  │  │  │  ├─ install.cpython-311.pyc
   │        │  │  │  │  ├─ install_data.cpython-311.pyc
   │        │  │  │  │  ├─ install_egg_info.cpython-311.pyc
   │        │  │  │  │  ├─ install_headers.cpython-311.pyc
   │        │  │  │  │  ├─ install_lib.cpython-311.pyc
   │        │  │  │  │  ├─ install_scripts.cpython-311.pyc
   │        │  │  │  │  └─ sdist.cpython-311.pyc
   │        │  │  │  ├─ _framework_compat.py
   │        │  │  │  ├─ bdist.py
   │        │  │  │  ├─ bdist_dumb.py
   │        │  │  │  ├─ bdist_rpm.py
   │        │  │  │  ├─ build.py
   │        │  │  │  ├─ build_clib.py
   │        │  │  │  ├─ build_ext.py
   │        │  │  │  ├─ build_py.py
   │        │  │  │  ├─ build_scripts.py
   │        │  │  │  ├─ check.py
   │        │  │  │  ├─ clean.py
   │        │  │  │  ├─ config.py
   │        │  │  │  ├─ install.py
   │        │  │  │  ├─ install_data.py
   │        │  │  │  ├─ install_egg_info.py
   │        │  │  │  ├─ install_headers.py
   │        │  │  │  ├─ install_lib.py
   │        │  │  │  ├─ install_scripts.py
   │        │  │  │  └─ sdist.py
   │        │  │  ├─ compat
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ numpy.cpython-311.pyc
   │        │  │  │  │  └─ py39.cpython-311.pyc
   │        │  │  │  ├─ numpy.py
   │        │  │  │  └─ py39.py
   │        │  │  ├─ compilers
   │        │  │  │  └─ C
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ base.cpython-311.pyc
   │        │  │  │     │  ├─ cygwin.cpython-311.pyc
   │        │  │  │     │  ├─ errors.cpython-311.pyc
   │        │  │  │     │  ├─ msvc.cpython-311.pyc
   │        │  │  │     │  ├─ unix.cpython-311.pyc
   │        │  │  │     │  └─ zos.cpython-311.pyc
   │        │  │  │     ├─ base.py
   │        │  │  │     ├─ cygwin.py
   │        │  │  │     ├─ errors.py
   │        │  │  │     ├─ msvc.py
   │        │  │  │     ├─ tests
   │        │  │  │     │  ├─ __pycache__
   │        │  │  │     │  │  ├─ test_base.cpython-311.pyc
   │        │  │  │     │  │  ├─ test_cygwin.cpython-311.pyc
   │        │  │  │     │  │  ├─ test_mingw.cpython-311.pyc
   │        │  │  │     │  │  ├─ test_msvc.cpython-311.pyc
   │        │  │  │     │  │  └─ test_unix.cpython-311.pyc
   │        │  │  │     │  ├─ test_base.py
   │        │  │  │     │  ├─ test_cygwin.py
   │        │  │  │     │  ├─ test_mingw.py
   │        │  │  │     │  ├─ test_msvc.py
   │        │  │  │     │  └─ test_unix.py
   │        │  │  │     ├─ unix.py
   │        │  │  │     └─ zos.py
   │        │  │  ├─ core.py
   │        │  │  ├─ cygwinccompiler.py
   │        │  │  ├─ debug.py
   │        │  │  ├─ dep_util.py
   │        │  │  ├─ dir_util.py
   │        │  │  ├─ dist.py
   │        │  │  ├─ errors.py
   │        │  │  ├─ extension.py
   │        │  │  ├─ fancy_getopt.py
   │        │  │  ├─ file_util.py
   │        │  │  ├─ filelist.py
   │        │  │  ├─ log.py
   │        │  │  ├─ spawn.py
   │        │  │  ├─ sysconfig.py
   │        │  │  ├─ tests
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ support.cpython-311.pyc
   │        │  │  │  │  ├─ test_archive_util.cpython-311.pyc
   │        │  │  │  │  ├─ test_bdist.cpython-311.pyc
   │        │  │  │  │  ├─ test_bdist_dumb.cpython-311.pyc
   │        │  │  │  │  ├─ test_bdist_rpm.cpython-311.pyc
   │        │  │  │  │  ├─ test_build.cpython-311.pyc
   │        │  │  │  │  ├─ test_build_clib.cpython-311.pyc
   │        │  │  │  │  ├─ test_build_ext.cpython-311.pyc
   │        │  │  │  │  ├─ test_build_py.cpython-311.pyc
   │        │  │  │  │  ├─ test_build_scripts.cpython-311.pyc
   │        │  │  │  │  ├─ test_check.cpython-311.pyc
   │        │  │  │  │  ├─ test_clean.cpython-311.pyc
   │        │  │  │  │  ├─ test_cmd.cpython-311.pyc
   │        │  │  │  │  ├─ test_config_cmd.cpython-311.pyc
   │        │  │  │  │  ├─ test_core.cpython-311.pyc
   │        │  │  │  │  ├─ test_dir_util.cpython-311.pyc
   │        │  │  │  │  ├─ test_dist.cpython-311.pyc
   │        │  │  │  │  ├─ test_extension.cpython-311.pyc
   │        │  │  │  │  ├─ test_file_util.cpython-311.pyc
   │        │  │  │  │  ├─ test_filelist.cpython-311.pyc
   │        │  │  │  │  ├─ test_install.cpython-311.pyc
   │        │  │  │  │  ├─ test_install_data.cpython-311.pyc
   │        │  │  │  │  ├─ test_install_headers.cpython-311.pyc
   │        │  │  │  │  ├─ test_install_lib.cpython-311.pyc
   │        │  │  │  │  ├─ test_install_scripts.cpython-311.pyc
   │        │  │  │  │  ├─ test_log.cpython-311.pyc
   │        │  │  │  │  ├─ test_modified.cpython-311.pyc
   │        │  │  │  │  ├─ test_sdist.cpython-311.pyc
   │        │  │  │  │  ├─ test_spawn.cpython-311.pyc
   │        │  │  │  │  ├─ test_sysconfig.cpython-311.pyc
   │        │  │  │  │  ├─ test_text_file.cpython-311.pyc
   │        │  │  │  │  ├─ test_util.cpython-311.pyc
   │        │  │  │  │  ├─ test_version.cpython-311.pyc
   │        │  │  │  │  ├─ test_versionpredicate.cpython-311.pyc
   │        │  │  │  │  └─ unix_compat.cpython-311.pyc
   │        │  │  │  ├─ compat
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ py39.cpython-311.pyc
   │        │  │  │  │  └─ py39.py
   │        │  │  │  ├─ support.py
   │        │  │  │  ├─ test_archive_util.py
   │        │  │  │  ├─ test_bdist.py
   │        │  │  │  ├─ test_bdist_dumb.py
   │        │  │  │  ├─ test_bdist_rpm.py
   │        │  │  │  ├─ test_build.py
   │        │  │  │  ├─ test_build_clib.py
   │        │  │  │  ├─ test_build_ext.py
   │        │  │  │  ├─ test_build_py.py
   │        │  │  │  ├─ test_build_scripts.py
   │        │  │  │  ├─ test_check.py
   │        │  │  │  ├─ test_clean.py
   │        │  │  │  ├─ test_cmd.py
   │        │  │  │  ├─ test_config_cmd.py
   │        │  │  │  ├─ test_core.py
   │        │  │  │  ├─ test_dir_util.py
   │        │  │  │  ├─ test_dist.py
   │        │  │  │  ├─ test_extension.py
   │        │  │  │  ├─ test_file_util.py
   │        │  │  │  ├─ test_filelist.py
   │        │  │  │  ├─ test_install.py
   │        │  │  │  ├─ test_install_data.py
   │        │  │  │  ├─ test_install_headers.py
   │        │  │  │  ├─ test_install_lib.py
   │        │  │  │  ├─ test_install_scripts.py
   │        │  │  │  ├─ test_log.py
   │        │  │  │  ├─ test_modified.py
   │        │  │  │  ├─ test_sdist.py
   │        │  │  │  ├─ test_spawn.py
   │        │  │  │  ├─ test_sysconfig.py
   │        │  │  │  ├─ test_text_file.py
   │        │  │  │  ├─ test_util.py
   │        │  │  │  ├─ test_version.py
   │        │  │  │  ├─ test_versionpredicate.py
   │        │  │  │  └─ unix_compat.py
   │        │  │  ├─ text_file.py
   │        │  │  ├─ unixccompiler.py
   │        │  │  ├─ util.py
   │        │  │  ├─ version.py
   │        │  │  ├─ versionpredicate.py
   │        │  │  └─ zosccompiler.py
   │        │  ├─ _entry_points.py
   │        │  ├─ _imp.py
   │        │  ├─ _importlib.py
   │        │  ├─ _itertools.py
   │        │  ├─ _normalization.py
   │        │  ├─ _path.py
   │        │  ├─ _reqs.py
   │        │  ├─ _scripts.py
   │        │  ├─ _shutil.py
   │        │  ├─ _static.py
   │        │  ├─ _vendor
   │        │  │  ├─ __pycache__
   │        │  │  │  └─ typing_extensions.cpython-311.pyc
   │        │  │  ├─ autocommand
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ autoasync.cpython-311.pyc
   │        │  │  │  │  ├─ autocommand.cpython-311.pyc
   │        │  │  │  │  ├─ automain.cpython-311.pyc
   │        │  │  │  │  ├─ autoparse.cpython-311.pyc
   │        │  │  │  │  └─ errors.cpython-311.pyc
   │        │  │  │  ├─ autoasync.py
   │        │  │  │  ├─ autocommand.py
   │        │  │  │  ├─ automain.py
   │        │  │  │  ├─ autoparse.py
   │        │  │  │  └─ errors.py
   │        │  │  ├─ autocommand-2.2.2.dist-info
   │        │  │  │  ├─ INSTALLER
   │        │  │  │  ├─ LICENSE
   │        │  │  │  ├─ METADATA
   │        │  │  │  ├─ RECORD
   │        │  │  │  ├─ WHEEL
   │        │  │  │  └─ top_level.txt
   │        │  │  ├─ backports
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  │  └─ tarfile
   │        │  │  │     ├─ __init__.py
   │        │  │  │     ├─ __main__.py
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │     │  └─ __main__.cpython-311.pyc
   │        │  │  │     └─ compat
   │        │  │  │        ├─ __init__.py
   │        │  │  │        ├─ __pycache__
   │        │  │  │        │  ├─ __init__.cpython-311.pyc
   │        │  │  │        │  └─ py38.cpython-311.pyc
   │        │  │  │        └─ py38.py
   │        │  │  ├─ backports.tarfile-1.2.0.dist-info
   │        │  │  │  ├─ INSTALLER
   │        │  │  │  ├─ LICENSE
   │        │  │  │  ├─ METADATA
   │        │  │  │  ├─ RECORD
   │        │  │  │  ├─ REQUESTED
   │        │  │  │  ├─ WHEEL
   │        │  │  │  └─ top_level.txt
   │        │  │  ├─ importlib_metadata
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ _adapters.cpython-311.pyc
   │        │  │  │  │  ├─ _collections.cpython-311.pyc
   │        │  │  │  │  ├─ _compat.cpython-311.pyc
   │        │  │  │  │  ├─ _functools.cpython-311.pyc
   │        │  │  │  │  ├─ _itertools.cpython-311.pyc
   │        │  │  │  │  ├─ _meta.cpython-311.pyc
   │        │  │  │  │  ├─ _text.cpython-311.pyc
   │        │  │  │  │  └─ diagnose.cpython-311.pyc
   │        │  │  │  ├─ _adapters.py
   │        │  │  │  ├─ _collections.py
   │        │  │  │  ├─ _compat.py
   │        │  │  │  ├─ _functools.py
   │        │  │  │  ├─ _itertools.py
   │        │  │  │  ├─ _meta.py
   │        │  │  │  ├─ _text.py
   │        │  │  │  ├─ compat
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ py311.cpython-311.pyc
   │        │  │  │  │  │  └─ py39.cpython-311.pyc
   │        │  │  │  │  ├─ py311.py
   │        │  │  │  │  └─ py39.py
   │        │  │  │  ├─ diagnose.py
   │        │  │  │  └─ py.typed
   │        │  │  ├─ importlib_metadata-8.0.0.dist-info
   │        │  │  │  ├─ INSTALLER
   │        │  │  │  ├─ LICENSE
   │        │  │  │  ├─ METADATA
   │        │  │  │  ├─ RECORD
   │        │  │  │  ├─ REQUESTED
   │        │  │  │  ├─ WHEEL
   │        │  │  │  └─ top_level.txt
   │        │  │  ├─ inflect
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  │  ├─ compat
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ py38.cpython-311.pyc
   │        │  │  │  │  └─ py38.py
   │        │  │  │  └─ py.typed
   │        │  │  ├─ inflect-7.3.1.dist-info
   │        │  │  │  ├─ INSTALLER
   │        │  │  │  ├─ LICENSE
   │        │  │  │  ├─ METADATA
   │        │  │  │  ├─ RECORD
   │        │  │  │  ├─ WHEEL
   │        │  │  │  └─ top_level.txt
   │        │  │  ├─ jaraco
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  └─ context.cpython-311.pyc
   │        │  │  │  ├─ collections
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  │  │  └─ py.typed
   │        │  │  │  ├─ context.py
   │        │  │  │  ├─ functools
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __init__.pyi
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  │  │  └─ py.typed
   │        │  │  │  └─ text
   │        │  │  │     ├─ Lorem ipsum.txt
   │        │  │  │     ├─ __init__.py
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │     │  ├─ layouts.cpython-311.pyc
   │        │  │  │     │  ├─ show-newlines.cpython-311.pyc
   │        │  │  │     │  ├─ strip-prefix.cpython-311.pyc
   │        │  │  │     │  ├─ to-dvorak.cpython-311.pyc
   │        │  │  │     │  └─ to-qwerty.cpython-311.pyc
   │        │  │  │     ├─ layouts.py
   │        │  │  │     ├─ show-newlines.py
   │        │  │  │     ├─ strip-prefix.py
   │        │  │  │     ├─ to-dvorak.py
   │        │  │  │     └─ to-qwerty.py
   │        │  │  ├─ jaraco.collections-5.1.0.dist-info
   │        │  │  │  ├─ INSTALLER
   │        │  │  │  ├─ LICENSE
   │        │  │  │  ├─ METADATA
   │        │  │  │  ├─ RECORD
   │        │  │  │  ├─ REQUESTED
   │        │  │  │  ├─ WHEEL
   │        │  │  │  └─ top_level.txt
   │        │  │  ├─ jaraco.context-5.3.0.dist-info
   │        │  │  │  ├─ INSTALLER
   │        │  │  │  ├─ LICENSE
   │        │  │  │  ├─ METADATA
   │        │  │  │  ├─ RECORD
   │        │  │  │  ├─ WHEEL
   │        │  │  │  └─ top_level.txt
   │        │  │  ├─ jaraco.functools-4.0.1.dist-info
   │        │  │  │  ├─ INSTALLER
   │        │  │  │  ├─ LICENSE
   │        │  │  │  ├─ METADATA
   │        │  │  │  ├─ RECORD
   │        │  │  │  ├─ WHEEL
   │        │  │  │  └─ top_level.txt
   │        │  │  ├─ jaraco.text-3.12.1.dist-info
   │        │  │  │  ├─ INSTALLER
   │        │  │  │  ├─ LICENSE
   │        │  │  │  ├─ METADATA
   │        │  │  │  ├─ RECORD
   │        │  │  │  ├─ REQUESTED
   │        │  │  │  ├─ WHEEL
   │        │  │  │  └─ top_level.txt
   │        │  │  ├─ more_itertools
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.pyi
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ more.cpython-311.pyc
   │        │  │  │  │  └─ recipes.cpython-311.pyc
   │        │  │  │  ├─ more.py
   │        │  │  │  ├─ more.pyi
   │        │  │  │  ├─ py.typed
   │        │  │  │  ├─ recipes.py
   │        │  │  │  └─ recipes.pyi
   │        │  │  ├─ more_itertools-10.3.0.dist-info
   │        │  │  │  ├─ INSTALLER
   │        │  │  │  ├─ LICENSE
   │        │  │  │  ├─ METADATA
   │        │  │  │  ├─ RECORD
   │        │  │  │  ├─ REQUESTED
   │        │  │  │  └─ WHEEL
   │        │  │  ├─ packaging
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ _elffile.cpython-311.pyc
   │        │  │  │  │  ├─ _manylinux.cpython-311.pyc
   │        │  │  │  │  ├─ _musllinux.cpython-311.pyc
   │        │  │  │  │  ├─ _parser.cpython-311.pyc
   │        │  │  │  │  ├─ _structures.cpython-311.pyc
   │        │  │  │  │  ├─ _tokenizer.cpython-311.pyc
   │        │  │  │  │  ├─ markers.cpython-311.pyc
   │        │  │  │  │  ├─ metadata.cpython-311.pyc
   │        │  │  │  │  ├─ requirements.cpython-311.pyc
   │        │  │  │  │  ├─ specifiers.cpython-311.pyc
   │        │  │  │  │  ├─ tags.cpython-311.pyc
   │        │  │  │  │  ├─ utils.cpython-311.pyc
   │        │  │  │  │  └─ version.cpython-311.pyc
   │        │  │  │  ├─ _elffile.py
   │        │  │  │  ├─ _manylinux.py
   │        │  │  │  ├─ _musllinux.py
   │        │  │  │  ├─ _parser.py
   │        │  │  │  ├─ _structures.py
   │        │  │  │  ├─ _tokenizer.py
   │        │  │  │  ├─ licenses
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ _spdx.cpython-311.pyc
   │        │  │  │  │  └─ _spdx.py
   │        │  │  │  ├─ markers.py
   │        │  │  │  ├─ metadata.py
   │        │  │  │  ├─ py.typed
   │        │  │  │  ├─ requirements.py
   │        │  │  │  ├─ specifiers.py
   │        │  │  │  ├─ tags.py
   │        │  │  │  ├─ utils.py
   │        │  │  │  └─ version.py
   │        │  │  ├─ packaging-24.2.dist-info
   │        │  │  │  ├─ INSTALLER
   │        │  │  │  ├─ LICENSE
   │        │  │  │  ├─ LICENSE.APACHE
   │        │  │  │  ├─ LICENSE.BSD
   │        │  │  │  ├─ METADATA
   │        │  │  │  ├─ RECORD
   │        │  │  │  ├─ REQUESTED
   │        │  │  │  └─ WHEEL
   │        │  │  ├─ platformdirs
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __main__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ __main__.cpython-311.pyc
   │        │  │  │  │  ├─ android.cpython-311.pyc
   │        │  │  │  │  ├─ api.cpython-311.pyc
   │        │  │  │  │  ├─ macos.cpython-311.pyc
   │        │  │  │  │  ├─ unix.cpython-311.pyc
   │        │  │  │  │  ├─ version.cpython-311.pyc
   │        │  │  │  │  └─ windows.cpython-311.pyc
   │        │  │  │  ├─ android.py
   │        │  │  │  ├─ api.py
   │        │  │  │  ├─ macos.py
   │        │  │  │  ├─ py.typed
   │        │  │  │  ├─ unix.py
   │        │  │  │  ├─ version.py
   │        │  │  │  └─ windows.py
   │        │  │  ├─ platformdirs-4.2.2.dist-info
   │        │  │  │  ├─ INSTALLER
   │        │  │  │  ├─ METADATA
   │        │  │  │  ├─ RECORD
   │        │  │  │  ├─ REQUESTED
   │        │  │  │  ├─ WHEEL
   │        │  │  │  └─ licenses
   │        │  │  │     └─ LICENSE
   │        │  │  ├─ tomli
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ _parser.cpython-311.pyc
   │        │  │  │  │  ├─ _re.cpython-311.pyc
   │        │  │  │  │  └─ _types.cpython-311.pyc
   │        │  │  │  ├─ _parser.py
   │        │  │  │  ├─ _re.py
   │        │  │  │  ├─ _types.py
   │        │  │  │  └─ py.typed
   │        │  │  ├─ tomli-2.0.1.dist-info
   │        │  │  │  ├─ INSTALLER
   │        │  │  │  ├─ LICENSE
   │        │  │  │  ├─ METADATA
   │        │  │  │  ├─ RECORD
   │        │  │  │  ├─ REQUESTED
   │        │  │  │  └─ WHEEL
   │        │  │  ├─ typeguard
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ _checkers.cpython-311.pyc
   │        │  │  │  │  ├─ _config.cpython-311.pyc
   │        │  │  │  │  ├─ _decorators.cpython-311.pyc
   │        │  │  │  │  ├─ _exceptions.cpython-311.pyc
   │        │  │  │  │  ├─ _functions.cpython-311.pyc
   │        │  │  │  │  ├─ _importhook.cpython-311.pyc
   │        │  │  │  │  ├─ _memo.cpython-311.pyc
   │        │  │  │  │  ├─ _pytest_plugin.cpython-311.pyc
   │        │  │  │  │  ├─ _suppression.cpython-311.pyc
   │        │  │  │  │  ├─ _transformer.cpython-311.pyc
   │        │  │  │  │  ├─ _union_transformer.cpython-311.pyc
   │        │  │  │  │  └─ _utils.cpython-311.pyc
   │        │  │  │  ├─ _checkers.py
   │        │  │  │  ├─ _config.py
   │        │  │  │  ├─ _decorators.py
   │        │  │  │  ├─ _exceptions.py
   │        │  │  │  ├─ _functions.py
   │        │  │  │  ├─ _importhook.py
   │        │  │  │  ├─ _memo.py
   │        │  │  │  ├─ _pytest_plugin.py
   │        │  │  │  ├─ _suppression.py
   │        │  │  │  ├─ _transformer.py
   │        │  │  │  ├─ _union_transformer.py
   │        │  │  │  ├─ _utils.py
   │        │  │  │  └─ py.typed
   │        │  │  ├─ typeguard-4.3.0.dist-info
   │        │  │  │  ├─ INSTALLER
   │        │  │  │  ├─ LICENSE
   │        │  │  │  ├─ METADATA
   │        │  │  │  ├─ RECORD
   │        │  │  │  ├─ WHEEL
   │        │  │  │  ├─ entry_points.txt
   │        │  │  │  └─ top_level.txt
   │        │  │  ├─ typing_extensions-4.12.2.dist-info
   │        │  │  │  ├─ INSTALLER
   │        │  │  │  ├─ LICENSE
   │        │  │  │  ├─ METADATA
   │        │  │  │  ├─ RECORD
   │        │  │  │  └─ WHEEL
   │        │  │  ├─ typing_extensions.py
   │        │  │  ├─ wheel
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __main__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ __main__.cpython-311.pyc
   │        │  │  │  │  ├─ _bdist_wheel.cpython-311.pyc
   │        │  │  │  │  ├─ _setuptools_logging.cpython-311.pyc
   │        │  │  │  │  ├─ bdist_wheel.cpython-311.pyc
   │        │  │  │  │  ├─ macosx_libfile.cpython-311.pyc
   │        │  │  │  │  ├─ metadata.cpython-311.pyc
   │        │  │  │  │  ├─ util.cpython-311.pyc
   │        │  │  │  │  └─ wheelfile.cpython-311.pyc
   │        │  │  │  ├─ _bdist_wheel.py
   │        │  │  │  ├─ _setuptools_logging.py
   │        │  │  │  ├─ bdist_wheel.py
   │        │  │  │  ├─ cli
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  ├─ convert.cpython-311.pyc
   │        │  │  │  │  │  ├─ pack.cpython-311.pyc
   │        │  │  │  │  │  ├─ tags.cpython-311.pyc
   │        │  │  │  │  │  └─ unpack.cpython-311.pyc
   │        │  │  │  │  ├─ convert.py
   │        │  │  │  │  ├─ pack.py
   │        │  │  │  │  ├─ tags.py
   │        │  │  │  │  └─ unpack.py
   │        │  │  │  ├─ macosx_libfile.py
   │        │  │  │  ├─ metadata.py
   │        │  │  │  ├─ util.py
   │        │  │  │  ├─ vendored
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ packaging
   │        │  │  │  │  │  ├─ LICENSE
   │        │  │  │  │  │  ├─ LICENSE.APACHE
   │        │  │  │  │  │  ├─ LICENSE.BSD
   │        │  │  │  │  │  ├─ __init__.py
   │        │  │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ _elffile.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ _manylinux.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ _musllinux.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ _parser.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ _structures.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ _tokenizer.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ markers.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ requirements.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ specifiers.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ tags.cpython-311.pyc
   │        │  │  │  │  │  │  ├─ utils.cpython-311.pyc
   │        │  │  │  │  │  │  └─ version.cpython-311.pyc
   │        │  │  │  │  │  ├─ _elffile.py
   │        │  │  │  │  │  ├─ _manylinux.py
   │        │  │  │  │  │  ├─ _musllinux.py
   │        │  │  │  │  │  ├─ _parser.py
   │        │  │  │  │  │  ├─ _structures.py
   │        │  │  │  │  │  ├─ _tokenizer.py
   │        │  │  │  │  │  ├─ markers.py
   │        │  │  │  │  │  ├─ requirements.py
   │        │  │  │  │  │  ├─ specifiers.py
   │        │  │  │  │  │  ├─ tags.py
   │        │  │  │  │  │  ├─ utils.py
   │        │  │  │  │  │  └─ version.py
   │        │  │  │  │  └─ vendor.txt
   │        │  │  │  └─ wheelfile.py
   │        │  │  ├─ wheel-0.45.1.dist-info
   │        │  │  │  ├─ INSTALLER
   │        │  │  │  ├─ LICENSE.txt
   │        │  │  │  ├─ METADATA
   │        │  │  │  ├─ RECORD
   │        │  │  │  ├─ REQUESTED
   │        │  │  │  ├─ WHEEL
   │        │  │  │  └─ entry_points.txt
   │        │  │  ├─ zipp
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  └─ glob.cpython-311.pyc
   │        │  │  │  ├─ compat
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ py310.cpython-311.pyc
   │        │  │  │  │  └─ py310.py
   │        │  │  │  └─ glob.py
   │        │  │  └─ zipp-3.19.2.dist-info
   │        │  │     ├─ INSTALLER
   │        │  │     ├─ LICENSE
   │        │  │     ├─ METADATA
   │        │  │     ├─ RECORD
   │        │  │     ├─ REQUESTED
   │        │  │     ├─ WHEEL
   │        │  │     └─ top_level.txt
   │        │  ├─ archive_util.py
   │        │  ├─ build_meta.py
   │        │  ├─ cli-32.exe
   │        │  ├─ cli-64.exe
   │        │  ├─ cli-arm64.exe
   │        │  ├─ cli.exe
   │        │  ├─ command
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _requirestxt.cpython-311.pyc
   │        │  │  │  ├─ alias.cpython-311.pyc
   │        │  │  │  ├─ bdist_egg.cpython-311.pyc
   │        │  │  │  ├─ bdist_rpm.cpython-311.pyc
   │        │  │  │  ├─ bdist_wheel.cpython-311.pyc
   │        │  │  │  ├─ build.cpython-311.pyc
   │        │  │  │  ├─ build_clib.cpython-311.pyc
   │        │  │  │  ├─ build_ext.cpython-311.pyc
   │        │  │  │  ├─ build_py.cpython-311.pyc
   │        │  │  │  ├─ develop.cpython-311.pyc
   │        │  │  │  ├─ dist_info.cpython-311.pyc
   │        │  │  │  ├─ easy_install.cpython-311.pyc
   │        │  │  │  ├─ editable_wheel.cpython-311.pyc
   │        │  │  │  ├─ egg_info.cpython-311.pyc
   │        │  │  │  ├─ install.cpython-311.pyc
   │        │  │  │  ├─ install_egg_info.cpython-311.pyc
   │        │  │  │  ├─ install_lib.cpython-311.pyc
   │        │  │  │  ├─ install_scripts.cpython-311.pyc
   │        │  │  │  ├─ rotate.cpython-311.pyc
   │        │  │  │  ├─ saveopts.cpython-311.pyc
   │        │  │  │  ├─ sdist.cpython-311.pyc
   │        │  │  │  ├─ setopt.cpython-311.pyc
   │        │  │  │  └─ test.cpython-311.pyc
   │        │  │  ├─ _requirestxt.py
   │        │  │  ├─ alias.py
   │        │  │  ├─ bdist_egg.py
   │        │  │  ├─ bdist_rpm.py
   │        │  │  ├─ bdist_wheel.py
   │        │  │  ├─ build.py
   │        │  │  ├─ build_clib.py
   │        │  │  ├─ build_ext.py
   │        │  │  ├─ build_py.py
   │        │  │  ├─ develop.py
   │        │  │  ├─ dist_info.py
   │        │  │  ├─ easy_install.py
   │        │  │  ├─ editable_wheel.py
   │        │  │  ├─ egg_info.py
   │        │  │  ├─ install.py
   │        │  │  ├─ install_egg_info.py
   │        │  │  ├─ install_lib.py
   │        │  │  ├─ install_scripts.py
   │        │  │  ├─ launcher manifest.xml
   │        │  │  ├─ rotate.py
   │        │  │  ├─ saveopts.py
   │        │  │  ├─ sdist.py
   │        │  │  ├─ setopt.py
   │        │  │  └─ test.py
   │        │  ├─ compat
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ py310.cpython-311.pyc
   │        │  │  │  ├─ py311.cpython-311.pyc
   │        │  │  │  ├─ py312.cpython-311.pyc
   │        │  │  │  └─ py39.cpython-311.pyc
   │        │  │  ├─ py310.py
   │        │  │  ├─ py311.py
   │        │  │  ├─ py312.py
   │        │  │  └─ py39.py
   │        │  ├─ config
   │        │  │  ├─ NOTICE
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ _apply_pyprojecttoml.cpython-311.pyc
   │        │  │  │  ├─ expand.cpython-311.pyc
   │        │  │  │  ├─ pyprojecttoml.cpython-311.pyc
   │        │  │  │  └─ setupcfg.cpython-311.pyc
   │        │  │  ├─ _apply_pyprojecttoml.py
   │        │  │  ├─ _validate_pyproject
   │        │  │  │  ├─ NOTICE
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ error_reporting.cpython-311.pyc
   │        │  │  │  │  ├─ extra_validations.cpython-311.pyc
   │        │  │  │  │  ├─ fastjsonschema_exceptions.cpython-311.pyc
   │        │  │  │  │  ├─ fastjsonschema_validations.cpython-311.pyc
   │        │  │  │  │  └─ formats.cpython-311.pyc
   │        │  │  │  ├─ error_reporting.py
   │        │  │  │  ├─ extra_validations.py
   │        │  │  │  ├─ fastjsonschema_exceptions.py
   │        │  │  │  ├─ fastjsonschema_validations.py
   │        │  │  │  └─ formats.py
   │        │  │  ├─ distutils.schema.json
   │        │  │  ├─ expand.py
   │        │  │  ├─ pyprojecttoml.py
   │        │  │  ├─ setupcfg.py
   │        │  │  └─ setuptools.schema.json
   │        │  ├─ depends.py
   │        │  ├─ discovery.py
   │        │  ├─ dist.py
   │        │  ├─ errors.py
   │        │  ├─ extension.py
   │        │  ├─ glob.py
   │        │  ├─ gui-32.exe
   │        │  ├─ gui-64.exe
   │        │  ├─ gui-arm64.exe
   │        │  ├─ gui.exe
   │        │  ├─ installer.py
   │        │  ├─ launch.py
   │        │  ├─ logging.py
   │        │  ├─ modified.py
   │        │  ├─ monkey.py
   │        │  ├─ msvc.py
   │        │  ├─ namespaces.py
   │        │  ├─ script (dev).tmpl
   │        │  ├─ script.tmpl
   │        │  ├─ tests
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ contexts.cpython-311.pyc
   │        │  │  │  ├─ environment.cpython-311.pyc
   │        │  │  │  ├─ fixtures.cpython-311.pyc
   │        │  │  │  ├─ mod_with_constant.cpython-311.pyc
   │        │  │  │  ├─ namespaces.cpython-311.pyc
   │        │  │  │  ├─ script-with-bom.cpython-311.pyc
   │        │  │  │  ├─ test_archive_util.cpython-311.pyc
   │        │  │  │  ├─ test_bdist_deprecations.cpython-311.pyc
   │        │  │  │  ├─ test_bdist_egg.cpython-311.pyc
   │        │  │  │  ├─ test_bdist_wheel.cpython-311.pyc
   │        │  │  │  ├─ test_build.cpython-311.pyc
   │        │  │  │  ├─ test_build_clib.cpython-311.pyc
   │        │  │  │  ├─ test_build_ext.cpython-311.pyc
   │        │  │  │  ├─ test_build_meta.cpython-311.pyc
   │        │  │  │  ├─ test_build_py.cpython-311.pyc
   │        │  │  │  ├─ test_config_discovery.cpython-311.pyc
   │        │  │  │  ├─ test_core_metadata.cpython-311.pyc
   │        │  │  │  ├─ test_depends.cpython-311.pyc
   │        │  │  │  ├─ test_develop.cpython-311.pyc
   │        │  │  │  ├─ test_dist.cpython-311.pyc
   │        │  │  │  ├─ test_dist_info.cpython-311.pyc
   │        │  │  │  ├─ test_distutils_adoption.cpython-311.pyc
   │        │  │  │  ├─ test_editable_install.cpython-311.pyc
   │        │  │  │  ├─ test_egg_info.cpython-311.pyc
   │        │  │  │  ├─ test_extern.cpython-311.pyc
   │        │  │  │  ├─ test_find_packages.cpython-311.pyc
   │        │  │  │  ├─ test_find_py_modules.cpython-311.pyc
   │        │  │  │  ├─ test_glob.cpython-311.pyc
   │        │  │  │  ├─ test_install_scripts.cpython-311.pyc
   │        │  │  │  ├─ test_logging.cpython-311.pyc
   │        │  │  │  ├─ test_manifest.cpython-311.pyc
   │        │  │  │  ├─ test_namespaces.cpython-311.pyc
   │        │  │  │  ├─ test_scripts.cpython-311.pyc
   │        │  │  │  ├─ test_sdist.cpython-311.pyc
   │        │  │  │  ├─ test_setopt.cpython-311.pyc
   │        │  │  │  ├─ test_setuptools.cpython-311.pyc
   │        │  │  │  ├─ test_shutil_wrapper.cpython-311.pyc
   │        │  │  │  ├─ test_unicode_utils.cpython-311.pyc
   │        │  │  │  ├─ test_virtualenv.cpython-311.pyc
   │        │  │  │  ├─ test_warnings.cpython-311.pyc
   │        │  │  │  ├─ test_wheel.cpython-311.pyc
   │        │  │  │  ├─ test_windows_wrappers.cpython-311.pyc
   │        │  │  │  ├─ text.cpython-311.pyc
   │        │  │  │  └─ textwrap.cpython-311.pyc
   │        │  │  ├─ compat
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  └─ py39.cpython-311.pyc
   │        │  │  │  └─ py39.py
   │        │  │  ├─ config
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ test_apply_pyprojecttoml.cpython-311.pyc
   │        │  │  │  │  ├─ test_expand.cpython-311.pyc
   │        │  │  │  │  ├─ test_pyprojecttoml.cpython-311.pyc
   │        │  │  │  │  ├─ test_pyprojecttoml_dynamic_deps.cpython-311.pyc
   │        │  │  │  │  └─ test_setupcfg.cpython-311.pyc
   │        │  │  │  ├─ downloads
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  │  └─ preload.cpython-311.pyc
   │        │  │  │  │  └─ preload.py
   │        │  │  │  ├─ setupcfg_examples.txt
   │        │  │  │  ├─ test_apply_pyprojecttoml.py
   │        │  │  │  ├─ test_expand.py
   │        │  │  │  ├─ test_pyprojecttoml.py
   │        │  │  │  ├─ test_pyprojecttoml_dynamic_deps.py
   │        │  │  │  └─ test_setupcfg.py
   │        │  │  ├─ contexts.py
   │        │  │  ├─ environment.py
   │        │  │  ├─ fixtures.py
   │        │  │  ├─ indexes
   │        │  │  │  └─ test_links_priority
   │        │  │  │     ├─ external.html
   │        │  │  │     └─ simple
   │        │  │  │        └─ foobar
   │        │  │  │           └─ index.html
   │        │  │  ├─ integration
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ helpers.cpython-311.pyc
   │        │  │  │  │  ├─ test_pbr.cpython-311.pyc
   │        │  │  │  │  └─ test_pip_install_sdist.cpython-311.pyc
   │        │  │  │  ├─ helpers.py
   │        │  │  │  ├─ test_pbr.py
   │        │  │  │  └─ test_pip_install_sdist.py
   │        │  │  ├─ mod_with_constant.py
   │        │  │  ├─ namespaces.py
   │        │  │  ├─ script-with-bom.py
   │        │  │  ├─ test_archive_util.py
   │        │  │  ├─ test_bdist_deprecations.py
   │        │  │  ├─ test_bdist_egg.py
   │        │  │  ├─ test_bdist_wheel.py
   │        │  │  ├─ test_build.py
   │        │  │  ├─ test_build_clib.py
   │        │  │  ├─ test_build_ext.py
   │        │  │  ├─ test_build_meta.py
   │        │  │  ├─ test_build_py.py
   │        │  │  ├─ test_config_discovery.py
   │        │  │  ├─ test_core_metadata.py
   │        │  │  ├─ test_depends.py
   │        │  │  ├─ test_develop.py
   │        │  │  ├─ test_dist.py
   │        │  │  ├─ test_dist_info.py
   │        │  │  ├─ test_distutils_adoption.py
   │        │  │  ├─ test_editable_install.py
   │        │  │  ├─ test_egg_info.py
   │        │  │  ├─ test_extern.py
   │        │  │  ├─ test_find_packages.py
   │        │  │  ├─ test_find_py_modules.py
   │        │  │  ├─ test_glob.py
   │        │  │  ├─ test_install_scripts.py
   │        │  │  ├─ test_logging.py
   │        │  │  ├─ test_manifest.py
   │        │  │  ├─ test_namespaces.py
   │        │  │  ├─ test_scripts.py
   │        │  │  ├─ test_sdist.py
   │        │  │  ├─ test_setopt.py
   │        │  │  ├─ test_setuptools.py
   │        │  │  ├─ test_shutil_wrapper.py
   │        │  │  ├─ test_unicode_utils.py
   │        │  │  ├─ test_virtualenv.py
   │        │  │  ├─ test_warnings.py
   │        │  │  ├─ test_wheel.py
   │        │  │  ├─ test_windows_wrappers.py
   │        │  │  ├─ text.py
   │        │  │  └─ textwrap.py
   │        │  ├─ unicode_utils.py
   │        │  ├─ version.py
   │        │  ├─ warnings.py
   │        │  ├─ wheel.py
   │        │  └─ windows_support.py
   │        ├─ setuptools-80.7.1.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  ├─ entry_points.txt
   │        │  ├─ licenses
   │        │  │  └─ LICENSE
   │        │  └─ top_level.txt
   │        ├─ six-1.17.0.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ LICENSE
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  └─ top_level.txt
   │        ├─ six.py
   │        ├─ smmap
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ buf.cpython-311.pyc
   │        │  │  ├─ mman.cpython-311.pyc
   │        │  │  └─ util.cpython-311.pyc
   │        │  ├─ buf.py
   │        │  ├─ mman.py
   │        │  ├─ test
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ lib.cpython-311.pyc
   │        │  │  │  ├─ test_buf.cpython-311.pyc
   │        │  │  │  ├─ test_mman.cpython-311.pyc
   │        │  │  │  ├─ test_tutorial.cpython-311.pyc
   │        │  │  │  └─ test_util.cpython-311.pyc
   │        │  │  ├─ lib.py
   │        │  │  ├─ test_buf.py
   │        │  │  ├─ test_mman.py
   │        │  │  ├─ test_tutorial.py
   │        │  │  └─ test_util.py
   │        │  └─ util.py
   │        ├─ smmap-5.0.2.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ LICENSE
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  ├─ top_level.txt
   │        │  └─ zip-safe
   │        ├─ sqlparse
   │        │  ├─ __init__.py
   │        │  ├─ __main__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ __main__.cpython-311.pyc
   │        │  │  ├─ cli.cpython-311.pyc
   │        │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  ├─ formatter.cpython-311.pyc
   │        │  │  ├─ keywords.cpython-311.pyc
   │        │  │  ├─ lexer.cpython-311.pyc
   │        │  │  ├─ sql.cpython-311.pyc
   │        │  │  ├─ tokens.cpython-311.pyc
   │        │  │  └─ utils.cpython-311.pyc
   │        │  ├─ cli.py
   │        │  ├─ engine
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ filter_stack.cpython-311.pyc
   │        │  │  │  ├─ grouping.cpython-311.pyc
   │        │  │  │  └─ statement_splitter.cpython-311.pyc
   │        │  │  ├─ filter_stack.py
   │        │  │  ├─ grouping.py
   │        │  │  └─ statement_splitter.py
   │        │  ├─ exceptions.py
   │        │  ├─ filters
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ aligned_indent.cpython-311.pyc
   │        │  │  │  ├─ others.cpython-311.pyc
   │        │  │  │  ├─ output.cpython-311.pyc
   │        │  │  │  ├─ reindent.cpython-311.pyc
   │        │  │  │  ├─ right_margin.cpython-311.pyc
   │        │  │  │  └─ tokens.cpython-311.pyc
   │        │  │  ├─ aligned_indent.py
   │        │  │  ├─ others.py
   │        │  │  ├─ output.py
   │        │  │  ├─ reindent.py
   │        │  │  ├─ right_margin.py
   │        │  │  └─ tokens.py
   │        │  ├─ formatter.py
   │        │  ├─ keywords.py
   │        │  ├─ lexer.py
   │        │  ├─ sql.py
   │        │  ├─ tokens.py
   │        │  └─ utils.py
   │        ├─ sqlparse-0.5.3.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ WHEEL
   │        │  ├─ entry_points.txt
   │        │  └─ licenses
   │        │     ├─ AUTHORS
   │        │     └─ LICENSE
   │        ├─ streamlit
   │        │  ├─ __init__.py
   │        │  ├─ __main__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ __main__.cpython-311.pyc
   │        │  │  ├─ auth_util.cpython-311.pyc
   │        │  │  ├─ cli_util.cpython-311.pyc
   │        │  │  ├─ column_config.cpython-311.pyc
   │        │  │  ├─ config.cpython-311.pyc
   │        │  │  ├─ config_option.cpython-311.pyc
   │        │  │  ├─ config_util.cpython-311.pyc
   │        │  │  ├─ cursor.cpython-311.pyc
   │        │  │  ├─ dataframe_util.cpython-311.pyc
   │        │  │  ├─ delta_generator.cpython-311.pyc
   │        │  │  ├─ delta_generator_singletons.cpython-311.pyc
   │        │  │  ├─ deprecation_util.cpython-311.pyc
   │        │  │  ├─ development.cpython-311.pyc
   │        │  │  ├─ emojis.cpython-311.pyc
   │        │  │  ├─ env_util.cpython-311.pyc
   │        │  │  ├─ error_util.cpython-311.pyc
   │        │  │  ├─ errors.cpython-311.pyc
   │        │  │  ├─ file_util.cpython-311.pyc
   │        │  │  ├─ git_util.cpython-311.pyc
   │        │  │  ├─ logger.cpython-311.pyc
   │        │  │  ├─ material_icon_names.cpython-311.pyc
   │        │  │  ├─ net_util.cpython-311.pyc
   │        │  │  ├─ platform.cpython-311.pyc
   │        │  │  ├─ source_util.cpython-311.pyc
   │        │  │  ├─ string_util.cpython-311.pyc
   │        │  │  ├─ temporary_directory.cpython-311.pyc
   │        │  │  ├─ time_util.cpython-311.pyc
   │        │  │  ├─ type_util.cpython-311.pyc
   │        │  │  ├─ url_util.cpython-311.pyc
   │        │  │  ├─ user_info.cpython-311.pyc
   │        │  │  ├─ util.cpython-311.pyc
   │        │  │  └─ version.cpython-311.pyc
   │        │  ├─ auth_util.py
   │        │  ├─ cli_util.py
   │        │  ├─ column_config.py
   │        │  ├─ commands
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ echo.cpython-311.pyc
   │        │  │  │  ├─ execution_control.cpython-311.pyc
   │        │  │  │  ├─ experimental_query_params.cpython-311.pyc
   │        │  │  │  ├─ logo.cpython-311.pyc
   │        │  │  │  ├─ navigation.cpython-311.pyc
   │        │  │  │  └─ page_config.cpython-311.pyc
   │        │  │  ├─ echo.py
   │        │  │  ├─ execution_control.py
   │        │  │  ├─ experimental_query_params.py
   │        │  │  ├─ logo.py
   │        │  │  ├─ navigation.py
   │        │  │  └─ page_config.py
   │        │  ├─ components
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  ├─ lib
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  └─ local_component_registry.cpython-311.pyc
   │        │  │  │  └─ local_component_registry.py
   │        │  │  ├─ types
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ base_component_registry.cpython-311.pyc
   │        │  │  │  │  └─ base_custom_component.cpython-311.pyc
   │        │  │  │  ├─ base_component_registry.py
   │        │  │  │  └─ base_custom_component.py
   │        │  │  └─ v1
   │        │  │     ├─ __init__.py
   │        │  │     ├─ __pycache__
   │        │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │     │  ├─ component_arrow.cpython-311.pyc
   │        │  │     │  ├─ component_registry.cpython-311.pyc
   │        │  │     │  ├─ components.cpython-311.pyc
   │        │  │     │  └─ custom_component.cpython-311.pyc
   │        │  │     ├─ component_arrow.py
   │        │  │     ├─ component_registry.py
   │        │  │     ├─ components.py
   │        │  │     └─ custom_component.py
   │        │  ├─ config.py
   │        │  ├─ config_option.py
   │        │  ├─ config_util.py
   │        │  ├─ connections
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ base_connection.cpython-311.pyc
   │        │  │  │  ├─ snowflake_connection.cpython-311.pyc
   │        │  │  │  ├─ snowpark_connection.cpython-311.pyc
   │        │  │  │  ├─ sql_connection.cpython-311.pyc
   │        │  │  │  └─ util.cpython-311.pyc
   │        │  │  ├─ base_connection.py
   │        │  │  ├─ snowflake_connection.py
   │        │  │  ├─ snowpark_connection.py
   │        │  │  ├─ sql_connection.py
   │        │  │  └─ util.py
   │        │  ├─ cursor.py
   │        │  ├─ dataframe_util.py
   │        │  ├─ delta_generator.py
   │        │  ├─ delta_generator_singletons.py
   │        │  ├─ deprecation_util.py
   │        │  ├─ development.py
   │        │  ├─ elements
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ alert.cpython-311.pyc
   │        │  │  │  ├─ arrow.cpython-311.pyc
   │        │  │  │  ├─ balloons.cpython-311.pyc
   │        │  │  │  ├─ bokeh_chart.cpython-311.pyc
   │        │  │  │  ├─ code.cpython-311.pyc
   │        │  │  │  ├─ deck_gl_json_chart.cpython-311.pyc
   │        │  │  │  ├─ dialog_decorator.cpython-311.pyc
   │        │  │  │  ├─ doc_string.cpython-311.pyc
   │        │  │  │  ├─ empty.cpython-311.pyc
   │        │  │  │  ├─ exception.cpython-311.pyc
   │        │  │  │  ├─ form.cpython-311.pyc
   │        │  │  │  ├─ graphviz_chart.cpython-311.pyc
   │        │  │  │  ├─ heading.cpython-311.pyc
   │        │  │  │  ├─ html.cpython-311.pyc
   │        │  │  │  ├─ iframe.cpython-311.pyc
   │        │  │  │  ├─ image.cpython-311.pyc
   │        │  │  │  ├─ json.cpython-311.pyc
   │        │  │  │  ├─ layouts.cpython-311.pyc
   │        │  │  │  ├─ map.cpython-311.pyc
   │        │  │  │  ├─ markdown.cpython-311.pyc
   │        │  │  │  ├─ media.cpython-311.pyc
   │        │  │  │  ├─ metric.cpython-311.pyc
   │        │  │  │  ├─ plotly_chart.cpython-311.pyc
   │        │  │  │  ├─ progress.cpython-311.pyc
   │        │  │  │  ├─ pyplot.cpython-311.pyc
   │        │  │  │  ├─ snow.cpython-311.pyc
   │        │  │  │  ├─ spinner.cpython-311.pyc
   │        │  │  │  ├─ text.cpython-311.pyc
   │        │  │  │  ├─ toast.cpython-311.pyc
   │        │  │  │  ├─ vega_charts.cpython-311.pyc
   │        │  │  │  └─ write.cpython-311.pyc
   │        │  │  ├─ alert.py
   │        │  │  ├─ arrow.py
   │        │  │  ├─ balloons.py
   │        │  │  ├─ bokeh_chart.py
   │        │  │  ├─ code.py
   │        │  │  ├─ deck_gl_json_chart.py
   │        │  │  ├─ dialog_decorator.py
   │        │  │  ├─ doc_string.py
   │        │  │  ├─ empty.py
   │        │  │  ├─ exception.py
   │        │  │  ├─ form.py
   │        │  │  ├─ graphviz_chart.py
   │        │  │  ├─ heading.py
   │        │  │  ├─ html.py
   │        │  │  ├─ iframe.py
   │        │  │  ├─ image.py
   │        │  │  ├─ json.py
   │        │  │  ├─ layouts.py
   │        │  │  ├─ lib
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ built_in_chart_utils.cpython-311.pyc
   │        │  │  │  │  ├─ color_util.cpython-311.pyc
   │        │  │  │  │  ├─ column_config_utils.cpython-311.pyc
   │        │  │  │  │  ├─ column_types.cpython-311.pyc
   │        │  │  │  │  ├─ dialog.cpython-311.pyc
   │        │  │  │  │  ├─ dicttools.cpython-311.pyc
   │        │  │  │  │  ├─ event_utils.cpython-311.pyc
   │        │  │  │  │  ├─ file_uploader_utils.cpython-311.pyc
   │        │  │  │  │  ├─ form_utils.cpython-311.pyc
   │        │  │  │  │  ├─ image_utils.cpython-311.pyc
   │        │  │  │  │  ├─ js_number.cpython-311.pyc
   │        │  │  │  │  ├─ layout_utils.cpython-311.pyc
   │        │  │  │  │  ├─ mutable_status_container.cpython-311.pyc
   │        │  │  │  │  ├─ options_selector_utils.cpython-311.pyc
   │        │  │  │  │  ├─ pandas_styler_utils.cpython-311.pyc
   │        │  │  │  │  ├─ policies.cpython-311.pyc
   │        │  │  │  │  ├─ streamlit_plotly_theme.cpython-311.pyc
   │        │  │  │  │  ├─ subtitle_utils.cpython-311.pyc
   │        │  │  │  │  └─ utils.cpython-311.pyc
   │        │  │  │  ├─ built_in_chart_utils.py
   │        │  │  │  ├─ color_util.py
   │        │  │  │  ├─ column_config_utils.py
   │        │  │  │  ├─ column_types.py
   │        │  │  │  ├─ dialog.py
   │        │  │  │  ├─ dicttools.py
   │        │  │  │  ├─ event_utils.py
   │        │  │  │  ├─ file_uploader_utils.py
   │        │  │  │  ├─ form_utils.py
   │        │  │  │  ├─ image_utils.py
   │        │  │  │  ├─ js_number.py
   │        │  │  │  ├─ layout_utils.py
   │        │  │  │  ├─ mutable_status_container.py
   │        │  │  │  ├─ options_selector_utils.py
   │        │  │  │  ├─ pandas_styler_utils.py
   │        │  │  │  ├─ policies.py
   │        │  │  │  ├─ streamlit_plotly_theme.py
   │        │  │  │  ├─ subtitle_utils.py
   │        │  │  │  └─ utils.py
   │        │  │  ├─ map.py
   │        │  │  ├─ markdown.py
   │        │  │  ├─ media.py
   │        │  │  ├─ metric.py
   │        │  │  ├─ plotly_chart.py
   │        │  │  ├─ progress.py
   │        │  │  ├─ pyplot.py
   │        │  │  ├─ snow.py
   │        │  │  ├─ spinner.py
   │        │  │  ├─ text.py
   │        │  │  ├─ toast.py
   │        │  │  ├─ vega_charts.py
   │        │  │  ├─ widgets
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ audio_input.cpython-311.pyc
   │        │  │  │  │  ├─ button.cpython-311.pyc
   │        │  │  │  │  ├─ button_group.cpython-311.pyc
   │        │  │  │  │  ├─ camera_input.cpython-311.pyc
   │        │  │  │  │  ├─ chat.cpython-311.pyc
   │        │  │  │  │  ├─ checkbox.cpython-311.pyc
   │        │  │  │  │  ├─ color_picker.cpython-311.pyc
   │        │  │  │  │  ├─ data_editor.cpython-311.pyc
   │        │  │  │  │  ├─ file_uploader.cpython-311.pyc
   │        │  │  │  │  ├─ multiselect.cpython-311.pyc
   │        │  │  │  │  ├─ number_input.cpython-311.pyc
   │        │  │  │  │  ├─ radio.cpython-311.pyc
   │        │  │  │  │  ├─ select_slider.cpython-311.pyc
   │        │  │  │  │  ├─ selectbox.cpython-311.pyc
   │        │  │  │  │  ├─ slider.cpython-311.pyc
   │        │  │  │  │  ├─ text_widgets.cpython-311.pyc
   │        │  │  │  │  └─ time_widgets.cpython-311.pyc
   │        │  │  │  ├─ audio_input.py
   │        │  │  │  ├─ button.py
   │        │  │  │  ├─ button_group.py
   │        │  │  │  ├─ camera_input.py
   │        │  │  │  ├─ chat.py
   │        │  │  │  ├─ checkbox.py
   │        │  │  │  ├─ color_picker.py
   │        │  │  │  ├─ data_editor.py
   │        │  │  │  ├─ file_uploader.py
   │        │  │  │  ├─ multiselect.py
   │        │  │  │  ├─ number_input.py
   │        │  │  │  ├─ radio.py
   │        │  │  │  ├─ select_slider.py
   │        │  │  │  ├─ selectbox.py
   │        │  │  │  ├─ slider.py
   │        │  │  │  ├─ text_widgets.py
   │        │  │  │  └─ time_widgets.py
   │        │  │  └─ write.py
   │        │  ├─ emojis.py
   │        │  ├─ env_util.py
   │        │  ├─ error_util.py
   │        │  ├─ errors.py
   │        │  ├─ external
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  └─ langchain
   │        │  │     ├─ __init__.py
   │        │  │     ├─ __pycache__
   │        │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │     │  └─ streamlit_callback_handler.cpython-311.pyc
   │        │  │     └─ streamlit_callback_handler.py
   │        │  ├─ file_util.py
   │        │  ├─ git_util.py
   │        │  ├─ hello
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ animation_demo.cpython-311.pyc
   │        │  │  │  ├─ dataframe_demo.cpython-311.pyc
   │        │  │  │  ├─ hello.cpython-311.pyc
   │        │  │  │  ├─ mapping_demo.cpython-311.pyc
   │        │  │  │  ├─ plotting_demo.cpython-311.pyc
   │        │  │  │  ├─ streamlit_app.cpython-311.pyc
   │        │  │  │  └─ utils.cpython-311.pyc
   │        │  │  ├─ animation_demo.py
   │        │  │  ├─ dataframe_demo.py
   │        │  │  ├─ hello.py
   │        │  │  ├─ mapping_demo.py
   │        │  │  ├─ plotting_demo.py
   │        │  │  ├─ streamlit_app.py
   │        │  │  └─ utils.py
   │        │  ├─ logger.py
   │        │  ├─ material_icon_names.py
   │        │  ├─ navigation
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  └─ page.cpython-311.pyc
   │        │  │  └─ page.py
   │        │  ├─ net_util.py
   │        │  ├─ platform.py
   │        │  ├─ proto
   │        │  │  ├─ Alert_pb2.py
   │        │  │  ├─ Alert_pb2.pyi
   │        │  │  ├─ AppPage_pb2.py
   │        │  │  ├─ AppPage_pb2.pyi
   │        │  │  ├─ ArrowNamedDataSet_pb2.py
   │        │  │  ├─ ArrowNamedDataSet_pb2.pyi
   │        │  │  ├─ ArrowVegaLiteChart_pb2.py
   │        │  │  ├─ ArrowVegaLiteChart_pb2.pyi
   │        │  │  ├─ Arrow_pb2.py
   │        │  │  ├─ Arrow_pb2.pyi
   │        │  │  ├─ AudioInput_pb2.py
   │        │  │  ├─ AudioInput_pb2.pyi
   │        │  │  ├─ Audio_pb2.py
   │        │  │  ├─ Audio_pb2.pyi
   │        │  │  ├─ AuthRedirect_pb2.py
   │        │  │  ├─ AuthRedirect_pb2.pyi
   │        │  │  ├─ AutoRerun_pb2.py
   │        │  │  ├─ AutoRerun_pb2.pyi
   │        │  │  ├─ BackMsg_pb2.py
   │        │  │  ├─ BackMsg_pb2.pyi
   │        │  │  ├─ Balloons_pb2.py
   │        │  │  ├─ Balloons_pb2.pyi
   │        │  │  ├─ Block_pb2.py
   │        │  │  ├─ Block_pb2.pyi
   │        │  │  ├─ BokehChart_pb2.py
   │        │  │  ├─ BokehChart_pb2.pyi
   │        │  │  ├─ ButtonGroup_pb2.py
   │        │  │  ├─ ButtonGroup_pb2.pyi
   │        │  │  ├─ Button_pb2.py
   │        │  │  ├─ Button_pb2.pyi
   │        │  │  ├─ CameraInput_pb2.py
   │        │  │  ├─ CameraInput_pb2.pyi
   │        │  │  ├─ ChatInput_pb2.py
   │        │  │  ├─ ChatInput_pb2.pyi
   │        │  │  ├─ Checkbox_pb2.py
   │        │  │  ├─ Checkbox_pb2.pyi
   │        │  │  ├─ ClientState_pb2.py
   │        │  │  ├─ ClientState_pb2.pyi
   │        │  │  ├─ Code_pb2.py
   │        │  │  ├─ Code_pb2.pyi
   │        │  │  ├─ ColorPicker_pb2.py
   │        │  │  ├─ ColorPicker_pb2.pyi
   │        │  │  ├─ Common_pb2.py
   │        │  │  ├─ Common_pb2.pyi
   │        │  │  ├─ Components_pb2.py
   │        │  │  ├─ Components_pb2.pyi
   │        │  │  ├─ DataFrame_pb2.py
   │        │  │  ├─ DataFrame_pb2.pyi
   │        │  │  ├─ DateInput_pb2.py
   │        │  │  ├─ DateInput_pb2.pyi
   │        │  │  ├─ DeckGlJsonChart_pb2.py
   │        │  │  ├─ DeckGlJsonChart_pb2.pyi
   │        │  │  ├─ Delta_pb2.py
   │        │  │  ├─ Delta_pb2.pyi
   │        │  │  ├─ DocString_pb2.py
   │        │  │  ├─ DocString_pb2.pyi
   │        │  │  ├─ DownloadButton_pb2.py
   │        │  │  ├─ DownloadButton_pb2.pyi
   │        │  │  ├─ Element_pb2.py
   │        │  │  ├─ Element_pb2.pyi
   │        │  │  ├─ Empty_pb2.py
   │        │  │  ├─ Empty_pb2.pyi
   │        │  │  ├─ Exception_pb2.py
   │        │  │  ├─ Exception_pb2.pyi
   │        │  │  ├─ Favicon_pb2.py
   │        │  │  ├─ Favicon_pb2.pyi
   │        │  │  ├─ FileUploader_pb2.py
   │        │  │  ├─ FileUploader_pb2.pyi
   │        │  │  ├─ ForwardMsg_pb2.py
   │        │  │  ├─ ForwardMsg_pb2.pyi
   │        │  │  ├─ GitInfo_pb2.py
   │        │  │  ├─ GitInfo_pb2.pyi
   │        │  │  ├─ GraphVizChart_pb2.py
   │        │  │  ├─ GraphVizChart_pb2.pyi
   │        │  │  ├─ Heading_pb2.py
   │        │  │  ├─ Heading_pb2.pyi
   │        │  │  ├─ Html_pb2.py
   │        │  │  ├─ Html_pb2.pyi
   │        │  │  ├─ IFrame_pb2.py
   │        │  │  ├─ IFrame_pb2.pyi
   │        │  │  ├─ Image_pb2.py
   │        │  │  ├─ Image_pb2.pyi
   │        │  │  ├─ Json_pb2.py
   │        │  │  ├─ Json_pb2.pyi
   │        │  │  ├─ LabelVisibilityMessage_pb2.py
   │        │  │  ├─ LabelVisibilityMessage_pb2.pyi
   │        │  │  ├─ LinkButton_pb2.py
   │        │  │  ├─ LinkButton_pb2.pyi
   │        │  │  ├─ Logo_pb2.py
   │        │  │  ├─ Logo_pb2.pyi
   │        │  │  ├─ Markdown_pb2.py
   │        │  │  ├─ Markdown_pb2.pyi
   │        │  │  ├─ Metric_pb2.py
   │        │  │  ├─ Metric_pb2.pyi
   │        │  │  ├─ MetricsEvent_pb2.py
   │        │  │  ├─ MetricsEvent_pb2.pyi
   │        │  │  ├─ MultiSelect_pb2.py
   │        │  │  ├─ MultiSelect_pb2.pyi
   │        │  │  ├─ NamedDataSet_pb2.py
   │        │  │  ├─ NamedDataSet_pb2.pyi
   │        │  │  ├─ Navigation_pb2.py
   │        │  │  ├─ Navigation_pb2.pyi
   │        │  │  ├─ NewSession_pb2.py
   │        │  │  ├─ NewSession_pb2.pyi
   │        │  │  ├─ NumberInput_pb2.py
   │        │  │  ├─ NumberInput_pb2.pyi
   │        │  │  ├─ PageConfig_pb2.py
   │        │  │  ├─ PageConfig_pb2.pyi
   │        │  │  ├─ PageInfo_pb2.py
   │        │  │  ├─ PageInfo_pb2.pyi
   │        │  │  ├─ PageLink_pb2.py
   │        │  │  ├─ PageLink_pb2.pyi
   │        │  │  ├─ PageNotFound_pb2.py
   │        │  │  ├─ PageNotFound_pb2.pyi
   │        │  │  ├─ PageProfile_pb2.py
   │        │  │  ├─ PageProfile_pb2.pyi
   │        │  │  ├─ PagesChanged_pb2.py
   │        │  │  ├─ PagesChanged_pb2.pyi
   │        │  │  ├─ ParentMessage_pb2.py
   │        │  │  ├─ ParentMessage_pb2.pyi
   │        │  │  ├─ PlotlyChart_pb2.py
   │        │  │  ├─ PlotlyChart_pb2.pyi
   │        │  │  ├─ Progress_pb2.py
   │        │  │  ├─ Progress_pb2.pyi
   │        │  │  ├─ Radio_pb2.py
   │        │  │  ├─ Radio_pb2.pyi
   │        │  │  ├─ RootContainer_pb2.py
   │        │  │  ├─ RootContainer_pb2.pyi
   │        │  │  ├─ Selectbox_pb2.py
   │        │  │  ├─ Selectbox_pb2.pyi
   │        │  │  ├─ SessionEvent_pb2.py
   │        │  │  ├─ SessionEvent_pb2.pyi
   │        │  │  ├─ SessionStatus_pb2.py
   │        │  │  ├─ SessionStatus_pb2.pyi
   │        │  │  ├─ Skeleton_pb2.py
   │        │  │  ├─ Skeleton_pb2.pyi
   │        │  │  ├─ Slider_pb2.py
   │        │  │  ├─ Slider_pb2.pyi
   │        │  │  ├─ Snow_pb2.py
   │        │  │  ├─ Snow_pb2.pyi
   │        │  │  ├─ Spinner_pb2.py
   │        │  │  ├─ Spinner_pb2.pyi
   │        │  │  ├─ TextArea_pb2.py
   │        │  │  ├─ TextArea_pb2.pyi
   │        │  │  ├─ TextInput_pb2.py
   │        │  │  ├─ TextInput_pb2.pyi
   │        │  │  ├─ Text_pb2.py
   │        │  │  ├─ Text_pb2.pyi
   │        │  │  ├─ TimeInput_pb2.py
   │        │  │  ├─ TimeInput_pb2.pyi
   │        │  │  ├─ Toast_pb2.py
   │        │  │  ├─ Toast_pb2.pyi
   │        │  │  ├─ VegaLiteChart_pb2.py
   │        │  │  ├─ VegaLiteChart_pb2.pyi
   │        │  │  ├─ Video_pb2.py
   │        │  │  ├─ Video_pb2.pyi
   │        │  │  ├─ WidgetStates_pb2.py
   │        │  │  ├─ WidgetStates_pb2.pyi
   │        │  │  ├─ WidthConfig_pb2.py
   │        │  │  ├─ WidthConfig_pb2.pyi
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ Alert_pb2.cpython-311.pyc
   │        │  │  │  ├─ AppPage_pb2.cpython-311.pyc
   │        │  │  │  ├─ ArrowNamedDataSet_pb2.cpython-311.pyc
   │        │  │  │  ├─ ArrowVegaLiteChart_pb2.cpython-311.pyc
   │        │  │  │  ├─ Arrow_pb2.cpython-311.pyc
   │        │  │  │  ├─ AudioInput_pb2.cpython-311.pyc
   │        │  │  │  ├─ Audio_pb2.cpython-311.pyc
   │        │  │  │  ├─ AuthRedirect_pb2.cpython-311.pyc
   │        │  │  │  ├─ AutoRerun_pb2.cpython-311.pyc
   │        │  │  │  ├─ BackMsg_pb2.cpython-311.pyc
   │        │  │  │  ├─ Balloons_pb2.cpython-311.pyc
   │        │  │  │  ├─ Block_pb2.cpython-311.pyc
   │        │  │  │  ├─ BokehChart_pb2.cpython-311.pyc
   │        │  │  │  ├─ ButtonGroup_pb2.cpython-311.pyc
   │        │  │  │  ├─ Button_pb2.cpython-311.pyc
   │        │  │  │  ├─ CameraInput_pb2.cpython-311.pyc
   │        │  │  │  ├─ ChatInput_pb2.cpython-311.pyc
   │        │  │  │  ├─ Checkbox_pb2.cpython-311.pyc
   │        │  │  │  ├─ ClientState_pb2.cpython-311.pyc
   │        │  │  │  ├─ Code_pb2.cpython-311.pyc
   │        │  │  │  ├─ ColorPicker_pb2.cpython-311.pyc
   │        │  │  │  ├─ Common_pb2.cpython-311.pyc
   │        │  │  │  ├─ Components_pb2.cpython-311.pyc
   │        │  │  │  ├─ DataFrame_pb2.cpython-311.pyc
   │        │  │  │  ├─ DateInput_pb2.cpython-311.pyc
   │        │  │  │  ├─ DeckGlJsonChart_pb2.cpython-311.pyc
   │        │  │  │  ├─ Delta_pb2.cpython-311.pyc
   │        │  │  │  ├─ DocString_pb2.cpython-311.pyc
   │        │  │  │  ├─ DownloadButton_pb2.cpython-311.pyc
   │        │  │  │  ├─ Element_pb2.cpython-311.pyc
   │        │  │  │  ├─ Empty_pb2.cpython-311.pyc
   │        │  │  │  ├─ Exception_pb2.cpython-311.pyc
   │        │  │  │  ├─ Favicon_pb2.cpython-311.pyc
   │        │  │  │  ├─ FileUploader_pb2.cpython-311.pyc
   │        │  │  │  ├─ ForwardMsg_pb2.cpython-311.pyc
   │        │  │  │  ├─ GitInfo_pb2.cpython-311.pyc
   │        │  │  │  ├─ GraphVizChart_pb2.cpython-311.pyc
   │        │  │  │  ├─ Heading_pb2.cpython-311.pyc
   │        │  │  │  ├─ Html_pb2.cpython-311.pyc
   │        │  │  │  ├─ IFrame_pb2.cpython-311.pyc
   │        │  │  │  ├─ Image_pb2.cpython-311.pyc
   │        │  │  │  ├─ Json_pb2.cpython-311.pyc
   │        │  │  │  ├─ LabelVisibilityMessage_pb2.cpython-311.pyc
   │        │  │  │  ├─ LinkButton_pb2.cpython-311.pyc
   │        │  │  │  ├─ Logo_pb2.cpython-311.pyc
   │        │  │  │  ├─ Markdown_pb2.cpython-311.pyc
   │        │  │  │  ├─ Metric_pb2.cpython-311.pyc
   │        │  │  │  ├─ MetricsEvent_pb2.cpython-311.pyc
   │        │  │  │  ├─ MultiSelect_pb2.cpython-311.pyc
   │        │  │  │  ├─ NamedDataSet_pb2.cpython-311.pyc
   │        │  │  │  ├─ Navigation_pb2.cpython-311.pyc
   │        │  │  │  ├─ NewSession_pb2.cpython-311.pyc
   │        │  │  │  ├─ NumberInput_pb2.cpython-311.pyc
   │        │  │  │  ├─ PageConfig_pb2.cpython-311.pyc
   │        │  │  │  ├─ PageInfo_pb2.cpython-311.pyc
   │        │  │  │  ├─ PageLink_pb2.cpython-311.pyc
   │        │  │  │  ├─ PageNotFound_pb2.cpython-311.pyc
   │        │  │  │  ├─ PageProfile_pb2.cpython-311.pyc
   │        │  │  │  ├─ PagesChanged_pb2.cpython-311.pyc
   │        │  │  │  ├─ ParentMessage_pb2.cpython-311.pyc
   │        │  │  │  ├─ PlotlyChart_pb2.cpython-311.pyc
   │        │  │  │  ├─ Progress_pb2.cpython-311.pyc
   │        │  │  │  ├─ Radio_pb2.cpython-311.pyc
   │        │  │  │  ├─ RootContainer_pb2.cpython-311.pyc
   │        │  │  │  ├─ Selectbox_pb2.cpython-311.pyc
   │        │  │  │  ├─ SessionEvent_pb2.cpython-311.pyc
   │        │  │  │  ├─ SessionStatus_pb2.cpython-311.pyc
   │        │  │  │  ├─ Skeleton_pb2.cpython-311.pyc
   │        │  │  │  ├─ Slider_pb2.cpython-311.pyc
   │        │  │  │  ├─ Snow_pb2.cpython-311.pyc
   │        │  │  │  ├─ Spinner_pb2.cpython-311.pyc
   │        │  │  │  ├─ TextArea_pb2.cpython-311.pyc
   │        │  │  │  ├─ TextInput_pb2.cpython-311.pyc
   │        │  │  │  ├─ Text_pb2.cpython-311.pyc
   │        │  │  │  ├─ TimeInput_pb2.cpython-311.pyc
   │        │  │  │  ├─ Toast_pb2.cpython-311.pyc
   │        │  │  │  ├─ VegaLiteChart_pb2.cpython-311.pyc
   │        │  │  │  ├─ Video_pb2.cpython-311.pyc
   │        │  │  │  ├─ WidgetStates_pb2.cpython-311.pyc
   │        │  │  │  ├─ WidthConfig_pb2.cpython-311.pyc
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  └─ openmetrics_data_model_pb2.cpython-311.pyc
   │        │  │  ├─ openmetrics_data_model_pb2.py
   │        │  │  └─ openmetrics_data_model_pb2.pyi
   │        │  ├─ py.typed
   │        │  ├─ runtime
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ app_session.cpython-311.pyc
   │        │  │  │  ├─ connection_factory.cpython-311.pyc
   │        │  │  │  ├─ context.cpython-311.pyc
   │        │  │  │  ├─ context_util.cpython-311.pyc
   │        │  │  │  ├─ credentials.cpython-311.pyc
   │        │  │  │  ├─ forward_msg_cache.cpython-311.pyc
   │        │  │  │  ├─ forward_msg_queue.cpython-311.pyc
   │        │  │  │  ├─ fragment.cpython-311.pyc
   │        │  │  │  ├─ media_file_manager.cpython-311.pyc
   │        │  │  │  ├─ media_file_storage.cpython-311.pyc
   │        │  │  │  ├─ memory_media_file_storage.cpython-311.pyc
   │        │  │  │  ├─ memory_session_storage.cpython-311.pyc
   │        │  │  │  ├─ memory_uploaded_file_manager.cpython-311.pyc
   │        │  │  │  ├─ metrics_util.cpython-311.pyc
   │        │  │  │  ├─ pages_manager.cpython-311.pyc
   │        │  │  │  ├─ runtime.cpython-311.pyc
   │        │  │  │  ├─ runtime_util.cpython-311.pyc
   │        │  │  │  ├─ script_data.cpython-311.pyc
   │        │  │  │  ├─ secrets.cpython-311.pyc
   │        │  │  │  ├─ session_manager.cpython-311.pyc
   │        │  │  │  ├─ stats.cpython-311.pyc
   │        │  │  │  ├─ uploaded_file_manager.cpython-311.pyc
   │        │  │  │  └─ websocket_session_manager.cpython-311.pyc
   │        │  │  ├─ app_session.py
   │        │  │  ├─ caching
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ cache_data_api.cpython-311.pyc
   │        │  │  │  │  ├─ cache_errors.cpython-311.pyc
   │        │  │  │  │  ├─ cache_resource_api.cpython-311.pyc
   │        │  │  │  │  ├─ cache_type.cpython-311.pyc
   │        │  │  │  │  ├─ cache_utils.cpython-311.pyc
   │        │  │  │  │  ├─ cached_message_replay.cpython-311.pyc
   │        │  │  │  │  ├─ hashing.cpython-311.pyc
   │        │  │  │  │  └─ legacy_cache_api.cpython-311.pyc
   │        │  │  │  ├─ cache_data_api.py
   │        │  │  │  ├─ cache_errors.py
   │        │  │  │  ├─ cache_resource_api.py
   │        │  │  │  ├─ cache_type.py
   │        │  │  │  ├─ cache_utils.py
   │        │  │  │  ├─ cached_message_replay.py
   │        │  │  │  ├─ hashing.py
   │        │  │  │  ├─ legacy_cache_api.py
   │        │  │  │  └─ storage
   │        │  │  │     ├─ __init__.py
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │  │     │  ├─ cache_storage_protocol.cpython-311.pyc
   │        │  │  │     │  ├─ dummy_cache_storage.cpython-311.pyc
   │        │  │  │     │  ├─ in_memory_cache_storage_wrapper.cpython-311.pyc
   │        │  │  │     │  └─ local_disk_cache_storage.cpython-311.pyc
   │        │  │  │     ├─ cache_storage_protocol.py
   │        │  │  │     ├─ dummy_cache_storage.py
   │        │  │  │     ├─ in_memory_cache_storage_wrapper.py
   │        │  │  │     └─ local_disk_cache_storage.py
   │        │  │  ├─ connection_factory.py
   │        │  │  ├─ context.py
   │        │  │  ├─ context_util.py
   │        │  │  ├─ credentials.py
   │        │  │  ├─ forward_msg_cache.py
   │        │  │  ├─ forward_msg_queue.py
   │        │  │  ├─ fragment.py
   │        │  │  ├─ media_file_manager.py
   │        │  │  ├─ media_file_storage.py
   │        │  │  ├─ memory_media_file_storage.py
   │        │  │  ├─ memory_session_storage.py
   │        │  │  ├─ memory_uploaded_file_manager.py
   │        │  │  ├─ metrics_util.py
   │        │  │  ├─ pages_manager.py
   │        │  │  ├─ runtime.py
   │        │  │  ├─ runtime_util.py
   │        │  │  ├─ script_data.py
   │        │  │  ├─ scriptrunner
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ exec_code.cpython-311.pyc
   │        │  │  │  │  ├─ magic.cpython-311.pyc
   │        │  │  │  │  ├─ magic_funcs.cpython-311.pyc
   │        │  │  │  │  ├─ script_cache.cpython-311.pyc
   │        │  │  │  │  └─ script_runner.cpython-311.pyc
   │        │  │  │  ├─ exec_code.py
   │        │  │  │  ├─ magic.py
   │        │  │  │  ├─ magic_funcs.py
   │        │  │  │  ├─ script_cache.py
   │        │  │  │  └─ script_runner.py
   │        │  │  ├─ scriptrunner_utils
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  │  │  ├─ script_requests.cpython-311.pyc
   │        │  │  │  │  └─ script_run_context.cpython-311.pyc
   │        │  │  │  ├─ exceptions.py
   │        │  │  │  ├─ script_requests.py
   │        │  │  │  └─ script_run_context.py
   │        │  │  ├─ secrets.py
   │        │  │  ├─ session_manager.py
   │        │  │  ├─ state
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ common.cpython-311.pyc
   │        │  │  │  │  ├─ query_params.cpython-311.pyc
   │        │  │  │  │  ├─ query_params_proxy.cpython-311.pyc
   │        │  │  │  │  ├─ safe_session_state.cpython-311.pyc
   │        │  │  │  │  ├─ session_state.cpython-311.pyc
   │        │  │  │  │  ├─ session_state_proxy.cpython-311.pyc
   │        │  │  │  │  └─ widgets.cpython-311.pyc
   │        │  │  │  ├─ common.py
   │        │  │  │  ├─ query_params.py
   │        │  │  │  ├─ query_params_proxy.py
   │        │  │  │  ├─ safe_session_state.py
   │        │  │  │  ├─ session_state.py
   │        │  │  │  ├─ session_state_proxy.py
   │        │  │  │  └─ widgets.py
   │        │  │  ├─ stats.py
   │        │  │  ├─ uploaded_file_manager.py
   │        │  │  └─ websocket_session_manager.py
   │        │  ├─ source_util.py
   │        │  ├─ static
   │        │  │  ├─ favicon.png
   │        │  │  ├─ index.html
   │        │  │  └─ static
   │        │  │     ├─ css
   │        │  │     │  ├─ index.C5t3M85E.css
   │        │  │     │  ├─ index.DqDwtg6_.css
   │        │  │     │  └─ index.DzuxGC_t.css
   │        │  │     ├─ js
   │        │  │     │  ├─ ErrorOutline.esm.DU9IrB3M.js
   │        │  │     │  ├─ FileDownload.esm.P9rKwKo8.js
   │        │  │     │  ├─ FileHelper.D7RMkx0e.js
   │        │  │     │  ├─ FormClearHelper.B67tgll0.js
   │        │  │     │  ├─ Hooks.ncTJktu9.js
   │        │  │     │  ├─ InputInstructions.D-Y8geDN.js
   │        │  │     │  ├─ ProgressBar.B-kexwwD.js
   │        │  │     │  ├─ RenderInPortalIfExists.BgaoZgep.js
   │        │  │     │  ├─ Toolbar.D9RUZv9G.js
   │        │  │     │  ├─ UploadFileInfo.C-jY39rj.js
   │        │  │     │  ├─ base-input.BoAa1U94.js
   │        │  │     │  ├─ checkbox.Z6iSfe5F.js
   │        │  │     │  ├─ createDownloadLinkElement.DZMwyjvU.js
   │        │  │     │  ├─ createSuper.B4oGDYRm.js
   │        │  │     │  ├─ data-grid-overlay-editor.msYws2Ou.js
   │        │  │     │  ├─ downloader.kc14n2Hv.js
   │        │  │     │  ├─ es6.CxQz807-.js
   │        │  │     │  ├─ iframeResizer.contentWindow.B19u0ONI.js
   │        │  │     │  ├─ index.-5ruC9At.js
   │        │  │     │  ├─ index.8jhZBWF2.js
   │        │  │     │  ├─ index.9V1KdxfP.js
   │        │  │     │  ├─ index.BCx3C6e_.js
   │        │  │     │  ├─ index.BFz9U2y0.js
   │        │  │     │  ├─ index.BGga-hcS.js
   │        │  │     │  ├─ index.BHGGDa8K.js
   │        │  │     │  ├─ index.BHXxWdde.js
   │        │  │     │  ├─ index.BRXmLIsC.js
   │        │  │     │  ├─ index.BRuTz_S4.js
   │        │  │     │  ├─ index.Bcru_ti-.js
   │        │  │     │  ├─ index.Bl1FMJRd.js
   │        │  │     │  ├─ index.BoigZiu7.js
   │        │  │     │  ├─ index.BpILzHf_.js
   │        │  │     │  ├─ index.BqfdT8-Q.js
   │        │  │     │  ├─ index.C1z8KpLA.js
   │        │  │     │  ├─ index.C32I2PUe.js
   │        │  │     │  ├─ index.C5GnDRB7.js
   │        │  │     │  ├─ index.CG4qPaaW.js
   │        │  │     │  ├─ index.C_msmT1u.js
   │        │  │     │  ├─ index.CbeNTdd6.js
   │        │  │     │  ├─ index.CmTAF0dM.js
   │        │  │     │  ├─ index.CnGQVJcw.js
   │        │  │     │  ├─ index.CopVVq4l.js
   │        │  │     │  ├─ index.CtXupx4d.js
   │        │  │     │  ├─ index.DGmCchO7.js
   │        │  │     │  ├─ index.DH6zBk0e.js
   │        │  │     │  ├─ index.DHVlVWsm.js
   │        │  │     │  ├─ index.DRKIVBoi.js
   │        │  │     │  ├─ index.DUd-lFXx.js
   │        │  │     │  ├─ index.D_uRBA4B.js
   │        │  │     │  ├─ index.DeB9iKFW.js
   │        │  │     │  ├─ index.LaIasviC.js
   │        │  │     │  ├─ index.QHNfgPJd.js
   │        │  │     │  ├─ index.a-RJocYL.js
   │        │  │     │  ├─ index.cvz4B1gy.js
   │        │  │     │  ├─ index.t--hEgTQ.js
   │        │  │     │  ├─ index.xNQq3Ei5.js
   │        │  │     │  ├─ input.DsCfafm0.js
   │        │  │     │  ├─ inputUtils.CQWz5UKz.js
   │        │  │     │  ├─ memory.nY_lMTtu.js
   │        │  │     │  ├─ mergeWith.B_7zmsM4.js
   │        │  │     │  ├─ number-overlay-editor.CSeVhHRU.js
   │        │  │     │  ├─ possibleConstructorReturn.nNhsvgRd.js
   │        │  │     │  ├─ sandbox.Cgm3iuL6.js
   │        │  │     │  ├─ sprintf.D7DtBTRn.js
   │        │  │     │  ├─ textarea.BR8rlyih.js
   │        │  │     │  ├─ threshold.DjX0wlsa.js
   │        │  │     │  ├─ timepicker.w4XhAenH.js
   │        │  │     │  ├─ timer.CAwTRJ_g.js
   │        │  │     │  ├─ toConsumableArray.CgkEPBwD.js
   │        │  │     │  ├─ uniqueId.j-1rlNNH.js
   │        │  │     │  ├─ useBasicWidgetState.zXY9CjFS.js
   │        │  │     │  ├─ useOnInputChange.z04u96A8.js
   │        │  │     │  ├─ value.CgPGBV_l.js
   │        │  │     │  └─ withFullScreenWrapper.Ov13692o.js
   │        │  │     └─ media
   │        │  │        ├─ KaTeX_AMS-Regular.BQhdFMY1.woff2
   │        │  │        ├─ KaTeX_AMS-Regular.DMm9YOAa.woff
   │        │  │        ├─ KaTeX_AMS-Regular.DRggAlZN.ttf
   │        │  │        ├─ KaTeX_Caligraphic-Bold.ATXxdsX0.ttf
   │        │  │        ├─ KaTeX_Caligraphic-Bold.BEiXGLvX.woff
   │        │  │        ├─ KaTeX_Caligraphic-Bold.Dq_IR9rO.woff2
   │        │  │        ├─ KaTeX_Caligraphic-Regular.CTRA-rTL.woff
   │        │  │        ├─ KaTeX_Caligraphic-Regular.Di6jR-x-.woff2
   │        │  │        ├─ KaTeX_Caligraphic-Regular.wX97UBjC.ttf
   │        │  │        ├─ KaTeX_Fraktur-Bold.BdnERNNW.ttf
   │        │  │        ├─ KaTeX_Fraktur-Bold.BsDP51OF.woff
   │        │  │        ├─ KaTeX_Fraktur-Bold.CL6g_b3V.woff2
   │        │  │        ├─ KaTeX_Fraktur-Regular.CB_wures.ttf
   │        │  │        ├─ KaTeX_Fraktur-Regular.CTYiF6lA.woff2
   │        │  │        ├─ KaTeX_Fraktur-Regular.Dxdc4cR9.woff
   │        │  │        ├─ KaTeX_Main-Bold.Cx986IdX.woff2
   │        │  │        ├─ KaTeX_Main-Bold.Jm3AIy58.woff
   │        │  │        ├─ KaTeX_Main-Bold.waoOVXN0.ttf
   │        │  │        ├─ KaTeX_Main-BoldItalic.DxDJ3AOS.woff2
   │        │  │        ├─ KaTeX_Main-BoldItalic.DzxPMmG6.ttf
   │        │  │        ├─ KaTeX_Main-BoldItalic.SpSLRI95.woff
   │        │  │        ├─ KaTeX_Main-Italic.3WenGoN9.ttf
   │        │  │        ├─ KaTeX_Main-Italic.BMLOBm91.woff
   │        │  │        ├─ KaTeX_Main-Italic.NWA7e6Wa.woff2
   │        │  │        ├─ KaTeX_Main-Regular.B22Nviop.woff2
   │        │  │        ├─ KaTeX_Main-Regular.Dr94JaBh.woff
   │        │  │        ├─ KaTeX_Main-Regular.ypZvNtVU.ttf
   │        │  │        ├─ KaTeX_Math-BoldItalic.B3XSjfu4.ttf
   │        │  │        ├─ KaTeX_Math-BoldItalic.CZnvNsCZ.woff2
   │        │  │        ├─ KaTeX_Math-BoldItalic.iY-2wyZ7.woff
   │        │  │        ├─ KaTeX_Math-Italic.DA0__PXp.woff
   │        │  │        ├─ KaTeX_Math-Italic.flOr_0UB.ttf
   │        │  │        ├─ KaTeX_Math-Italic.t53AETM-.woff2
   │        │  │        ├─ KaTeX_SansSerif-Bold.CFMepnvq.ttf
   │        │  │        ├─ KaTeX_SansSerif-Bold.D1sUS0GD.woff2
   │        │  │        ├─ KaTeX_SansSerif-Bold.DbIhKOiC.woff
   │        │  │        ├─ KaTeX_SansSerif-Italic.C3H0VqGB.woff2
   │        │  │        ├─ KaTeX_SansSerif-Italic.DN2j7dab.woff
   │        │  │        ├─ KaTeX_SansSerif-Italic.YYjJ1zSn.ttf
   │        │  │        ├─ KaTeX_SansSerif-Regular.BNo7hRIc.ttf
   │        │  │        ├─ KaTeX_SansSerif-Regular.CS6fqUqJ.woff
   │        │  │        ├─ KaTeX_SansSerif-Regular.DDBCnlJ7.woff2
   │        │  │        ├─ KaTeX_Script-Regular.C5JkGWo-.ttf
   │        │  │        ├─ KaTeX_Script-Regular.D3wIWfF6.woff2
   │        │  │        ├─ KaTeX_Script-Regular.D5yQViql.woff
   │        │  │        ├─ KaTeX_Size1-Regular.C195tn64.woff
   │        │  │        ├─ KaTeX_Size1-Regular.Dbsnue_I.ttf
   │        │  │        ├─ KaTeX_Size1-Regular.mCD8mA8B.woff2
   │        │  │        ├─ KaTeX_Size2-Regular.B7gKUWhC.ttf
   │        │  │        ├─ KaTeX_Size2-Regular.Dy4dx90m.woff2
   │        │  │        ├─ KaTeX_Size2-Regular.oD1tc_U0.woff
   │        │  │        ├─ KaTeX_Size3-Regular.CTq5MqoE.woff
   │        │  │        ├─ KaTeX_Size3-Regular.DgpXs0kz.ttf
   │        │  │        ├─ KaTeX_Size4-Regular.BF-4gkZK.woff
   │        │  │        ├─ KaTeX_Size4-Regular.DWFBv043.ttf
   │        │  │        ├─ KaTeX_Size4-Regular.Dl5lxZxV.woff2
   │        │  │        ├─ KaTeX_Typewriter-Regular.C0xS9mPB.woff
   │        │  │        ├─ KaTeX_Typewriter-Regular.CO6r4hn1.woff2
   │        │  │        ├─ KaTeX_Typewriter-Regular.D3Ib7_Hf.ttf
   │        │  │        ├─ MaterialSymbols-Rounded.DsbC8sYI.woff2
   │        │  │        ├─ SourceCodePro-Bold.CFEfr7-q.woff2
   │        │  │        ├─ SourceCodePro-BoldItalic.C-LkFXxa.woff2
   │        │  │        ├─ SourceCodePro-Italic.CxFOx7N-.woff2
   │        │  │        ├─ SourceCodePro-Regular.CBOlD63d.woff2
   │        │  │        ├─ SourceCodePro-SemiBold.CFHwW3Wd.woff2
   │        │  │        ├─ SourceCodePro-SemiBoldItalic.Cg2yRu82.woff2
   │        │  │        ├─ SourceSansPro-Bold.-6c9oR8J.woff2
   │        │  │        ├─ SourceSansPro-BoldItalic.DmM_grLY.woff2
   │        │  │        ├─ SourceSansPro-Italic.I1ipWe7Q.woff2
   │        │  │        ├─ SourceSansPro-Regular.DZLUzqI4.woff2
   │        │  │        ├─ SourceSansPro-SemiBold.sKQIyTMz.woff2
   │        │  │        ├─ SourceSansPro-SemiBoldItalic.C0wP0icr.woff2
   │        │  │        ├─ SourceSerifPro-Bold.8TUnKj4x.woff2
   │        │  │        ├─ SourceSerifPro-BoldItalic.CBVO7Ve7.woff2
   │        │  │        ├─ SourceSerifPro-Italic.DkFgL2HZ.woff2
   │        │  │        ├─ SourceSerifPro-Regular.CNJNET2S.woff2
   │        │  │        ├─ SourceSerifPro-SemiBold.CHyh9GC5.woff2
   │        │  │        ├─ SourceSerifPro-SemiBoldItalic.CBtz8sWN.woff2
   │        │  │        ├─ balloon-0.Czj7AKwE.png
   │        │  │        ├─ balloon-1.CNvFFrND.png
   │        │  │        ├─ balloon-2.DTvC6B1t.png
   │        │  │        ├─ balloon-3.CgSk4tbL.png
   │        │  │        ├─ balloon-4.mbtFrzxf.png
   │        │  │        ├─ balloon-5.CSwkUfRA.png
   │        │  │        ├─ fireworks.B4d-_KUe.gif
   │        │  │        ├─ flake-0.DgWaVvm5.png
   │        │  │        ├─ flake-1.B2r5AHMK.png
   │        │  │        ├─ flake-2.BnWSExPC.png
   │        │  │        └─ snowflake.JU2jBHL8.svg
   │        │  ├─ string_util.py
   │        │  ├─ temporary_directory.py
   │        │  ├─ testing
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  └─ v1
   │        │  │     ├─ __init__.py
   │        │  │     ├─ __pycache__
   │        │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │     │  ├─ app_test.cpython-311.pyc
   │        │  │     │  ├─ element_tree.cpython-311.pyc
   │        │  │     │  ├─ local_script_runner.cpython-311.pyc
   │        │  │     │  └─ util.cpython-311.pyc
   │        │  │     ├─ app_test.py
   │        │  │     ├─ element_tree.py
   │        │  │     ├─ local_script_runner.py
   │        │  │     └─ util.py
   │        │  ├─ time_util.py
   │        │  ├─ type_util.py
   │        │  ├─ url_util.py
   │        │  ├─ user_info.py
   │        │  ├─ util.py
   │        │  ├─ vendor
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  └─ pympler
   │        │  │     ├─ __init__.py
   │        │  │     ├─ __pycache__
   │        │  │     │  ├─ __init__.cpython-311.pyc
   │        │  │     │  └─ asizeof.cpython-311.pyc
   │        │  │     └─ asizeof.py
   │        │  ├─ version.py
   │        │  ├─ watcher
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ event_based_path_watcher.cpython-311.pyc
   │        │  │  │  ├─ folder_black_list.cpython-311.pyc
   │        │  │  │  ├─ local_sources_watcher.cpython-311.pyc
   │        │  │  │  ├─ path_watcher.cpython-311.pyc
   │        │  │  │  ├─ polling_path_watcher.cpython-311.pyc
   │        │  │  │  └─ util.cpython-311.pyc
   │        │  │  ├─ event_based_path_watcher.py
   │        │  │  ├─ folder_black_list.py
   │        │  │  ├─ local_sources_watcher.py
   │        │  │  ├─ path_watcher.py
   │        │  │  ├─ polling_path_watcher.py
   │        │  │  └─ util.py
   │        │  └─ web
   │        │     ├─ __init__.py
   │        │     ├─ __pycache__
   │        │     │  ├─ __init__.cpython-311.pyc
   │        │     │  ├─ bootstrap.cpython-311.pyc
   │        │     │  ├─ cache_storage_manager_config.cpython-311.pyc
   │        │     │  └─ cli.cpython-311.pyc
   │        │     ├─ bootstrap.py
   │        │     ├─ cache_storage_manager_config.py
   │        │     ├─ cli.py
   │        │     └─ server
   │        │        ├─ __init__.py
   │        │        ├─ __pycache__
   │        │        │  ├─ __init__.cpython-311.pyc
   │        │        │  ├─ app_static_file_handler.cpython-311.pyc
   │        │        │  ├─ authlib_tornado_integration.cpython-311.pyc
   │        │        │  ├─ browser_websocket_handler.cpython-311.pyc
   │        │        │  ├─ component_request_handler.cpython-311.pyc
   │        │        │  ├─ media_file_handler.cpython-311.pyc
   │        │        │  ├─ oauth_authlib_routes.cpython-311.pyc
   │        │        │  ├─ oidc_mixin.cpython-311.pyc
   │        │        │  ├─ routes.cpython-311.pyc
   │        │        │  ├─ server.cpython-311.pyc
   │        │        │  ├─ server_util.cpython-311.pyc
   │        │        │  ├─ stats_request_handler.cpython-311.pyc
   │        │        │  ├─ upload_file_request_handler.cpython-311.pyc
   │        │        │  └─ websocket_headers.cpython-311.pyc
   │        │        ├─ app_static_file_handler.py
   │        │        ├─ authlib_tornado_integration.py
   │        │        ├─ browser_websocket_handler.py
   │        │        ├─ component_request_handler.py
   │        │        ├─ media_file_handler.py
   │        │        ├─ oauth_authlib_routes.py
   │        │        ├─ oidc_mixin.py
   │        │        ├─ routes.py
   │        │        ├─ server.py
   │        │        ├─ server_util.py
   │        │        ├─ stats_request_handler.py
   │        │        ├─ upload_file_request_handler.py
   │        │        └─ websocket_headers.py
   │        ├─ streamlit-1.45.1.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  ├─ entry_points.txt
   │        │  └─ top_level.txt
   │        ├─ tenacity
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ _utils.cpython-311.pyc
   │        │  │  ├─ after.cpython-311.pyc
   │        │  │  ├─ before.cpython-311.pyc
   │        │  │  ├─ before_sleep.cpython-311.pyc
   │        │  │  ├─ nap.cpython-311.pyc
   │        │  │  ├─ retry.cpython-311.pyc
   │        │  │  ├─ stop.cpython-311.pyc
   │        │  │  ├─ tornadoweb.cpython-311.pyc
   │        │  │  └─ wait.cpython-311.pyc
   │        │  ├─ _utils.py
   │        │  ├─ after.py
   │        │  ├─ asyncio
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  └─ retry.cpython-311.pyc
   │        │  │  └─ retry.py
   │        │  ├─ before.py
   │        │  ├─ before_sleep.py
   │        │  ├─ nap.py
   │        │  ├─ py.typed
   │        │  ├─ retry.py
   │        │  ├─ stop.py
   │        │  ├─ tornadoweb.py
   │        │  └─ wait.py
   │        ├─ tenacity-9.1.2.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  ├─ licenses
   │        │  │  └─ LICENSE
   │        │  └─ top_level.txt
   │        ├─ toml
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ decoder.cpython-311.pyc
   │        │  │  ├─ encoder.cpython-311.pyc
   │        │  │  ├─ ordered.cpython-311.pyc
   │        │  │  └─ tz.cpython-311.pyc
   │        │  ├─ decoder.py
   │        │  ├─ encoder.py
   │        │  ├─ ordered.py
   │        │  └─ tz.py
   │        ├─ toml-0.10.2.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ LICENSE
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  └─ top_level.txt
   │        ├─ tornado
   │        │  ├─ __init__.py
   │        │  ├─ __init__.pyi
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ _locale_data.cpython-311.pyc
   │        │  │  ├─ auth.cpython-311.pyc
   │        │  │  ├─ autoreload.cpython-311.pyc
   │        │  │  ├─ concurrent.cpython-311.pyc
   │        │  │  ├─ curl_httpclient.cpython-311.pyc
   │        │  │  ├─ escape.cpython-311.pyc
   │        │  │  ├─ gen.cpython-311.pyc
   │        │  │  ├─ http1connection.cpython-311.pyc
   │        │  │  ├─ httpclient.cpython-311.pyc
   │        │  │  ├─ httpserver.cpython-311.pyc
   │        │  │  ├─ httputil.cpython-311.pyc
   │        │  │  ├─ ioloop.cpython-311.pyc
   │        │  │  ├─ iostream.cpython-311.pyc
   │        │  │  ├─ locale.cpython-311.pyc
   │        │  │  ├─ locks.cpython-311.pyc
   │        │  │  ├─ log.cpython-311.pyc
   │        │  │  ├─ netutil.cpython-311.pyc
   │        │  │  ├─ options.cpython-311.pyc
   │        │  │  ├─ process.cpython-311.pyc
   │        │  │  ├─ queues.cpython-311.pyc
   │        │  │  ├─ routing.cpython-311.pyc
   │        │  │  ├─ simple_httpclient.cpython-311.pyc
   │        │  │  ├─ tcpclient.cpython-311.pyc
   │        │  │  ├─ tcpserver.cpython-311.pyc
   │        │  │  ├─ template.cpython-311.pyc
   │        │  │  ├─ testing.cpython-311.pyc
   │        │  │  ├─ util.cpython-311.pyc
   │        │  │  ├─ web.cpython-311.pyc
   │        │  │  ├─ websocket.cpython-311.pyc
   │        │  │  └─ wsgi.cpython-311.pyc
   │        │  ├─ _locale_data.py
   │        │  ├─ auth.py
   │        │  ├─ autoreload.py
   │        │  ├─ concurrent.py
   │        │  ├─ curl_httpclient.py
   │        │  ├─ escape.py
   │        │  ├─ gen.py
   │        │  ├─ http1connection.py
   │        │  ├─ httpclient.py
   │        │  ├─ httpserver.py
   │        │  ├─ httputil.py
   │        │  ├─ ioloop.py
   │        │  ├─ iostream.py
   │        │  ├─ locale.py
   │        │  ├─ locks.py
   │        │  ├─ log.py
   │        │  ├─ netutil.py
   │        │  ├─ options.py
   │        │  ├─ platform
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ asyncio.cpython-311.pyc
   │        │  │  │  ├─ caresresolver.cpython-311.pyc
   │        │  │  │  └─ twisted.cpython-311.pyc
   │        │  │  ├─ asyncio.py
   │        │  │  ├─ caresresolver.py
   │        │  │  └─ twisted.py
   │        │  ├─ process.py
   │        │  ├─ py.typed
   │        │  ├─ queues.py
   │        │  ├─ routing.py
   │        │  ├─ simple_httpclient.py
   │        │  ├─ speedups.abi3.so
   │        │  ├─ speedups.pyi
   │        │  ├─ tcpclient.py
   │        │  ├─ tcpserver.py
   │        │  ├─ template.py
   │        │  ├─ test
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __main__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ __main__.cpython-311.pyc
   │        │  │  │  ├─ asyncio_test.cpython-311.pyc
   │        │  │  │  ├─ auth_test.cpython-311.pyc
   │        │  │  │  ├─ autoreload_test.cpython-311.pyc
   │        │  │  │  ├─ circlerefs_test.cpython-311.pyc
   │        │  │  │  ├─ concurrent_test.cpython-311.pyc
   │        │  │  │  ├─ curl_httpclient_test.cpython-311.pyc
   │        │  │  │  ├─ escape_test.cpython-311.pyc
   │        │  │  │  ├─ gen_test.cpython-311.pyc
   │        │  │  │  ├─ http1connection_test.cpython-311.pyc
   │        │  │  │  ├─ httpclient_test.cpython-311.pyc
   │        │  │  │  ├─ httpserver_test.cpython-311.pyc
   │        │  │  │  ├─ httputil_test.cpython-311.pyc
   │        │  │  │  ├─ import_test.cpython-311.pyc
   │        │  │  │  ├─ ioloop_test.cpython-311.pyc
   │        │  │  │  ├─ iostream_test.cpython-311.pyc
   │        │  │  │  ├─ locale_test.cpython-311.pyc
   │        │  │  │  ├─ locks_test.cpython-311.pyc
   │        │  │  │  ├─ log_test.cpython-311.pyc
   │        │  │  │  ├─ netutil_test.cpython-311.pyc
   │        │  │  │  ├─ options_test.cpython-311.pyc
   │        │  │  │  ├─ process_test.cpython-311.pyc
   │        │  │  │  ├─ queues_test.cpython-311.pyc
   │        │  │  │  ├─ resolve_test_helper.cpython-311.pyc
   │        │  │  │  ├─ routing_test.cpython-311.pyc
   │        │  │  │  ├─ runtests.cpython-311.pyc
   │        │  │  │  ├─ simple_httpclient_test.cpython-311.pyc
   │        │  │  │  ├─ tcpclient_test.cpython-311.pyc
   │        │  │  │  ├─ tcpserver_test.cpython-311.pyc
   │        │  │  │  ├─ template_test.cpython-311.pyc
   │        │  │  │  ├─ testing_test.cpython-311.pyc
   │        │  │  │  ├─ twisted_test.cpython-311.pyc
   │        │  │  │  ├─ util.cpython-311.pyc
   │        │  │  │  ├─ util_test.cpython-311.pyc
   │        │  │  │  ├─ web_test.cpython-311.pyc
   │        │  │  │  ├─ websocket_test.cpython-311.pyc
   │        │  │  │  └─ wsgi_test.cpython-311.pyc
   │        │  │  ├─ asyncio_test.py
   │        │  │  ├─ auth_test.py
   │        │  │  ├─ autoreload_test.py
   │        │  │  ├─ circlerefs_test.py
   │        │  │  ├─ concurrent_test.py
   │        │  │  ├─ csv_translations
   │        │  │  │  └─ fr_FR.csv
   │        │  │  ├─ curl_httpclient_test.py
   │        │  │  ├─ escape_test.py
   │        │  │  ├─ gen_test.py
   │        │  │  ├─ gettext_translations
   │        │  │  │  └─ fr_FR
   │        │  │  │     └─ LC_MESSAGES
   │        │  │  │        ├─ tornado_test.mo
   │        │  │  │        └─ tornado_test.po
   │        │  │  ├─ http1connection_test.py
   │        │  │  ├─ httpclient_test.py
   │        │  │  ├─ httpserver_test.py
   │        │  │  ├─ httputil_test.py
   │        │  │  ├─ import_test.py
   │        │  │  ├─ ioloop_test.py
   │        │  │  ├─ iostream_test.py
   │        │  │  ├─ locale_test.py
   │        │  │  ├─ locks_test.py
   │        │  │  ├─ log_test.py
   │        │  │  ├─ netutil_test.py
   │        │  │  ├─ options_test.cfg
   │        │  │  ├─ options_test.py
   │        │  │  ├─ options_test_types.cfg
   │        │  │  ├─ options_test_types_str.cfg
   │        │  │  ├─ process_test.py
   │        │  │  ├─ queues_test.py
   │        │  │  ├─ resolve_test_helper.py
   │        │  │  ├─ routing_test.py
   │        │  │  ├─ runtests.py
   │        │  │  ├─ simple_httpclient_test.py
   │        │  │  ├─ static
   │        │  │  │  ├─ dir
   │        │  │  │  │  └─ index.html
   │        │  │  │  ├─ robots.txt
   │        │  │  │  ├─ sample.xml
   │        │  │  │  ├─ sample.xml.bz2
   │        │  │  │  └─ sample.xml.gz
   │        │  │  ├─ static_foo.txt
   │        │  │  ├─ tcpclient_test.py
   │        │  │  ├─ tcpserver_test.py
   │        │  │  ├─ template_test.py
   │        │  │  ├─ templates
   │        │  │  │  └─ utf8.html
   │        │  │  ├─ test.crt
   │        │  │  ├─ test.key
   │        │  │  ├─ testing_test.py
   │        │  │  ├─ twisted_test.py
   │        │  │  ├─ util.py
   │        │  │  ├─ util_test.py
   │        │  │  ├─ web_test.py
   │        │  │  ├─ websocket_test.py
   │        │  │  └─ wsgi_test.py
   │        │  ├─ testing.py
   │        │  ├─ util.py
   │        │  ├─ web.py
   │        │  ├─ websocket.py
   │        │  └─ wsgi.py
   │        ├─ tornado-6.5.1.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  ├─ licenses
   │        │  │  └─ LICENSE
   │        │  └─ top_level.txt
   │        ├─ typing_extensions-4.13.2.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  └─ licenses
   │        │     └─ LICENSE
   │        ├─ typing_extensions.py
   │        ├─ tzdata
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  └─ __init__.cpython-311.pyc
   │        │  ├─ zoneinfo
   │        │  │  ├─ Africa
   │        │  │  │  ├─ Abidjan
   │        │  │  │  ├─ Accra
   │        │  │  │  ├─ Addis_Ababa
   │        │  │  │  ├─ Algiers
   │        │  │  │  ├─ Asmara
   │        │  │  │  ├─ Asmera
   │        │  │  │  ├─ Bamako
   │        │  │  │  ├─ Bangui
   │        │  │  │  ├─ Banjul
   │        │  │  │  ├─ Bissau
   │        │  │  │  ├─ Blantyre
   │        │  │  │  ├─ Brazzaville
   │        │  │  │  ├─ Bujumbura
   │        │  │  │  ├─ Cairo
   │        │  │  │  ├─ Casablanca
   │        │  │  │  ├─ Ceuta
   │        │  │  │  ├─ Conakry
   │        │  │  │  ├─ Dakar
   │        │  │  │  ├─ Dar_es_Salaam
   │        │  │  │  ├─ Djibouti
   │        │  │  │  ├─ Douala
   │        │  │  │  ├─ El_Aaiun
   │        │  │  │  ├─ Freetown
   │        │  │  │  ├─ Gaborone
   │        │  │  │  ├─ Harare
   │        │  │  │  ├─ Johannesburg
   │        │  │  │  ├─ Juba
   │        │  │  │  ├─ Kampala
   │        │  │  │  ├─ Khartoum
   │        │  │  │  ├─ Kigali
   │        │  │  │  ├─ Kinshasa
   │        │  │  │  ├─ Lagos
   │        │  │  │  ├─ Libreville
   │        │  │  │  ├─ Lome
   │        │  │  │  ├─ Luanda
   │        │  │  │  ├─ Lubumbashi
   │        │  │  │  ├─ Lusaka
   │        │  │  │  ├─ Malabo
   │        │  │  │  ├─ Maputo
   │        │  │  │  ├─ Maseru
   │        │  │  │  ├─ Mbabane
   │        │  │  │  ├─ Mogadishu
   │        │  │  │  ├─ Monrovia
   │        │  │  │  ├─ Nairobi
   │        │  │  │  ├─ Ndjamena
   │        │  │  │  ├─ Niamey
   │        │  │  │  ├─ Nouakchott
   │        │  │  │  ├─ Ouagadougou
   │        │  │  │  ├─ Porto-Novo
   │        │  │  │  ├─ Sao_Tome
   │        │  │  │  ├─ Timbuktu
   │        │  │  │  ├─ Tripoli
   │        │  │  │  ├─ Tunis
   │        │  │  │  ├─ Windhoek
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ America
   │        │  │  │  ├─ Adak
   │        │  │  │  ├─ Anchorage
   │        │  │  │  ├─ Anguilla
   │        │  │  │  ├─ Antigua
   │        │  │  │  ├─ Araguaina
   │        │  │  │  ├─ Argentina
   │        │  │  │  │  ├─ Buenos_Aires
   │        │  │  │  │  ├─ Catamarca
   │        │  │  │  │  ├─ ComodRivadavia
   │        │  │  │  │  ├─ Cordoba
   │        │  │  │  │  ├─ Jujuy
   │        │  │  │  │  ├─ La_Rioja
   │        │  │  │  │  ├─ Mendoza
   │        │  │  │  │  ├─ Rio_Gallegos
   │        │  │  │  │  ├─ Salta
   │        │  │  │  │  ├─ San_Juan
   │        │  │  │  │  ├─ San_Luis
   │        │  │  │  │  ├─ Tucuman
   │        │  │  │  │  ├─ Ushuaia
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  └─ __pycache__
   │        │  │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  │  ├─ Aruba
   │        │  │  │  ├─ Asuncion
   │        │  │  │  ├─ Atikokan
   │        │  │  │  ├─ Atka
   │        │  │  │  ├─ Bahia
   │        │  │  │  ├─ Bahia_Banderas
   │        │  │  │  ├─ Barbados
   │        │  │  │  ├─ Belem
   │        │  │  │  ├─ Belize
   │        │  │  │  ├─ Blanc-Sablon
   │        │  │  │  ├─ Boa_Vista
   │        │  │  │  ├─ Bogota
   │        │  │  │  ├─ Boise
   │        │  │  │  ├─ Buenos_Aires
   │        │  │  │  ├─ Cambridge_Bay
   │        │  │  │  ├─ Campo_Grande
   │        │  │  │  ├─ Cancun
   │        │  │  │  ├─ Caracas
   │        │  │  │  ├─ Catamarca
   │        │  │  │  ├─ Cayenne
   │        │  │  │  ├─ Cayman
   │        │  │  │  ├─ Chicago
   │        │  │  │  ├─ Chihuahua
   │        │  │  │  ├─ Ciudad_Juarez
   │        │  │  │  ├─ Coral_Harbour
   │        │  │  │  ├─ Cordoba
   │        │  │  │  ├─ Costa_Rica
   │        │  │  │  ├─ Coyhaique
   │        │  │  │  ├─ Creston
   │        │  │  │  ├─ Cuiaba
   │        │  │  │  ├─ Curacao
   │        │  │  │  ├─ Danmarkshavn
   │        │  │  │  ├─ Dawson
   │        │  │  │  ├─ Dawson_Creek
   │        │  │  │  ├─ Denver
   │        │  │  │  ├─ Detroit
   │        │  │  │  ├─ Dominica
   │        │  │  │  ├─ Edmonton
   │        │  │  │  ├─ Eirunepe
   │        │  │  │  ├─ El_Salvador
   │        │  │  │  ├─ Ensenada
   │        │  │  │  ├─ Fort_Nelson
   │        │  │  │  ├─ Fort_Wayne
   │        │  │  │  ├─ Fortaleza
   │        │  │  │  ├─ Glace_Bay
   │        │  │  │  ├─ Godthab
   │        │  │  │  ├─ Goose_Bay
   │        │  │  │  ├─ Grand_Turk
   │        │  │  │  ├─ Grenada
   │        │  │  │  ├─ Guadeloupe
   │        │  │  │  ├─ Guatemala
   │        │  │  │  ├─ Guayaquil
   │        │  │  │  ├─ Guyana
   │        │  │  │  ├─ Halifax
   │        │  │  │  ├─ Havana
   │        │  │  │  ├─ Hermosillo
   │        │  │  │  ├─ Indiana
   │        │  │  │  │  ├─ Indianapolis
   │        │  │  │  │  ├─ Knox
   │        │  │  │  │  ├─ Marengo
   │        │  │  │  │  ├─ Petersburg
   │        │  │  │  │  ├─ Tell_City
   │        │  │  │  │  ├─ Vevay
   │        │  │  │  │  ├─ Vincennes
   │        │  │  │  │  ├─ Winamac
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  └─ __pycache__
   │        │  │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  │  ├─ Indianapolis
   │        │  │  │  ├─ Inuvik
   │        │  │  │  ├─ Iqaluit
   │        │  │  │  ├─ Jamaica
   │        │  │  │  ├─ Jujuy
   │        │  │  │  ├─ Juneau
   │        │  │  │  ├─ Kentucky
   │        │  │  │  │  ├─ Louisville
   │        │  │  │  │  ├─ Monticello
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  └─ __pycache__
   │        │  │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  │  ├─ Knox_IN
   │        │  │  │  ├─ Kralendijk
   │        │  │  │  ├─ La_Paz
   │        │  │  │  ├─ Lima
   │        │  │  │  ├─ Los_Angeles
   │        │  │  │  ├─ Louisville
   │        │  │  │  ├─ Lower_Princes
   │        │  │  │  ├─ Maceio
   │        │  │  │  ├─ Managua
   │        │  │  │  ├─ Manaus
   │        │  │  │  ├─ Marigot
   │        │  │  │  ├─ Martinique
   │        │  │  │  ├─ Matamoros
   │        │  │  │  ├─ Mazatlan
   │        │  │  │  ├─ Mendoza
   │        │  │  │  ├─ Menominee
   │        │  │  │  ├─ Merida
   │        │  │  │  ├─ Metlakatla
   │        │  │  │  ├─ Mexico_City
   │        │  │  │  ├─ Miquelon
   │        │  │  │  ├─ Moncton
   │        │  │  │  ├─ Monterrey
   │        │  │  │  ├─ Montevideo
   │        │  │  │  ├─ Montreal
   │        │  │  │  ├─ Montserrat
   │        │  │  │  ├─ Nassau
   │        │  │  │  ├─ New_York
   │        │  │  │  ├─ Nipigon
   │        │  │  │  ├─ Nome
   │        │  │  │  ├─ Noronha
   │        │  │  │  ├─ North_Dakota
   │        │  │  │  │  ├─ Beulah
   │        │  │  │  │  ├─ Center
   │        │  │  │  │  ├─ New_Salem
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  └─ __pycache__
   │        │  │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  │  ├─ Nuuk
   │        │  │  │  ├─ Ojinaga
   │        │  │  │  ├─ Panama
   │        │  │  │  ├─ Pangnirtung
   │        │  │  │  ├─ Paramaribo
   │        │  │  │  ├─ Phoenix
   │        │  │  │  ├─ Port-au-Prince
   │        │  │  │  ├─ Port_of_Spain
   │        │  │  │  ├─ Porto_Acre
   │        │  │  │  ├─ Porto_Velho
   │        │  │  │  ├─ Puerto_Rico
   │        │  │  │  ├─ Punta_Arenas
   │        │  │  │  ├─ Rainy_River
   │        │  │  │  ├─ Rankin_Inlet
   │        │  │  │  ├─ Recife
   │        │  │  │  ├─ Regina
   │        │  │  │  ├─ Resolute
   │        │  │  │  ├─ Rio_Branco
   │        │  │  │  ├─ Rosario
   │        │  │  │  ├─ Santa_Isabel
   │        │  │  │  ├─ Santarem
   │        │  │  │  ├─ Santiago
   │        │  │  │  ├─ Santo_Domingo
   │        │  │  │  ├─ Sao_Paulo
   │        │  │  │  ├─ Scoresbysund
   │        │  │  │  ├─ Shiprock
   │        │  │  │  ├─ Sitka
   │        │  │  │  ├─ St_Barthelemy
   │        │  │  │  ├─ St_Johns
   │        │  │  │  ├─ St_Kitts
   │        │  │  │  ├─ St_Lucia
   │        │  │  │  ├─ St_Thomas
   │        │  │  │  ├─ St_Vincent
   │        │  │  │  ├─ Swift_Current
   │        │  │  │  ├─ Tegucigalpa
   │        │  │  │  ├─ Thule
   │        │  │  │  ├─ Thunder_Bay
   │        │  │  │  ├─ Tijuana
   │        │  │  │  ├─ Toronto
   │        │  │  │  ├─ Tortola
   │        │  │  │  ├─ Vancouver
   │        │  │  │  ├─ Virgin
   │        │  │  │  ├─ Whitehorse
   │        │  │  │  ├─ Winnipeg
   │        │  │  │  ├─ Yakutat
   │        │  │  │  ├─ Yellowknife
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ Antarctica
   │        │  │  │  ├─ Casey
   │        │  │  │  ├─ Davis
   │        │  │  │  ├─ DumontDUrville
   │        │  │  │  ├─ Macquarie
   │        │  │  │  ├─ Mawson
   │        │  │  │  ├─ McMurdo
   │        │  │  │  ├─ Palmer
   │        │  │  │  ├─ Rothera
   │        │  │  │  ├─ South_Pole
   │        │  │  │  ├─ Syowa
   │        │  │  │  ├─ Troll
   │        │  │  │  ├─ Vostok
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ Arctic
   │        │  │  │  ├─ Longyearbyen
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ Asia
   │        │  │  │  ├─ Aden
   │        │  │  │  ├─ Almaty
   │        │  │  │  ├─ Amman
   │        │  │  │  ├─ Anadyr
   │        │  │  │  ├─ Aqtau
   │        │  │  │  ├─ Aqtobe
   │        │  │  │  ├─ Ashgabat
   │        │  │  │  ├─ Ashkhabad
   │        │  │  │  ├─ Atyrau
   │        │  │  │  ├─ Baghdad
   │        │  │  │  ├─ Bahrain
   │        │  │  │  ├─ Baku
   │        │  │  │  ├─ Bangkok
   │        │  │  │  ├─ Barnaul
   │        │  │  │  ├─ Beirut
   │        │  │  │  ├─ Bishkek
   │        │  │  │  ├─ Brunei
   │        │  │  │  ├─ Calcutta
   │        │  │  │  ├─ Chita
   │        │  │  │  ├─ Choibalsan
   │        │  │  │  ├─ Chongqing
   │        │  │  │  ├─ Chungking
   │        │  │  │  ├─ Colombo
   │        │  │  │  ├─ Dacca
   │        │  │  │  ├─ Damascus
   │        │  │  │  ├─ Dhaka
   │        │  │  │  ├─ Dili
   │        │  │  │  ├─ Dubai
   │        │  │  │  ├─ Dushanbe
   │        │  │  │  ├─ Famagusta
   │        │  │  │  ├─ Gaza
   │        │  │  │  ├─ Harbin
   │        │  │  │  ├─ Hebron
   │        │  │  │  ├─ Ho_Chi_Minh
   │        │  │  │  ├─ Hong_Kong
   │        │  │  │  ├─ Hovd
   │        │  │  │  ├─ Irkutsk
   │        │  │  │  ├─ Istanbul
   │        │  │  │  ├─ Jakarta
   │        │  │  │  ├─ Jayapura
   │        │  │  │  ├─ Jerusalem
   │        │  │  │  ├─ Kabul
   │        │  │  │  ├─ Kamchatka
   │        │  │  │  ├─ Karachi
   │        │  │  │  ├─ Kashgar
   │        │  │  │  ├─ Kathmandu
   │        │  │  │  ├─ Katmandu
   │        │  │  │  ├─ Khandyga
   │        │  │  │  ├─ Kolkata
   │        │  │  │  ├─ Krasnoyarsk
   │        │  │  │  ├─ Kuala_Lumpur
   │        │  │  │  ├─ Kuching
   │        │  │  │  ├─ Kuwait
   │        │  │  │  ├─ Macao
   │        │  │  │  ├─ Macau
   │        │  │  │  ├─ Magadan
   │        │  │  │  ├─ Makassar
   │        │  │  │  ├─ Manila
   │        │  │  │  ├─ Muscat
   │        │  │  │  ├─ Nicosia
   │        │  │  │  ├─ Novokuznetsk
   │        │  │  │  ├─ Novosibirsk
   │        │  │  │  ├─ Omsk
   │        │  │  │  ├─ Oral
   │        │  │  │  ├─ Phnom_Penh
   │        │  │  │  ├─ Pontianak
   │        │  │  │  ├─ Pyongyang
   │        │  │  │  ├─ Qatar
   │        │  │  │  ├─ Qostanay
   │        │  │  │  ├─ Qyzylorda
   │        │  │  │  ├─ Rangoon
   │        │  │  │  ├─ Riyadh
   │        │  │  │  ├─ Saigon
   │        │  │  │  ├─ Sakhalin
   │        │  │  │  ├─ Samarkand
   │        │  │  │  ├─ Seoul
   │        │  │  │  ├─ Shanghai
   │        │  │  │  ├─ Singapore
   │        │  │  │  ├─ Srednekolymsk
   │        │  │  │  ├─ Taipei
   │        │  │  │  ├─ Tashkent
   │        │  │  │  ├─ Tbilisi
   │        │  │  │  ├─ Tehran
   │        │  │  │  ├─ Tel_Aviv
   │        │  │  │  ├─ Thimbu
   │        │  │  │  ├─ Thimphu
   │        │  │  │  ├─ Tokyo
   │        │  │  │  ├─ Tomsk
   │        │  │  │  ├─ Ujung_Pandang
   │        │  │  │  ├─ Ulaanbaatar
   │        │  │  │  ├─ Ulan_Bator
   │        │  │  │  ├─ Urumqi
   │        │  │  │  ├─ Ust-Nera
   │        │  │  │  ├─ Vientiane
   │        │  │  │  ├─ Vladivostok
   │        │  │  │  ├─ Yakutsk
   │        │  │  │  ├─ Yangon
   │        │  │  │  ├─ Yekaterinburg
   │        │  │  │  ├─ Yerevan
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ Atlantic
   │        │  │  │  ├─ Azores
   │        │  │  │  ├─ Bermuda
   │        │  │  │  ├─ Canary
   │        │  │  │  ├─ Cape_Verde
   │        │  │  │  ├─ Faeroe
   │        │  │  │  ├─ Faroe
   │        │  │  │  ├─ Jan_Mayen
   │        │  │  │  ├─ Madeira
   │        │  │  │  ├─ Reykjavik
   │        │  │  │  ├─ South_Georgia
   │        │  │  │  ├─ St_Helena
   │        │  │  │  ├─ Stanley
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ Australia
   │        │  │  │  ├─ ACT
   │        │  │  │  ├─ Adelaide
   │        │  │  │  ├─ Brisbane
   │        │  │  │  ├─ Broken_Hill
   │        │  │  │  ├─ Canberra
   │        │  │  │  ├─ Currie
   │        │  │  │  ├─ Darwin
   │        │  │  │  ├─ Eucla
   │        │  │  │  ├─ Hobart
   │        │  │  │  ├─ LHI
   │        │  │  │  ├─ Lindeman
   │        │  │  │  ├─ Lord_Howe
   │        │  │  │  ├─ Melbourne
   │        │  │  │  ├─ NSW
   │        │  │  │  ├─ North
   │        │  │  │  ├─ Perth
   │        │  │  │  ├─ Queensland
   │        │  │  │  ├─ South
   │        │  │  │  ├─ Sydney
   │        │  │  │  ├─ Tasmania
   │        │  │  │  ├─ Victoria
   │        │  │  │  ├─ West
   │        │  │  │  ├─ Yancowinna
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ Brazil
   │        │  │  │  ├─ Acre
   │        │  │  │  ├─ DeNoronha
   │        │  │  │  ├─ East
   │        │  │  │  ├─ West
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ CET
   │        │  │  ├─ CST6CDT
   │        │  │  ├─ Canada
   │        │  │  │  ├─ Atlantic
   │        │  │  │  ├─ Central
   │        │  │  │  ├─ Eastern
   │        │  │  │  ├─ Mountain
   │        │  │  │  ├─ Newfoundland
   │        │  │  │  ├─ Pacific
   │        │  │  │  ├─ Saskatchewan
   │        │  │  │  ├─ Yukon
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ Chile
   │        │  │  │  ├─ Continental
   │        │  │  │  ├─ EasterIsland
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ Cuba
   │        │  │  ├─ EET
   │        │  │  ├─ EST
   │        │  │  ├─ EST5EDT
   │        │  │  ├─ Egypt
   │        │  │  ├─ Eire
   │        │  │  ├─ Etc
   │        │  │  │  ├─ GMT
   │        │  │  │  ├─ GMT+0
   │        │  │  │  ├─ GMT+1
   │        │  │  │  ├─ GMT+10
   │        │  │  │  ├─ GMT+11
   │        │  │  │  ├─ GMT+12
   │        │  │  │  ├─ GMT+2
   │        │  │  │  ├─ GMT+3
   │        │  │  │  ├─ GMT+4
   │        │  │  │  ├─ GMT+5
   │        │  │  │  ├─ GMT+6
   │        │  │  │  ├─ GMT+7
   │        │  │  │  ├─ GMT+8
   │        │  │  │  ├─ GMT+9
   │        │  │  │  ├─ GMT-0
   │        │  │  │  ├─ GMT-1
   │        │  │  │  ├─ GMT-10
   │        │  │  │  ├─ GMT-11
   │        │  │  │  ├─ GMT-12
   │        │  │  │  ├─ GMT-13
   │        │  │  │  ├─ GMT-14
   │        │  │  │  ├─ GMT-2
   │        │  │  │  ├─ GMT-3
   │        │  │  │  ├─ GMT-4
   │        │  │  │  ├─ GMT-5
   │        │  │  │  ├─ GMT-6
   │        │  │  │  ├─ GMT-7
   │        │  │  │  ├─ GMT-8
   │        │  │  │  ├─ GMT-9
   │        │  │  │  ├─ GMT0
   │        │  │  │  ├─ Greenwich
   │        │  │  │  ├─ UCT
   │        │  │  │  ├─ UTC
   │        │  │  │  ├─ Universal
   │        │  │  │  ├─ Zulu
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ Europe
   │        │  │  │  ├─ Amsterdam
   │        │  │  │  ├─ Andorra
   │        │  │  │  ├─ Astrakhan
   │        │  │  │  ├─ Athens
   │        │  │  │  ├─ Belfast
   │        │  │  │  ├─ Belgrade
   │        │  │  │  ├─ Berlin
   │        │  │  │  ├─ Bratislava
   │        │  │  │  ├─ Brussels
   │        │  │  │  ├─ Bucharest
   │        │  │  │  ├─ Budapest
   │        │  │  │  ├─ Busingen
   │        │  │  │  ├─ Chisinau
   │        │  │  │  ├─ Copenhagen
   │        │  │  │  ├─ Dublin
   │        │  │  │  ├─ Gibraltar
   │        │  │  │  ├─ Guernsey
   │        │  │  │  ├─ Helsinki
   │        │  │  │  ├─ Isle_of_Man
   │        │  │  │  ├─ Istanbul
   │        │  │  │  ├─ Jersey
   │        │  │  │  ├─ Kaliningrad
   │        │  │  │  ├─ Kiev
   │        │  │  │  ├─ Kirov
   │        │  │  │  ├─ Kyiv
   │        │  │  │  ├─ Lisbon
   │        │  │  │  ├─ Ljubljana
   │        │  │  │  ├─ London
   │        │  │  │  ├─ Luxembourg
   │        │  │  │  ├─ Madrid
   │        │  │  │  ├─ Malta
   │        │  │  │  ├─ Mariehamn
   │        │  │  │  ├─ Minsk
   │        │  │  │  ├─ Monaco
   │        │  │  │  ├─ Moscow
   │        │  │  │  ├─ Nicosia
   │        │  │  │  ├─ Oslo
   │        │  │  │  ├─ Paris
   │        │  │  │  ├─ Podgorica
   │        │  │  │  ├─ Prague
   │        │  │  │  ├─ Riga
   │        │  │  │  ├─ Rome
   │        │  │  │  ├─ Samara
   │        │  │  │  ├─ San_Marino
   │        │  │  │  ├─ Sarajevo
   │        │  │  │  ├─ Saratov
   │        │  │  │  ├─ Simferopol
   │        │  │  │  ├─ Skopje
   │        │  │  │  ├─ Sofia
   │        │  │  │  ├─ Stockholm
   │        │  │  │  ├─ Tallinn
   │        │  │  │  ├─ Tirane
   │        │  │  │  ├─ Tiraspol
   │        │  │  │  ├─ Ulyanovsk
   │        │  │  │  ├─ Uzhgorod
   │        │  │  │  ├─ Vaduz
   │        │  │  │  ├─ Vatican
   │        │  │  │  ├─ Vienna
   │        │  │  │  ├─ Vilnius
   │        │  │  │  ├─ Volgograd
   │        │  │  │  ├─ Warsaw
   │        │  │  │  ├─ Zagreb
   │        │  │  │  ├─ Zaporozhye
   │        │  │  │  ├─ Zurich
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ Factory
   │        │  │  ├─ GB
   │        │  │  ├─ GB-Eire
   │        │  │  ├─ GMT
   │        │  │  ├─ GMT+0
   │        │  │  ├─ GMT-0
   │        │  │  ├─ GMT0
   │        │  │  ├─ Greenwich
   │        │  │  ├─ HST
   │        │  │  ├─ Hongkong
   │        │  │  ├─ Iceland
   │        │  │  ├─ Indian
   │        │  │  │  ├─ Antananarivo
   │        │  │  │  ├─ Chagos
   │        │  │  │  ├─ Christmas
   │        │  │  │  ├─ Cocos
   │        │  │  │  ├─ Comoro
   │        │  │  │  ├─ Kerguelen
   │        │  │  │  ├─ Mahe
   │        │  │  │  ├─ Maldives
   │        │  │  │  ├─ Mauritius
   │        │  │  │  ├─ Mayotte
   │        │  │  │  ├─ Reunion
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ Iran
   │        │  │  ├─ Israel
   │        │  │  ├─ Jamaica
   │        │  │  ├─ Japan
   │        │  │  ├─ Kwajalein
   │        │  │  ├─ Libya
   │        │  │  ├─ MET
   │        │  │  ├─ MST
   │        │  │  ├─ MST7MDT
   │        │  │  ├─ Mexico
   │        │  │  │  ├─ BajaNorte
   │        │  │  │  ├─ BajaSur
   │        │  │  │  ├─ General
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ NZ
   │        │  │  ├─ NZ-CHAT
   │        │  │  ├─ Navajo
   │        │  │  ├─ PRC
   │        │  │  ├─ PST8PDT
   │        │  │  ├─ Pacific
   │        │  │  │  ├─ Apia
   │        │  │  │  ├─ Auckland
   │        │  │  │  ├─ Bougainville
   │        │  │  │  ├─ Chatham
   │        │  │  │  ├─ Chuuk
   │        │  │  │  ├─ Easter
   │        │  │  │  ├─ Efate
   │        │  │  │  ├─ Enderbury
   │        │  │  │  ├─ Fakaofo
   │        │  │  │  ├─ Fiji
   │        │  │  │  ├─ Funafuti
   │        │  │  │  ├─ Galapagos
   │        │  │  │  ├─ Gambier
   │        │  │  │  ├─ Guadalcanal
   │        │  │  │  ├─ Guam
   │        │  │  │  ├─ Honolulu
   │        │  │  │  ├─ Johnston
   │        │  │  │  ├─ Kanton
   │        │  │  │  ├─ Kiritimati
   │        │  │  │  ├─ Kosrae
   │        │  │  │  ├─ Kwajalein
   │        │  │  │  ├─ Majuro
   │        │  │  │  ├─ Marquesas
   │        │  │  │  ├─ Midway
   │        │  │  │  ├─ Nauru
   │        │  │  │  ├─ Niue
   │        │  │  │  ├─ Norfolk
   │        │  │  │  ├─ Noumea
   │        │  │  │  ├─ Pago_Pago
   │        │  │  │  ├─ Palau
   │        │  │  │  ├─ Pitcairn
   │        │  │  │  ├─ Pohnpei
   │        │  │  │  ├─ Ponape
   │        │  │  │  ├─ Port_Moresby
   │        │  │  │  ├─ Rarotonga
   │        │  │  │  ├─ Saipan
   │        │  │  │  ├─ Samoa
   │        │  │  │  ├─ Tahiti
   │        │  │  │  ├─ Tarawa
   │        │  │  │  ├─ Tongatapu
   │        │  │  │  ├─ Truk
   │        │  │  │  ├─ Wake
   │        │  │  │  ├─ Wallis
   │        │  │  │  ├─ Yap
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ Poland
   │        │  │  ├─ Portugal
   │        │  │  ├─ ROC
   │        │  │  ├─ ROK
   │        │  │  ├─ Singapore
   │        │  │  ├─ Turkey
   │        │  │  ├─ UCT
   │        │  │  ├─ US
   │        │  │  │  ├─ Alaska
   │        │  │  │  ├─ Aleutian
   │        │  │  │  ├─ Arizona
   │        │  │  │  ├─ Central
   │        │  │  │  ├─ East-Indiana
   │        │  │  │  ├─ Eastern
   │        │  │  │  ├─ Hawaii
   │        │  │  │  ├─ Indiana-Starke
   │        │  │  │  ├─ Michigan
   │        │  │  │  ├─ Mountain
   │        │  │  │  ├─ Pacific
   │        │  │  │  ├─ Samoa
   │        │  │  │  ├─ __init__.py
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-311.pyc
   │        │  │  ├─ UTC
   │        │  │  ├─ Universal
   │        │  │  ├─ W-SU
   │        │  │  ├─ WET
   │        │  │  ├─ Zulu
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  └─ __init__.cpython-311.pyc
   │        │  │  ├─ iso3166.tab
   │        │  │  ├─ leapseconds
   │        │  │  ├─ tzdata.zi
   │        │  │  ├─ zone.tab
   │        │  │  ├─ zone1970.tab
   │        │  │  └─ zonenow.tab
   │        │  └─ zones
   │        ├─ tzdata-2025.2.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ METADATA
   │        │  ├─ RECORD
   │        │  ├─ REQUESTED
   │        │  ├─ WHEEL
   │        │  ├─ licenses
   │        │  │  ├─ LICENSE
   │        │  │  └─ licenses
   │        │  │     └─ LICENSE_APACHE
   │        │  └─ top_level.txt
   │        ├─ urllib3
   │        │  ├─ __init__.py
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-311.pyc
   │        │  │  ├─ _base_connection.cpython-311.pyc
   │        │  │  ├─ _collections.cpython-311.pyc
   │        │  │  ├─ _request_methods.cpython-311.pyc
   │        │  │  ├─ _version.cpython-311.pyc
   │        │  │  ├─ connection.cpython-311.pyc
   │        │  │  ├─ connectionpool.cpython-311.pyc
   │        │  │  ├─ exceptions.cpython-311.pyc
   │        │  │  ├─ fields.cpython-311.pyc
   │        │  │  ├─ filepost.cpython-311.pyc
   │        │  │  ├─ poolmanager.cpython-311.pyc
   │        │  │  └─ response.cpython-311.pyc
   │        │  ├─ _base_connection.py
   │        │  ├─ _collections.py
   │        │  ├─ _request_methods.py
   │        │  ├─ _version.py
   │        │  ├─ connection.py
   │        │  ├─ connectionpool.py
   │        │  ├─ contrib
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ pyopenssl.cpython-311.pyc
   │        │  │  │  └─ socks.cpython-311.pyc
   │        │  │  ├─ emscripten
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  │  ├─ connection.cpython-311.pyc
   │        │  │  │  │  ├─ fetch.cpython-311.pyc
   │        │  │  │  │  ├─ request.cpython-311.pyc
   │        │  │  │  │  └─ response.cpython-311.pyc
   │        │  │  │  ├─ connection.py
   │        │  │  │  ├─ emscripten_fetch_worker.js
   │        │  │  │  ├─ fetch.py
   │        │  │  │  ├─ request.py
   │        │  │  │  └─ response.py
   │        │  │  ├─ pyopenssl.py
   │        │  │  └─ socks.py
   │        │  ├─ exceptions.py
   │        │  ├─ fields.py
   │        │  ├─ filepost.py
   │        │  ├─ http2
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-311.pyc
   │        │  │  │  ├─ connection.cpython-311.pyc
   │        │  │  │  └─ probe.cpython-311.pyc
   │        │  │  ├─ connection.py
   │        │  │  └─ probe.py
   │        │  ├─ poolmanager.py
   │        │  ├─ py.typed
   │        │  ├─ response.py
   │        │  └─ util
   │        │     ├─ __init__.py
   │        │     ├─ __pycache__
   │        │     │  ├─ __init__.cpython-311.pyc
   │        │     │  ├─ connection.cpython-311.pyc
   │        │     │  ├─ proxy.cpython-311.pyc
   │        │     │  ├─ request.cpython-311.pyc
   │        │     │  ├─ response.cpython-311.pyc
   │        │     │  ├─ retry.cpython-311.pyc
   │        │     │  ├─ ssl_.cpython-311.pyc
   │        │     │  ├─ ssl_match_hostname.cpython-311.pyc
   │        │     │  ├─ ssltransport.cpython-311.pyc
   │        │     │  ├─ timeout.cpython-311.pyc
   │        │     │  ├─ url.cpython-311.pyc
   │        │     │  ├─ util.cpython-311.pyc
   │        │     │  └─ wait.cpython-311.pyc
   │        │     ├─ connection.py
   │        │     ├─ proxy.py
   │        │     ├─ request.py
   │        │     ├─ response.py
   │        │     ├─ retry.py
   │        │     ├─ ssl_.py
   │        │     ├─ ssl_match_hostname.py
   │        │     ├─ ssltransport.py
   │        │     ├─ timeout.py
   │        │     ├─ url.py
   │        │     ├─ util.py
   │        │     └─ wait.py
   │        └─ urllib3-2.4.0.dist-info
   │           ├─ INSTALLER
   │           ├─ METADATA
   │           ├─ RECORD
   │           ├─ REQUESTED
   │           ├─ WHEEL
   │           └─ licenses
   │              └─ LICENSE.txt
   ├─ pyvenv.cfg
   └─ share
      └─ jupyter
         └─ nbextensions
            └─ pydeck
               ├─ extensionRequires.js
               ├─ index.js
               └─ index.js.map

```