import pytest

import numpy as np
import reciprocalspaceship as rs
import tensorflow as tf

from scipy.stats import pearsonr
from SFC_TF.Fmodel import SFcalculator


@pytest.mark.parametrize("case", [1, 2])
def test_constructor_SFcalculator(data_pdb, data_mtz_exp, case):
    if case == 1:
        sfcalculator = SFcalculator(
            data_pdb, mtzfile_dir=data_mtz_exp, set_experiment=True)
        assert len(sfcalculator.HKL_array) == 22230
        assert len(sfcalculator.Hasu_array) == 22303
    else:
        sfcalculator = SFcalculator(
            data_pdb, mtzfile_dir=None, dmin=1.5, set_experiment=True)
        assert sfcalculator.HKL_array is None
        assert len(sfcalculator.Hasu_array) == 10239
    assert len(sfcalculator.atom_name) == 1492


def test_inspect_data(data_pdb, data_mtz_exp):
    sfcalculator = SFcalculator(
        data_pdb, mtzfile_dir=data_mtz_exp, set_experiment=True)
    sfcalculator.inspect_data()
    assert sfcalculator.inspected
    assert np.isclose(sfcalculator.solventpct, 11.1, atol=0.5)
    assert sfcalculator.gridsize == [80, 120, 144]


def test_inspect_data_nomtz(data_pdb):
    sfcalculator = SFcalculator(
        data_pdb, mtzfile_dir=None, dmin=1.5, set_experiment=True)
    sfcalculator.inspect_data()
    assert sfcalculator.inspected
    assert np.isclose(sfcalculator.solventpct, 11.1, atol=0.5)
    assert sfcalculator.gridsize == [60, 90, 108]


@pytest.mark.parametrize("Return", [True, False])
def test_calc_Fprotein(data_pdb, data_mtz_exp, data_mtz_fmodel_ksol0, Return):
    sfcalculator = SFcalculator(
        data_pdb, mtzfile_dir=data_mtz_exp, set_experiment=True)
    sfcalculator.inspect_data()
    Fprotein = sfcalculator.Calc_Fprotein(Return=Return)
    Fcalc = rs.read_mtz(data_mtz_fmodel_ksol0)
    assert (Fcalc.get_hkls() == sfcalculator.HKL_array).all()

    if Return:
        Fprotein_arr = Fprotein.numpy()
        try:
            assert pearsonr(np.abs(Fprotein_arr),
                            Fcalc['FMODEL'].to_numpy()).statistic > 0.99
        except:
            assert pearsonr(np.abs(Fprotein_arr),
                            Fcalc['FMODEL'].to_numpy())[0] > 0.99
    else:
        assert Fprotein is None
        Fprotein_arr = sfcalculator.Fprotein_HKL.numpy()
        try:
            assert pearsonr(np.abs(Fprotein_arr),
                            Fcalc['FMODEL'].to_numpy()).statistic > 0.99
        except:
            assert pearsonr(np.abs(Fprotein_arr),
                            Fcalc['FMODEL'].to_numpy())[0] > 0.99


@pytest.mark.parametrize("Return", [True, False])
def test_calc_Fsolvent(data_pdb, data_mtz_exp, data_mtz_fmodel_ksol0, data_mtz_fmodel_ksol1, Return):
    sfcalculator = SFcalculator(
        data_pdb, mtzfile_dir=data_mtz_exp, set_experiment=True)
    sfcalculator.inspect_data()
    sfcalculator.Calc_Fprotein(Return=False)
    Fsolvent = sfcalculator.Calc_Fsolvent(
        dmin_mask=6.0, dmin_nonzero=3.0, Return=Return)

    Fcalc = rs.read_mtz(data_mtz_fmodel_ksol0)
    Fmodel = rs.read_mtz(data_mtz_fmodel_ksol1)
    assert (Fmodel.get_hkls() == sfcalculator.HKL_array).all()

    calc_mag = Fcalc['FMODEL'].to_numpy()
    calc_ph = np.deg2rad(Fcalc['PHIFMODEL'].to_numpy())
    Fcalc_complex = np.array([complex(mag*np.cos(ph), mag*np.sin(ph))
                              for mag, ph in zip(calc_mag, calc_ph)])

    model_mag = Fmodel['FMODEL'].to_numpy()
    model_ph = np.deg2rad(Fmodel['PHIFMODEL'].to_numpy())
    Fmodel_complex = np.array([complex(mag*np.cos(ph), mag*np.sin(ph))
                               for mag, ph in zip(model_mag, model_ph)])

    Fmask_complex = Fmodel_complex - Fcalc_complex

    if Return:
        Fsolvent_arr = Fsolvent.numpy()
        try:
            assert pearsonr(np.abs(Fsolvent_arr), np.abs(
                Fmask_complex)).statistic > 0.95
        except:
            assert pearsonr(np.abs(Fsolvent_arr), np.abs(
                Fmask_complex))[0] > 0.95
    else:
        assert Fsolvent is None
        Fsolvent_arr = sfcalculator.Fmask_HKL.numpy()
        try:
            assert pearsonr(np.abs(Fsolvent_arr), np.abs(
                Fmask_complex)).statistic > 0.95
        except:
            assert pearsonr(np.abs(Fsolvent_arr), np.abs(
                Fmask_complex))[0] > 0.95


