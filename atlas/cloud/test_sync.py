from sync_engine import SyncEngine


sync = SyncEngine()


print(
    sync.status(
        "atlas_workspace"
    )
)


print(
    sync.push(
        "atlas",
        "atlas_workspace/G-Unit-Backup"
    )
)