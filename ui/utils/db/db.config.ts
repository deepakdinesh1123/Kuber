import Dexie, { Table } from "dexie";

export interface File {
    id?: string
    content: string
};

export class Files extends Dexie {

    files!: Table<File>;

    constructor() {
        super('Kuber-DB');
        this.version(1).stores({
            files: 'id, content'
        });
    }
}
export const db = new Files();