import React, { useEffect, useState } from "react";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";
import Autocomplete from "@mui/material/Autocomplete";
import TextField from "@mui/material/TextField";
import Title from "../dashboard/Title";
import axiosApiInstance from "../../AxiosInstancs";
import axios from "axios";
import { format, addDays, parseISO } from "date-fns";
import FullWidthTabs from "../tabs/Tabs";

const backendURL = process.env.REACT_APP_BACKEND_URL;

export default function BoxSx() {
  const emptyOptionsArray = [{ id: null, label: "" }];
  const [selectedSpecialty, setSelectedSpecialty] = useState(null);
  const [specialtyTypes, setSpecialtyTypes] = useState(emptyOptionsArray);
  const [doctorsOptions, setDoctorsOptions] = useState(emptyOptionsArray);
  const [clearInput, setClearInput] = useState(true);
  const [disabled, setDisabled] = useState(true);
  const [doctor, setDoctor] = useState(null);
  const [date, setDate] = useState(format(new Date(), "yyyy-MM-dd"));
  const [slotsArray, setSlotsArray] = useState(null);

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
    if (!selectedSpecialty) return;
    const fetchDoctorsBySpecialty = async (e) => {
      try {
        const response = await axios.get(
          `${backendURL}/specialty/filter-doctors-by-specialty`,
          { params: { specialty: selectedSpecialty.label.toLowerCase() } }
        );
        const responseData = response.data;
        const resultArray = responseData.map((elm) => ({
          id: elm.details_id,
          label: elm.full_name.toUpperCase(),
        }));

        setDoctorsOptions(resultArray);
        setDisabled(false);
      } catch (err) {
        console.log(err);
      }
    };

    fetchDoctorsBySpecialty();
    return () => {};
  }, [selectedSpecialty]);

  const onChangeSpecialty = (event, newValue) => {
    setDoctorsOptions(emptyOptionsArray);
    setClearInput(!clearInput);
    setSelectedSpecialty(newValue);
    setDisabled(true);
    setDoctor(null);
  };

  const onChangeDoctor = (event, newValue) => {
    if (!newValue) {
      console.log(newValue);
      setDoctor(newValue);
      return;
    }
    setDoctor(newValue);
    const data = {
      appointment_date: date,
      doctor_id: newValue.id,
    };
    const fetchAppointmentsByDateAndDoctor = async (e) => {
      try {
        const response = await axios.post(
          `${backendURL}/appointments/filter-appointments-by-doctor-and-date`,
          data
        );
        const responseData = response.data;
        console.log(responseData);
        // const resultArray = responseData.map((elm) => ({
        //   id: elm.details_id,
        //   label: elm.full_name.toUpperCase(),
        // }));
      } catch (err) {
        console.log(err);
      }
    };
    fetchAppointmentsByDateAndDoctor();
  };

  // useEffect(() => {
  //   if (!doctor) return;

  //   console.log("effect ran");

  //   return () => {};
  // }, [doctor]);

  return (
    <Grid container spacing={2}>
      <Grid item xs={8}>
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
      <Grid item xs={8}>
        <Autocomplete
          disablePortal
          id="combo-box-demo-2"
          getOptionLabel={(doctorsOptions) => doctorsOptions.label}
          options={doctorsOptions}
          sx={{ width: 300 }}
          renderOption={(props, doctorsOptions) => (
            <Box component="li" {...props} key={doctorsOptions.id}>
              {doctorsOptions.label}
            </Box>
          )}
          renderInput={(params) => (
            <TextField {...params} label="Select Doctor" />
          )}
          key={clearInput}
          disabled={disabled}
          onChange={onChangeDoctor}
        />
      </Grid>
      {doctor ? (
        <Grid item xs={12}>
          <FullWidthTabs doctorID={doctor} />
        </Grid>
      ) : (
        ""
      )}
    </Grid>
  );
}
