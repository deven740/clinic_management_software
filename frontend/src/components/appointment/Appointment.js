import React, { useEffect, useState } from "react";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";
import Autocomplete from "@mui/material/Autocomplete";
import TextField from "@mui/material/TextField";
import Title from "../dashboard/Title";
import axiosApiInstance from "../../AxiosInstancs";
import axios from "axios";

const backendURL = process.env.REACT_APP_BACKEND_URL;

console.log(process.env.REACT_APP_BACKEND_URL);

export default function BoxSx() {
  const [selectedSpecialty, setSelectedSpecialty] = useState("");
  const [specialtyTypes, setSpecialtyTypes] = useState([
    { id: null, label: "" },
  ]);

  const handleChangeSpecialty = (e) => {
    console.log(e.target.value);
  };

  useEffect(() => {
    const fetchSpecialty = async (e) => {
      try {
        const response = await axios.get(`${backendURL}/specialty`);
        const responseData = response.data;
        const resultArray = responseData.map((elm) => ({
          id: elm.id,
          label: elm.specialty.toUpperCase(),
        }));

        setSpecialtyTypes(resultArray);
      } catch (err) {
        console.log(err.response);
      }
    };

    fetchSpecialty();
  }, []);

  useEffect(() => {
    console.log("changed");
    return () => {};
  }, [selectedSpecialty]);

  const onChangeSpecialty = (event, newValue) => {
    console.log(newValue);
    setSelectedSpecialty(newValue);
  };

  return (
    <Grid container spacing={2}>
      <Grid item xs={8}>
        {/* <Item>xs=8</Item> */}
        <Autocomplete
          disablePortal
          id="combo-box-demo"
          options={specialtyTypes}
          sx={{ width: 300 }}
          renderInput={(params) => (
            <TextField {...params} label="Select Specialty" />
          )}
          onChange={onChangeSpecialty}
        />
      </Grid>
    </Grid>
  );
}
