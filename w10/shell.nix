let
  nixpkgs = import <nixpkgs> {};
in nixpkgs.mkShell {
  packages = [
    (nixpkgs.python313Full.withPackages (pypkgs: with pypkgs; [
      flask
    ]))
    nixpkgs.python313Packages.flask
  ];
  shellHook = ''
    fish --init-command="eval $(ssh-agent -c); ssh-add ~/.ssh/github"
    exit
  '';
}