@pytest.mark.parametrize("case", [1, 2])
def test_calc_Ftotal(data_pdb, data_mtz_exp, case):
    if case == 1:
        sfcalculator = SFcalculator(
            data_pdb, mtzfile_dir=data_mtz_exp, set_experiment=True)
        sfcalculator.inspect_data()
        sfcalculator.Calc_Fprotein(Return=False)
        sfcalculator.Calc_Fsolvent(
            dmin_mask=6.0, dmin_nonzero=3.0, Return=False)
        Ftotal = sfcalculator.Calc_Ftotal()
        assert len(Ftotal) == 22230
    else:
        sfcalculator = SFcalculator(
            data_pdb, mtzfile_dir=None, dmin=1.5, set_experiment=True)
        sfcalculator.inspect_data()
        sfcalculator.Calc_Fprotein(Return=False)
        sfcalculator.Calc_Fsolvent(
            dmin_mask=6.0, dmin_nonzero=3.0, Return=False)
        Ftotal = sfcalculator.Calc_Ftotal()
        assert len(Ftotal) == 10239


@pytest.mark.parametrize("partition_size", [1, 4, 5, 20])
def test_calc_Fprotein_batch(data_pdb, data_mtz_exp, partition_size):
    sfcalculator = SFcalculator(
        data_pdb, mtzfile_dir=data_mtz_exp, set_experiment=True)
    sfcalculator.inspect_data()
    Fprotein = sfcalculator.Calc_Fprotein(Return=True)
    atoms_pos_batch = tf.repeat(sfcalculator.atom_pos_orth[None,...], 10, axis=0)
    Fprotein_batch = sfcalculator.Calc_Fprotein_batch(
        atoms_pos_batch, Return=True, PARTITION=partition_size)

    assert len(Fprotein_batch) == 10
    assert np.all(np.isclose(tf.math.abs(Fprotein_batch[5]).numpy(), 
                             tf.math.abs(Fprotein).numpy(), 
                             rtol=1e-3, atol=1e1))
    assert np.all(np.isclose(tf.math.abs(sfcalculator.Fprotein_asu_batch[5]).numpy(), 
                             tf.math.abs(sfcalculator.Fprotein_asu).numpy(), 
                             rtol=1e-3, atol=1e1))


@pytest.mark.parametrize("partition_size", [1, 4, 5, 20])
def test_calc_Fsolvent_batch(data_pdb, data_mtz_exp, partition_size):
    sfcalculator = SFcalculator(
        data_pdb, mtzfile_dir=data_mtz_exp, set_experiment=True)
    sfcalculator.inspect_data()
    sfcalculator.Calc_Fprotein(Return=False)
    Fsolvent = sfcalculator.Calc_Fsolvent(
        dmin_mask=6.0, dmin_nonzero=3.0, Return=True)

    atoms_pos_batch = tf.repeat(sfcalculator.atom_pos_orth[None,...], 10, axis=0)
    sfcalculator.Calc_Fprotein_batch(
        atoms_pos_batch, Return=False, PARTITION=partition_size)
    Fsolvent_batch = sfcalculator.Calc_Fsolvent_batch(
        dmin_mask=6.0, dmin_nonzero=3.0, Return=True, PARTITION=partition_size)

    assert len(Fsolvent_batch) == 10
    assert np.all(np.isclose(tf.math.abs(Fsolvent).numpy(),
                             tf.math.abs(Fsolvent_batch[3]).numpy(),
                             rtol=1e-2, atol=1e2))


def test_calc_Ftotal_batch(data_pdb, data_mtz_exp):
    sfcalculator = SFcalculator(
        data_pdb, mtzfile_dir=data_mtz_exp, set_experiment=True)
    sfcalculator.inspect_data()
    atoms_pos_batch = tf.repeat(sfcalculator.atom_pos_orth[None,...], 10, axis=0)

    sfcalculator.Calc_Fprotein(Return=False)
    sfcalculator.Calc_Fsolvent(
        dmin_mask=6.0, dmin_nonzero=3.0, Return=False)
    sfcalculator.Calc_Fprotein_batch(atoms_pos_batch, Return=False)
    sfcalculator.Calc_Fsolvent_batch(
        dmin_mask=6.0, dmin_nonzero=3.0, Return=False)

    kaniso = tf.constant(
        [-1.2193, -0.5417, -0.6066,  0.8886,  1.1478, -1.6649], dtype=tf.float32)
    Ftotal = sfcalculator.Calc_Ftotal(kaniso=kaniso)
    Ftotal_batch = sfcalculator.Calc_Ftotal_batch(kaniso=kaniso)

    assert np.all(np.isclose(tf.math.abs(Ftotal_batch[8]).numpy(),
                             tf.math.abs(Ftotal).numpy(),
                             rtol=1e1, atol=1e2))


def test_prepare_Dataset(data_pdb, data_mtz_exp):
    sfcalculator = SFcalculator(
        data_pdb, mtzfile_dir=data_mtz_exp, set_experiment=True)
    sfcalculator.inspect_data()

    sfcalculator.Calc_Fprotein(Return=False)
    sfcalculator.Calc_Fsolvent(
        dmin_mask=6.0, dmin_nonzero=3.0, Return=False)
    sfcalculator.Calc_Ftotal()
    ds = sfcalculator.prepare_DataSet("HKL_array", "Ftotal_HKL")
    assert len(ds) == 22230
