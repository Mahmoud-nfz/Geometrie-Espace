# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['esp.py'],
             pathex=['C:\\Users\\Mahmoud\\Desktop'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break
a.datas += [('balls.gif','C:\\Users\\Mahmoud\\Desktop\\balls.gif', 'Data')]
a.datas += [('space_icon.ico','C:\\Users\\Mahmoud\\Desktop\\space_icon.ico', 'Data')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='esp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='space_icon.ico')
