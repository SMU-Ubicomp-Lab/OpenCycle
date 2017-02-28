# Data dictionary

---

The data can be split hierarchically into levels. Menstrual cycles are collected into 'groups' of consecutive cycles. All the groups together pertain to a single woman ('Donna' in Italian).

- `DONNA` (`ID`): unique identifier for each woman
- `P_SPEZZ` (`GROUP_ID`): identifier for a woman's set of consecutive cycles
- `T_SPEZZ` (`N_GROUPS`): the number of consecutive cycles in this group
- `P_CICLO` (`CYCLE_ID`): identifier within a cycle group
- `T_CICLI` (`N_CYCLES`): number of cycles
- `ANN_NAS` (`BIRTH_YR`): year of birth
- `DATA` (`DATE`): date of first day of menstrual cycle
- `QUALIFI` (`DESC`): any special code. See VARLONDON for the data set.
- `L_CICLO`: time span for cycle
- `L_PREOV`: num days before BBT (basal body temperature) rises
- `L_PERIOD`: length of menstruation, days
- `TEMP1`–`TEMP99`: temperature