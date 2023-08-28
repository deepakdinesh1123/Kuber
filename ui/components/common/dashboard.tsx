import { handleGetUserImages } from "@/utils/service/image";
import { getCookie } from "cookies-next";
import { useEffect, useState } from "react";
import Card from "./card";
import { UUID } from "crypto";

interface DashboardProps {
  type: string;
}

export default function Dashboard({ type }: DashboardProps) {
  const [data, setData] = useState<any[]>([]);
  useEffect(() => {
    const request = {
      data: {},
      type: "get",
      url: `/${type}/`,
    };
    const response = handleGetUserImages(request).then((resp) => {
      setData(resp.data);
    });
  }, [type]);

  const handleClick = (id: number | UUID) => {};

  return (
    <>
      {data.map((item, index) => {
        <Card
          key={item.id}
          title={item.name}
          handleClick={() => handleClick(item.id)}
          buttonText={`Create ${type.slice(0, -1)}`}
        />;
      })}
    </>
  );
}
