import fire
import commands


if __name__ == '__main__':
    fire.Fire({
        'issue': commands.issue,
    })
