import pytest
import pandas
import os
import sys
parent_dir = os.path.abspath("..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject2

@pytest.mark.parametrize('petrel_context', [(petrel_version, pythontooltestproject2)], indirect=['petrel_context'])
class TestPointSets_set_values_df:

    def test_pointset_set_values_df(self, pointset_custom_property_units):
        ps = pointset_custom_property_units
        ps.readonly = False
        orig_dataframe = ps.as_dataframe()

        df = ps.as_dataframe()
        df.loc[0, 'Vp time (2)'] = 999
        ps.set_values(df)

        assert ps.as_dataframe().loc[0, 'Vp time (2)'] == 999

        ps.set_values(orig_dataframe)

    def test_pointset_set_values_df_attribute_not_exists(self, pointset_custom_property_units):
        ps = pointset_custom_property_units
        ps.readonly = False
        orig_dataframe = ps.as_dataframe()

        df = ps.as_dataframe()
        df.loc[0, 'Vp time (3)'] = 999
        ps.set_values(df)

        assert 'Vp time (3)' in df.columns
        assert not 'Vp time (3)' in ps.as_dataframe().columns

        ps.set_values(orig_dataframe)

    def test_pointset_set_values_df_create(self, cloned_pointset_custom_property_units):
        ps = cloned_pointset_custom_property_units
        ps.readonly = False

        df = ps.as_dataframe()
        df['Dip salsa'] = df['Dip angle']
        df.loc[0, 'Dip salsa'] = 999
        ps.set_values(df, create=['Dip salsa'])

        df_after = ps.as_dataframe()
        assert 'Dip salsa' in df_after.columns
        assert df_after.loc[0, 'Dip salsa'] == 999

    def test_pointset_set_values_df_create_attribute_exists(self, cloned_pointset_custom_property_units):
        ps = cloned_pointset_custom_property_units
        ps.readonly = False

        df = ps.as_dataframe()
        num_cols_before = len(df.columns)
        df.loc[0, 'Dip angle'] = 999
        ps.set_values(df, create=['Dip angle'])

        df_after = ps.as_dataframe()
        assert 'Dip angle' in df_after.columns
        assert len(df_after.columns) == num_cols_before
        assert df_after.loc[0, 'Dip angle'] == 999

    def test_pointset_set_values_df_includes_units_True(self, pointset_custom_property_units):
        ps = pointset_custom_property_units
        ps.readonly = False
        orig_dataframe = ps.as_dataframe()

        df = ps.as_dataframe(show_units=True)
        df.loc[0, 'Vp time (2) [m/s]'] = 999
        ps.set_values(df, df_includes_units=True)

        assert 'Vp time (2) [m/s]' in df.columns
        assert ps.as_dataframe(show_units=True).loc[0, 'Vp time (2) [m/s]'] == 999

        ps.set_values(orig_dataframe)

    def test_pointset_set_values_df_attribute_not_exists_includes_units_True(self, pointset_custom_property_units):
        ps = pointset_custom_property_units
        ps.readonly = False
        orig_dataframe = ps.as_dataframe()

        df = ps.as_dataframe(show_units=True)
        df.loc[0, 'Vp time (3) [m/s]'] = 999
        ps.set_values(df, df_includes_units=True)

        df_columns = df.columns
        assert 'Vp time (3) [m/s]' in df_columns
        cols = ps.as_dataframe(show_units=True).columns
        assert not 'Vp time (3) [m/s]' in cols

        ps.set_values(orig_dataframe)

    def test_pointset_set_values_df_create_includes_units_True(self, cloned_pointset_custom_property_units):

        ps = cloned_pointset_custom_property_units
        ps.readonly  = False
        
        df = ps.as_dataframe(show_units=True)
        df['Vp time (3) [m/s]'] = df['Vp time (2) [m/s]']
        assert 'Vp time (2) [m/s]' in df.columns
        assert 'Vp time (3) [m/s]' in df.columns
        df.loc[0, 'Vp time (3) [m/s]'] = 999
        ps.set_values(df, create = ['Vp time (3) [m/s]'], df_includes_units=True)

        assert 'Vp time (2) [m/s]' in df.columns
        assert 'Vp time (3) [m/s]' in df.columns

        assert 'Vp time (3) [ ]' in ps.as_dataframe(show_units=True).columns

    def test_pointset_set_values_df_create_attribute_exists_includes_units_True(self, cloned_pointset_custom_property_units):
        ps = cloned_pointset_custom_property_units
        ps.readonly = False

        df = ps.as_dataframe(show_units=True)
        num_cols_before = len(df.columns)
        df.loc[0, 'Dip angle [deg]'] = 999
        ps.set_values(df, create=['Dip angle [deg]'], df_includes_units=True)

        df_after = ps.as_dataframe(show_units=True)
        assert 'Dip angle [deg]' in df_after.columns
        assert len(df_after.columns) == num_cols_before
        assert df_after.loc[0, 'Dip angle [deg]'] == 999

@pytest.mark.parametrize('petrel_context', [(petrel_version, pythontooltestproject2)], indirect=['petrel_context'])
class TestPointSets_set_values_series:

    def test_pointset_set_values_series(self, pointset_custom_property_units):
        ps = pointset_custom_property_units
        ps.readonly = False
        orig_dataframe = ps.as_dataframe()

        series = orig_dataframe['Dip angle'].copy()
        assert type(series) == pandas.Series
        series[0] = 999

        ps.set_values(series)
        changed_df = ps.as_dataframe()
        assert changed_df.loc[0, 'Dip angle'] == 999

        ps.set_values(orig_dataframe)

    def test_pointset_set_values_series_attribute_not_exists(self, pointset_custom_property_units):
        ps = pointset_custom_property_units
        ps.readonly = False
        orig_dataframe = ps.as_dataframe()
        
        series = orig_dataframe['Dip angle'].copy()
        assert type(series) == pandas.Series
        series[0] = 999
        series.name = 'Dip salsa'

        ps.set_values(series)
        assert not 'Dip salsa' in ps.as_dataframe().columns 

        ps.set_values(orig_dataframe)

    def test_pointset_set_values_series_create(self, cloned_pointset_custom_property_units):
        ps = cloned_pointset_custom_property_units

        ps.readonly = False
        df = ps.as_dataframe()
        series = df['Dip angle'].copy()
        assert type(series) == pandas.Series
        series[0] = 999
        series.name = 'Dip salsa'

        ps.set_values(series, create=['Dip salsa'])
        
        df_after = ps.as_dataframe()
        assert 'Dip salsa' in df_after.columns
        assert df_after.loc[0, 'Dip salsa'] == 999

    def test_pointset_set_values_series_create_attributes_exists(self, cloned_pointset_custom_property_units):
        ps = cloned_pointset_custom_property_units
        ps.readonly = False

        df = ps.as_dataframe()
        num_cols_before = len(df.columns)
        series = df['Dip angle'].copy()
        assert type(series) == pandas.Series
        series[0] = 999
        
        ps.set_values(series, create=['Dip angle'])
        
        df_after = ps.as_dataframe()
        assert 'Dip angle' in df_after.columns
        assert len(df_after.columns) == num_cols_before
        assert df_after.loc[0, 'Dip angle'] == 999

    def test_pointset_set_values_series_includes_units_True(self, pointset_custom_property_units):
        ps = pointset_custom_property_units
        ps.readonly = False
        orig_dataframe = ps.as_dataframe(show_units=True)

        series = orig_dataframe['Dip angle [deg]'].copy()
        assert type(series) == pandas.Series
        series[0] = 999

        ps.set_values(series, df_includes_units=True)
        assert 'Dip angle [deg]' == series.name

        changed_df = ps.as_dataframe(show_units=True)
        assert changed_df.loc[0, 'Dip angle [deg]'] == 999

        ps.set_values(orig_dataframe, df_includes_units=True)

    def test_pointset_set_values_series_attribute_not_exists_includes_units_True(self, pointset_custom_property_units):
        ps = pointset_custom_property_units
        ps.readonly = False
        orig_dataframe = ps.as_dataframe(show_units=True)
        
        series = orig_dataframe['Dip angle [deg]'].copy()
        assert type(series) == pandas.Series
        series[0] = 999
        series.name = 'Dip salsa [deg]'

        ps.set_values(series, df_includes_units=True)
        assert 'Dip salsa [deg]' == series.name
        assert not 'Dip salsa [deg]' in ps.as_dataframe().columns 

        ps.set_values(orig_dataframe, df_includes_units=True)

    def test_pointset_set_values_series_create_includes_units_True(self, cloned_pointset_custom_property_units):
        ps = cloned_pointset_custom_property_units

        ps.readonly = False
        df = ps.as_dataframe(show_units=True)
        series = df['Dip angle [deg]'].copy()
        assert type(series) == pandas.Series
        series[0] = 999

        series.name = 'Dip salsa [deg]'
        ps.set_values(series, create=['Dip salsa [deg]'], df_includes_units=True)
        assert series.name == 'Dip salsa [deg]'
        df_after = ps.as_dataframe(show_units=True)
        assert 'Dip salsa [ ]' in df_after.columns
        assert df_after.loc[0, 'Dip salsa [ ]'] == 999

    def test_pointset_set_values_series_create_attributes_exists_includes_units_True(self, cloned_pointset_custom_property_units):
        ps = cloned_pointset_custom_property_units
        ps.readonly = False

        df = ps.as_dataframe(show_units=True)
        num_cols_before = len(df.columns)
        series = df['Dip angle [deg]'].copy()
        assert type(series) == pandas.Series
        series[0] = 999
        
        ps.set_values(series, create=['Dip angle [deg]'], df_includes_units=True)
        
        df_after = ps.as_dataframe(show_units=True)
        assert 'Dip angle [deg]' in df_after.columns
        assert len(df_after.columns) == num_cols_before
        assert df_after.loc[0, 'Dip angle [deg]'] == 999
