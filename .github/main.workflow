workflow "GitHub Action for pyup Safety" {
  on = "push"
  resolves = ["safety command"]
}

action "safety command" {
  uses = "cclauss/GitHub-Action-for-pyup-Safety-CI@master"
  args = "safety check --full-report"
}
