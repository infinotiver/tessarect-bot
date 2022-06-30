{ pkgs }: {
  deps = [
    pkgs.python39Full
    pkgs.python39Packages.poetry.out
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      pkgs.glib
      pkgs.xorg.libX11
    ];
    PYTHONBIN = "${pkgs.python39Full}/bin/python3.9";
    LANG = "en_US.UTF-8";
  };
}