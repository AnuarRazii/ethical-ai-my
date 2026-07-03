#!/bin/bash

set -e

REPO="AnuarRazii/ethical-ai-my"
BRANCH="main"

echo "Applying RZ1 branch protection..."

gh api \
  -X PUT \
  repos/$REPO/branches/$BRANCH/protection \
  -H "Accept: application/vnd.github+json" \
  -f required_status_checks.strict=true \
  -f enforce_admins=false \
  -f required_pull_request_reviews=null \
  -f restrictions=null \
  -f required_linear_history=false \
  -f allow_force_pushes=false \
  -f allow_deletions=false \
  -f block_creations=false \
  -f required_conversation_resolution=false \
  -f lock_branch=false \
  -f allow_fork_syncing=true \
  -f required_status_checks.contexts[]="RZ1 Validate" \
  -f required_status_checks.contexts[]="RZ1 Compliance Engine" \
  -f required_status_checks.contexts[]="CodeQL Analysis"

echo "Branch protection applied successfully."
