{ pkgs ? import (builtins.fetchTarball {
  name = "nixpkgs-unstable";
  url =
    "https://github.com/nixos/nixpkgs/archive/de679c57ca579974f35fab5444c7892ceb16230a.tar.gz"; # as of 6 september 2020
  sha256 = "0xhw2k33zxcxvqm83mch9izkxlxhfc6q6qsijky58qzn8x9854w0";
}) { }, naersk ? pkgs.fetchFromGitHub {
  owner = "nmattia";
  repo = "naersk";
  rev = "529e910a3f423a8211f8739290014b754b2555b6";
  sha256 = "3pDN/W17wjVDbrkgo60xQSb24+QAPQ7ulsUq5atNni0=";
} }:

let
  src = ./.;

  py-package = pkgs.python3Packages;

  naersk-lib = pkgs.callPackage naersk { };

  # only depend on the rust section, so no recompilation on the python side change
  portmod-rust-srcs = {
    cargo-toml = ./Cargo.toml;
    cargo-lock = ./Cargo.lock;
    rust-src = ./src;
    locales = ./l10n;
  };

  portmod-rust-src = pkgs.stdenv.mkDerivation {
    name = "portmod-src-git";
    src = portmod-rust-srcs.rust-src;
    installPhase = ''
      mkdir $out
      cp ${portmod-rust-srcs.cargo-toml} $out/Cargo.toml
      cp ${portmod-rust-srcs.cargo-lock} $out/Cargo.lock
      cp -rf ${portmod-rust-srcs.rust-src} $out/src
      cp -rf ${portmod-rust-srcs.locales} $out/l10n
    '';
    noAuditTmpdir = true;
  };

  portmod-rust = naersk-lib.buildPackage {
    src = portmod-rust-src;
    buildInputs = [ py-package.python ];
    copyLibs = true;
  };

  fasteners_portmod = py-package.buildPythonPackage rec {
    pname = "fasteners";
    version = "0.16";

    src = py-package.fetchPypi {
      inherit pname version;
      sha256 = "sha256-yZXYwmsBfF1qbemtKaD5zdV95hrhET0o+sJmIrBqCTM=";
    };

    propagatedBuildInputs = with py-package; [
      six
      monotonic
      more-itertools
      diskcache
    ];

    doCheck = false;
  };

  bin-program = with pkgs; [
    bubblewrap
    git
    py-package.virtualenv
    tr-patcher
    tes3cmd
    imagemagick
  ];
in py-package.buildPythonApplication rec {
  inherit src;
  pname = "portmod";

  version = "git"; # TODO: dynamically find the version

  prePatch = ''
    echo patching setup.py to make him not compile the rust library
    substituteInPlace setup.py \
    	--replace "from setuptools_rust import Binding, RustExtension" "" \
    	--replace "RustExtension(\"portmod.portmod\", binding=Binding.PyO3, strip=True)" ""
  '';

  SETUPTOOLS_SCM_PRETEND_VERSION = version;

  propagatedBuildInputs = with py-package; [
    setuptools_scm
    setuptools
    requests
    chardet
    colorama
    restrictedpython
    appdirs
    GitPython
    progressbar2
    python-sat
    redbaron
    patool
    packaging
    fasteners_portmod
  ];

  nativeBuildInputs = bin-program ++ [ py-package.pytest py-package.black ];

  doCheck = false; # python doesn't seem to have access to example repo ...

  postInstall = ''
    cp ${portmod-rust}/lib/libportmod.so $(echo $out/lib/python*/*/portmod)/portmod.so
    for script in $out/bin/*
    do
    	wrapProgram $script \
    		--prefix PATH : ${pkgs.lib.makeBinPath bin-program} \
    		--prefix GIT_SSL_CAINFO : ${pkgs.cacert}/etc/ssl/certs/ca-bundle.crt
    done
  '';

  shellHook = ''
    cp ${portmod-rust}/lib/libportmod.so portmod/portmod.so
    chmod +w portmod/portmod.so
  '';
}
