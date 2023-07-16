import { useRouter } from "next/router";
import Card  from "@/components/common/card";
import { handleGetEnvironment } from "@/utils/service/environment";

export async function getServerSideProps() {
    const request = {
        type: "get",
        url: "/environment/getEnvironments/"
    }
    const { success, data } = await  handleGetEnvironment(request);
    if (success) {
        return {
            props: {
                envs: data
            }
        }
    }
    return {
        props: {}
    }
}

export default function Dashboard({ envs }) {

    const router = useRouter();

    const createnewEnv = () => {
        router.push(`${process.env.NEXT_PUBLIC_HOST}/environments/create/`);
    }

    const handleClick = () => {

    }

    return <>
        <button type="button" onClick={createnewEnv}>
            create new environment
        </button>
        {
            envs.map((env, index) => (
                <Card key = {index} title={env.env_name} description="lol" handleClick={handleClick}/>
            ))
        }
    </>
}
