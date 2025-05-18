let
  nixpkgs = import <nixpkgs> {};
in nixpkgs.mkShell {
  packages = [
    (nixpkgs.python313Full.withPackages (pypkgs: with pypkgs; [
    ]))
  ];
  shellHook = ''
    fish --init-command="eval #(ssh-agent-c); ssh-add ~/.ssh/github"
    exit
  '';
}
