Technicalities underlying the fast-pace local workflow
======================================================

## 🔲 Clone the fork locally
- Clone the ``icub-tech-iit`` fork
  ```console
  git remote add icub-tech https://github.com/icub-tech-iit/robots-configuration.git
  ```
- Switch to the branch corresponding to the robot.

## 🔲 Set the default committer
- Fine-grained PAT can be scoped to work on a specified organization and only on a specified repository.
- To store credentials locally, one needs to issue the following, once the fork is cloned locally:
  ```console
  git config --local user.name "icub-tech-iit-bot"
  git config --local user.email "icub-tech@iit.it"
  git config --local credential.https://github.com/icub-tech-iit/robots-configuration.git.helper store
  ```
  ⚠️ Note the use of the option `--local` to avoid impacting Git globally on the system.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
- In order to push without password, the PAT needs to be provided. The credentials will be stored plainly under `~/.git-credentials`. No worries though, as this PAT has a very narrowed use and impacts a fork that is backed up anyhow by the upstream repository.
- The PAT can be stored manually in `~/.git-credentials` with the format `https://icub-tech-iit-bot:${PAT}@github`. Alternatively, when attempting to push the first time, it is enough to use `icub-tech-iit-bot` as user and specifying the `PAT` as password. This will be stored in the `~/.git-credentials` file automatically.
=======
- In order to push without password, the PAT needs to be provided. The credentials will be stored plainly under `~/.git-credentials` (the format is: `https://icub-tech-iit-bot:<PAT>@github`). No worries though, as this PAT has a very narrowed use and impacts a fork that is backed up anyhow by the upstream repository.
- The PAT can be stored manually in `~/.git-credentials` with the format `https://icub-tech-iit-bot:<PAT>@github`. Alternatively, when attempting to push the first time, it is enough to use `icub-tech-iit-bot` as user and specifying the `<PAT>` as password. These will be stored in the `~/.git-credentials` file automatically.
>>>>>>> 5570fc368 (Devel ergo cub sn001 (#660))
- ⚠️  Being the local system shared, no one else should store his/her PAT in the same file.
=======
- The first time there's a push, the PAT needs to be provided. The credentials will be stored plainly under `~/.git-credentials` (the format is: `https://icub-tech-iit-bot:<PAT>@github`). No worries though, as this PAT has a very narrowed use and impacts a fork that is backed up anyhow by the upstream repository. The PAT can be stored in `~/.git-credentials` upfront as well. Being the local system shared, no one else should store his/her PAT in the same file.
>>>>>>> fab4f646e (Minor modification to local-workflow-tech.md)
=======
- In order to push without password, the PAT needs to be provided. The credentials will be stored plainly under `~/.git-credentials` (the format is: `https://icub-tech-iit-bot:<PAT>@github`). No worries though, as this PAT has a very narrowed use and impacts a fork that is backed up anyhow by the upstream repository.
- The PAT can be stored manually in `~/.git-credentials` with the format `https://icub-tech-iit-bot:<PAT>@github`. Alternatively, when attempting to push the first time, it is enough to use `icub-tech-iit-bot` as user and specifying the `<PAT>` as password. These will be stored in the `~/.git-credentials` file automatically.
- ⚠️  Being the local system shared, no one else should store his/her PAT in the same file.
>>>>>>> b89000b2e (More info on the credentials storing for the local workflow documentation)
- ⌛ The PAT expires after **`1 year`** at the latest, thus needing to be regenerated.
- The upstream maintainer will take care of the PAT.

> [!tip]
> Instead of relying on the credential helper, one can resort to a simpler method:
> ```console
> git remote set-url icub-tech https://x-access-token:${PAT}@github.com/icub-tech-iit/robots-configuration.git
> ```

## 🔲 Ensure that the author information is specified explicitly at commit time
- We do rely on [Git hoooks](../.githooks).
<<<<<<< HEAD
<<<<<<< HEAD
- Run the following command from the `robots-configuration` root folder:
=======
- Run the following command  from the `robots-configuration` root folder:
>>>>>>> 89aa49b8c (Added more info to the local workflow md file)
=======
- Run the following command  from the `robots-configuration` root folder:
>>>>>>> 5570fc368 (Devel ergo cub sn001 (#660))
  ```console
  git config --local core.hooksPath .githooks/
  ```

## 🔲 Detect conflicts at push time and notify PIC

> [!note]
> To be still developed.
