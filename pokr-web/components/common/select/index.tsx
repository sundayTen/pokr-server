import React from 'react';
import styles from '@components/common/select/Select.module.scss';

interface SelectProps {
  value: string;
  setValue: React.Dispatch<React.SetStateAction<string>>;
  options: any;
  defaultValue?: string | number | readonly string[] | undefined;
}

const Select = (props: SelectProps) => {
  const { value, setValue, options, defaultValue = '' } = props;

  return (
    <select
      className={styles.root}
      onChange={(e: React.ChangeEvent<HTMLSelectElement>) =>
        setValue(e.target.value)
      }
      defaultValue={defaultValue}
      value={value}
    >
      {options.map((option: any, index: number) => (
        <option value={option} key={index}>
          {option}
        </option>
      ))}
    </select>
  );
};

export default Select;
