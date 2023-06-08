import { useRouter } from "next/router";

export default function Dashboard() {

    const router = useRouter();

    const createnewEnv = () => {
        router.push(`${process.env.NEXT_PUBLIC_HOST}/environments/create/`);
    }

    return <>
        <button type="button" onClick={createnewEnv}>
            create new environment
        </button>
    </>
}
