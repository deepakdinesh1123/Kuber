export async function upsertFile(db: any, path: string, content: string) {
    try {
        const id = await db.files.add({
            id: path,
            content
        });
    } catch(error) {
        const id = await db.files.update(path, { content: content});
    }
}

export async function readFile(db:any, path: string) {

}

export async function deleteFile(db:any, path: string) {

}