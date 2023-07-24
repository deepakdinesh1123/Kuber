import { useRouter } from "next/router";
import Card from "@/components/common/card";
import {
  handleGetEnvironment,
  handleCreateSandbox,
} from "@/utils/service/environment";
import { UUID } from "crypto";
import { JSON } from "@/types/common";

type Environment = {
  env_id: UUID;
  env_name: string;
  tag: string;
  config: JSON;
  images: Array<string>;
  creator: string;
  created_at: Date;
};

export async function getServerSideProps() {
  const request = {
    type: "get",
    url: "/environments/environment/",
  };
  const { success, data } = await handleGetEnvironment(request);
  if (success) {
    return {
      props: {
        envs: data,
      },
    };
  }
  return {
    props: {},
  };
}

export default function Dashboard({ envs }) {
  const createnewEnv = () => {
    router.push(`${process.env.NEXT_PUBLIC_HOST}/environments/create/`);
  };

  const createnewEnv = () => {
    router.push(`${process.env.NEXT_PUBLIC_HOST}/environments/create/`);
  };

  const handleClick = async (env_id: UUID) => {
    const request = {
      type: "post",
      url: `/environments/environment/${env_id}/sandbox/`,
    };
    const { success, data } = await handleCreateSandbox(request);
    if (success) {
      console.log("created");
    } else {
      console.log("Could not be created");
    }
  };

  return (
    <>
      <button type="button" onClick={createnewEnv}>
        create new environment
      </button>
      {envs.map((env, index) => (
        <Card
          key={env.env_id}
          title={env.env_name}
          description="lol"
          handleClick={() => handleClick(env.env_id)}
        />
      ))}
    </>
  );
}
