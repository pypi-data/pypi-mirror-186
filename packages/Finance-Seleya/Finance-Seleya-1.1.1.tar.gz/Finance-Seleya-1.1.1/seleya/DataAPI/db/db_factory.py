# -*- coding: utf-8 -*-
import pdb
import pandas as pd
from sqlalchemy import and_
from seleya.utilities.kd_logger import kd_logger

mapping_name = {
    'GDOveriewFactory': 'gd_overview',
    'GDReviewsFactory': 'gd_reviews',
    'GDELTFeedFactory': 'gdelt_feed',
    'GDELTGEOFactory': 'gdelt_geo',
    'GDELTTimelineToneFactory': 'gdelt_timelinetone',
    'GDELTTimelineVolinfoFactory': 'gdelt_timelinevolinfo',
    'GDELTTimelineVolrawFactory': 'gdelt_timelinevolraw',
    'BDLabelDataFactory': 'bd_label_data',
    'ESGFeedFactory': 'esg_feed',
    'ESGFactorFactory': 'esg_factor'
}


class EngineFactory():

    def create_engine(self, engine_class):
        return engine_class()

    def __init__(self, engine_class):
        self._fetch_engine = self.create_engine(engine_class)

    def name(self):
        return self._fetch_engine.name(self.__name__)

    def customize(self, clause_list, columns=None, method='and'):
        table = self._fetch_engine.name(self.__name__)
        new_list = and_(table.__dict__['flag'] == 1,
                        table.__dict__['flag'].isnot(None))
        indices = self._fetch_engine.show_indexs(self.__name__)
        for clause in clause_list:
            if clause.left.name in indices:
                new_list.append(clause)
            else:
                kd_logger.warning("{0} not indices".format(clause.left.name))
        if len(new_list) <= 2:
            kd_logger.error("unconditional query is not allowed")
            return pd.DataFrame()
        return self._fetch_engine.customize(table=table,
                                            clause_list=new_list,
                                            columns=columns)


class ShowColumnsFactory(EngineFactory):

    def result(self, name):
        return self._fetch_engine.show_cloumns(
            mapping_name[name]) if name in mapping_name else pd.DataFrame(
                columns=['name', 'type'])


class CustomizeFactory(EngineFactory):

    def name(self, name=None):
        return self._fetch_engine.name(name)

    def customize(self, clause_list, name, columns=None, method='and'):
        table = self._fetch_engine.name(name)
        new_list = and_(table.__dict__['flag'] == 1,
                        table.__dict__['flag'].isnot(None))
        indices = self._fetch_engine.show_indexs(name)
        for clause in clause_list:
            if clause.left.name in indices:
                new_list.append(clause)
            else:
                kd_logger.warning("{0} not indices".format(clause.left.name))
        if len(new_list) <= 2:
            kd_logger.error("unconditional query is not allowed")
            return pd.DataFrame()
        return self._fetch_engine.customize(table=table,
                                            clause_list=new_list,
                                            columns=columns)


class CustomFactory(EngineFactory):

    def result(self, query):
        return self._fetch_engine.custom(query)


class GDOveriewFactory(EngineFactory):
    __name__ = 'gd_overview'

    def result(self, codes, key=None, columns=None):
        return self._fetch_engine.gd_overview(codes=codes,
                                              key=key,
                                              columns=columns)


class GDReviewsFactory(EngineFactory):
    __name__ = 'gd_reviews'

    def result(self,
               codes,
               key=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None,
               limit=10,
               pos=0):
        return self._fetch_engine.gd_reviews(codes=codes,
                                             key=key,
                                             begin_date=begin_date,
                                             end_date=end_date,
                                             columns=columns,
                                             freq=freq,
                                             dates=dates,
                                             limit=limit,
                                             pos=pos)


class GDFactorFactory(EngineFactory):
    __name__ = 'gd_factor'

    def result(self,
               codes,
               key=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None):
        return self._fetch_engine.gd_factor(codes=codes,
                                            begin_date=begin_date,
                                            end_date=end_date,
                                            dates=dates,
                                            columns=columns)


class GDDistributionRatingsFactory(EngineFactory):
    __name__ = 'gd_distribution_ratings'

    def result(self, codes=None, key=None, columns=None):
        return self._fetch_engine.gd_distribution_ratings(codes=codes,
                                                          key=key,
                                                          columns=columns)


class GDTrendRatingsFactory(EngineFactory):
    __name__ = 'gd_trend_ratings'

    def result(self,
               codes,
               key=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None):
        return self._fetch_engine.gd_trend_ratings(codes=codes,
                                                   key=key,
                                                   begin_date=begin_date,
                                                   end_date=end_date,
                                                   columns=columns,
                                                   freq=freq,
                                                   dates=dates)


class GDELTToneFactory(EngineFactory):
    __name__ = 'gdelt_tone'

    def result(self,
               codes=None,
               categories=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None):
        return self._fetch_engine.gdelt_tone(codes=codes,
                                             categories=categories,
                                             begin_date=begin_date,
                                             end_date=end_date,
                                             columns=columns,
                                             freq=freq,
                                             dates=dates)


class GDELTVolRawFactory(EngineFactory):
    __name__ = 'gdelt_volraw'

    def result(self,
               codes=None,
               categories=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None):
        return self._fetch_engine.gdelt_volraw(codes=codes,
                                               categories=categories,
                                               begin_date=begin_date,
                                               end_date=end_date,
                                               columns=columns,
                                               freq=freq,
                                               dates=dates)


class GDELTFactorFactory(EngineFactory):
    __name__ = 'gdelt_factor'

    def result(self,
               codes=None,
               categories=None,
               level=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None):
        return self._fetch_engine.gdelt_factor(codes=codes,
                                               categories=categories,
                                               level=level,
                                               begin_date=begin_date,
                                               end_date=end_date,
                                               columns=columns,
                                               freq=freq,
                                               dates=dates)


class BHRFactorFactory(EngineFactory):
    __name__ = 'bhr_factor'

    def result(self,
               codes=None,
               categories=None,
               level=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None):
        return self._fetch_engine.bhr_factor(codes=codes,
                                             categories=categories,
                                             level=level,
                                             begin_date=begin_date,
                                             end_date=end_date,
                                             columns=columns,
                                             freq=freq,
                                             dates=dates)


class RefintivFactorFactory(EngineFactory):
    __name__ = 'refintiv_factor'

    def result(self,
               codes=None,
               categories=None,
               level=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None):
        return self._fetch_engine.refintiv_factor(codes=codes,
                                                  categories=categories,
                                                  level=level,
                                                  begin_date=begin_date,
                                                  end_date=end_date,
                                                  columns=columns,
                                                  freq=freq,
                                                  dates=dates)


class GDELTFeedFactory(EngineFactory):
    __name__ = 'gdelt_feed'

    def result(self,
               codes=None,
               key=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None,
               time_name='publish_time'):
        return self._fetch_engine.gdelt_feed(codes=codes,
                                             key=key,
                                             begin_date=begin_date,
                                             end_date=end_date,
                                             columns=columns,
                                             freq=freq,
                                             dates=dates,
                                             time_name=time_name)


class GDELTFeedFeatureFactory(EngineFactory):
    __name__ = 'gdelt_feed_feature'

    def result(self, codes=None, key=None, columns=None):
        return self._fetch_engine.gdelt_feed_feature(codes=codes,
                                                     key=key,
                                                     columns=columns)


class GDELTFeedSentimentFactory(EngineFactory):
    __name__ = 'gdelt_feed_sentiment'

    def result(self, codes=None, key=None, columns=None):
        return self._fetch_engine.gdelt_feed_sentiment(codes=codes,
                                                       key=key,
                                                       columns=columns)


class RefintivFeedSentimentFactory(EngineFactory):
    __name__ = 'refintiv_feed_sentiment'

    def result(self, codes=None, key=None, columns=None):
        return self._fetch_engine.refintiv_feed_sentiment(codes=codes,
                                                          key=key,
                                                          columns=columns)


class BDLabelDataFactory(EngineFactory):
    __name__ = 'bd_label_data'

    def result(self,
               codes=None,
               key=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None):
        return self._fetch_engine.bd_label_data(codes=codes,
                                                key=key,
                                                begin_date=begin_date,
                                                end_date=end_date,
                                                columns=columns,
                                                freq=freq,
                                                dates=dates)


class BHROveriewFactory(EngineFactory):
    __name__ = 'bhr_overview'

    def result(self, codes, key=None, columns=None):
        return self._fetch_engine.bhr_overview(codes=codes,
                                               key=key,
                                               columns=columns)


class BHRFeedFactory(EngineFactory):
    __name__ = 'bhr_feed'

    def result(self,
               codes=None,
               key=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None,
               time_name='publish_time'):
        return self._fetch_engine.bhr_feed(codes=codes,
                                           key=key,
                                           begin_date=begin_date,
                                           end_date=end_date,
                                           columns=columns,
                                           freq=freq,
                                           dates=dates,
                                           time_name=time_name)


class BHRFeedFeatureFactory(EngineFactory):
    __name__ = 'bhr_feed_feature'

    def result(self, codes=None, key=None, columns=None):
        return self._fetch_engine.bhr_feed_feature(codes=codes,
                                                   key=key,
                                                   columns=columns)


class BHRLabelFactory(EngineFactory):
    __name__ = 'bhr_label'

    def result(self,
               key_name,
               key_value,
               query_name,
               query_values,
               columns=None,
               freq=None):
        return self._fetch_engine.bhr_label(key_name=key_name,
                                            key_value=key_value,
                                            query_name=query_name,
                                            query_values=query_values,
                                            columns=columns,
                                            freq=freq)


class RefintivFeedFactory(EngineFactory):
    __name__ = 'refintiv_feed'

    def result(self,
               codes=None,
               key=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None,
               time_name='publish_time'):
        return self._fetch_engine.refintiv_feed(codes=codes,
                                                key=key,
                                                begin_date=begin_date,
                                                end_date=end_date,
                                                columns=columns,
                                                freq=freq,
                                                dates=dates,
                                                time_name=time_name)


class RefintivFeedFeatureFactory(EngineFactory):
    __name__ = 'refintiv_feed_feature'

    def result(self, codes=None, key=None, columns=None):
        return self._fetch_engine.refintiv_feed_feature(codes=codes,
                                                        key=key,
                                                        columns=columns)


class RefintiveESGCategory(EngineFactory):
    __name__ = 'refintiv_esg_category'

    def result(self, codes=None, key=None, columns=None):
        return self._fetch_engine.refintiv_esg_category(codes=codes,
                                                        key=key,
                                                        columns=columns)


class BHRCategoryMappingFactory(EngineFactory):
    __name__ = 'bhr_category_mapping'

    def result(self, name=None, columns=None):
        return self._fetch_engine.bhr_category_mapping(name=name,
                                                       columns=columns)


class CompanyFactory(EngineFactory):
    __name__ = 'company'

    def result(self, codes=None, primary=[1], key=None, columns=None):
        return self._fetch_engine.company(codes=codes,
                                          primary=primary,
                                          key=key,
                                          columns=columns)


class IndustryFactory(EngineFactory):
    __name__ = 'industry'

    def result(self, codes=None, key=None, category='GICS', columns=None):
        return self._fetch_engine.industry(codes=codes,
                                           key=key,
                                           category=category,
                                           columns=columns)


class IndexComponentsFactory(EngineFactory):
    __name__ = 'index_components'

    def result(self, codes=None, key=None, category='sp500', columns=None):
        return self._fetch_engine.index_components(codes=codes,
                                                   key=key,
                                                   category=category,
                                                   columns=columns)


class ESGFactorLevel0Factory(EngineFactory):
    __name__ = 'esg_factor_level0'


class ESGFactorLevel1Factory(EngineFactory):
    __name__ = 'esg_factor_level1'


class ESGFactorLevel2Factory(EngineFactory):
    __name__ = 'esg_factor_level2'


class ESGFactorFactory(EngineFactory):
    __name__ = 'esg_factor'

    def result(self,
               codes=None,
               categories=None,
               level=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None):
        return self._fetch_engine.esg_factor(codes=codes,
                                             categories=categories,
                                             level=level,
                                             begin_date=begin_date,
                                             end_date=end_date,
                                             columns=columns,
                                             freq=freq,
                                             dates=dates)


class ESGTargetFactory(EngineFactory):
    __name__ = 'esg_target'

    def result(self,
               codes,
               category,
               begin_date=None,
               end_date=None,
               columns=None):
        return self._fetch_engine.esg_target(codes=codes,
                                             category=category,
                                             begin_date=begin_date,
                                             end_date=end_date,
                                             columns=columns)


class BDGlassdoorRatingFactory(EngineFactory):
    __name__ = 'bd_glassdoors_rating'

    def result(self,
               codes=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None):
        return self._fetch_engine.bd_glassdoors_rating(codes=codes,
                                                       begin_date=begin_date,
                                                       end_date=end_date,
                                                       columns=columns,
                                                       freq=freq,
                                                       dates=dates)


class ESGFeedFactory(EngineFactory):
    __name__ = 'esg_feed'

    def result(self,
               codes=None,
               categories=None,
               key='category',
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None,
               limit=10,
               pos=0):
        return self._fetch_engine.esg_feed(codes=codes,
                                           categories=categories,
                                           key=key,
                                           begin_date=begin_date,
                                           end_date=end_date,
                                           columns=columns,
                                           freq=freq,
                                           dates=dates,
                                           limit=limit,
                                           pos=pos)


class ESGMetricsFactory(EngineFactory):
    __name__ = 'esg_metrics'

    def result(self,
               codes=None,
               key=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None,
               time_name='date'):
        return self._fetch_engine.esg_metrics(codes=codes,
                                              key=key,
                                              begin_date=begin_date,
                                              end_date=end_date,
                                              columns=columns,
                                              freq=freq,
                                              dates=dates,
                                              time_name=time_name)


class ESGMetrticsDataFactory(EngineFactory):
    __name__ = 'esg_metrics_data'

    def result(self,
               category,
               codes=None,
               key=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None,
               time_name='date'):
        return self._fetch_engine.esg_metrics_data(codes=codes,
                                                   key=key,
                                                   table_name=category,
                                                   begin_date=begin_date,
                                                   end_date=end_date,
                                                   columns=columns,
                                                   freq=freq,
                                                   dates=dates,
                                                   time_name=time_name)


class ESGIndicatorLevel0Factory(EngineFactory):
    __name__ = 'esg_indicator_level0'


class ESGIndicatorLevel1Factory(EngineFactory):
    __name__ = 'esg_indicator_level1'


class ESGMetrticsIndicatorFactory(EngineFactory):
    __name__ = 'esg_metrics_indicator'

    def result(self,
               codes=None,
               name=None,
               begin_date=None,
               end_date=None,
               columns=None):
        return self._fetch_engine.esg_metrics_indicator(codes=codes,
                                                        name=name,
                                                        begin_date=begin_date,
                                                        end_date=end_date,
                                                        columns=columns)


class ESGDetailFactory(EngineFactory):
    __name__ = 'esg_detail'

    def result(self, classify=None, category=None, level=None, columns=None):
        return self._fetch_engine.esg_detail(classify=classify,
                                             category=category,
                                             level=level,
                                             columns=columns)


class ESGMetricsDetailFactory(EngineFactory):
    __name__ = 'esg_metrics_detail'

    def result(self, codes=None, key='columns_name', columns=None):
        return self._fetch_engine.esg_metrics_detail(codes=codes,
                                                     key=key,
                                                     columns=columns)


class CorporateLeadershipFactory(EngineFactory):
    __name__ = 'corporate_leadership_rating'

    def result(self,
               codes=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None):
        return self._fetch_engine.corporate_leadership_rating(
            codes=codes,
            level=level,
            begin_date=begin_date,
            end_date=end_date,
            columns=columns,
            freq=freq,
            dates=dates)


class UserCorporateLeadershipFactory(EngineFactory):
    __name__ = 'user_model_rating'

    def result(self,
               codes=None,
               uid=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None):
        return self._fetch_engine.user_model_rating(
            tabel_name='user_corporate_leadership_rating',
            codes=codes,
            uid=uid,
            begin_date=begin_date,
            end_date=end_date,
            columns=columns,
            freq=freq,
            dates=dates)


class UserBusinessSustainabilityFactory(EngineFactory):
    __name__ = 'user_model_rating'

    def result(self,
               codes=None,
               uid=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None):
        return self._fetch_engine.user_model_rating(
            tabel_name='user_business_sustainability_rating',
            codes=codes,
            uid=uid,
            begin_date=begin_date,
            end_date=end_date,
            columns=columns,
            freq=freq,
            dates=dates)


class UserBusinessModelFactory(EngineFactory):
    __name__ = 'user_model_rating'

    def result(self,
               codes=None,
               uid=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None):
        return self._fetch_engine.user_model_rating(
            tabel_name='user_business_model_rating',
            codes=codes,
            uid=uid,
            begin_date=begin_date,
            end_date=end_date,
            columns=columns,
            freq=freq,
            dates=dates)


class CorporateLeadershipFactory(EngineFactory):
    __name__ = 'bd_model_rating'

    def result(self,
               codes=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None):
        return self._fetch_engine.bd_model_rating(
            tabel_name='corporate_leadership_rating',
            codes=codes,
            begin_date=begin_date,
            end_date=end_date,
            columns=columns,
            freq=freq,
            dates=dates)


class BusinessSustainabilityFactory(EngineFactory):
    __name__ = 'bd_model_rating'

    def result(self,
               codes=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None):
        return self._fetch_engine.bd_model_rating(
            tabel_name='business_sustainability_rating',
            codes=codes,
            begin_date=begin_date,
            end_date=end_date,
            columns=columns,
            freq=freq,
            dates=dates)


class BusinessModelFactory(EngineFactory):
    __name__ = 'bd_model_rating'

    def result(self,
               codes=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None):
        return self._fetch_engine.bd_model_rating(
            tabel_name='business_model_rating',
            codes=codes,
            begin_date=begin_date,
            end_date=end_date,
            columns=columns,
            freq=freq,
            dates=dates)


class BDCountFactory(EngineFactory):
    __name__ = 'bd_count'

    def result(self,
               codes=None,
               begin_date=None,
               end_date=None,
               columns=None,
               freq=None,
               dates=None):
        return self._fetch_engine.bd_count(codes=codes,
                                           begin_date=begin_date,
                                           end_date=end_date,
                                           columns=columns,
                                           freq=freq,
                                           dates=dates)


class ESGLogicalFactory(EngineFactory):
    __name__ = 'esg_logical'

    def result(self, codes=None, key='columns_name', columns=None):
        return self._fetch_engine.esg_logical(codes=codes,
                                              key=key,
                                              columns=columns)


class SASBMetricsFactory(EngineFactory):
    __name__ = 'sasb_metrics'

    def result(self, codes, column_name, begin_date, end_date):
        return self._fetch_engine.sasb_metrics(codes=codes,
                                               column_name=column_name,
                                               begin_date=begin_date,
                                               end_date=end_date)


SASBMetrics = SASBMetricsFactory


class SASBMapdomFactory(EngineFactory):
    __name__ = 'sasb_mapdom'

    def result(self, codes, key, values):
        return self._fetch_engine.sasb_mapdom(codes=codes,
                                              key=key,
                                              values=values)


SASBMapdom = SASBMapdomFactory


class SASBRelationshipFactory(EngineFactory):
    __name__ = 'sasb_relationship'

    def result(self, codes):
        return self._fetch_engine.sasb_relationship(codes=codes)


SASBRelationship = SASBRelationshipFactory


class ESGSummaryFactory(EngineFactory):
    __name__ = 'esg_summary'

    def result(self, codes=None, key=None, level=None, columns=None):
        return self._fetch_engine.esg_summary(codes=codes,
                                              key=key,
                                              level=level,
                                              columns=columns)


ESGSummary = ESGSummaryFactory


class UltronGentic(EngineFactory):

    def result(self, rootid=None, fitness=None, classify=None, columns=None):
        return self._fetch_engine.ultron_gentic(rootid=rootid,
                                                fitness=fitness,
                                                classify=classify,
                                                columns=columns)


class UsersFactory(EngineFactory):

    def result(self, codes=None, key='id', columns=None):
        return self._fetch_engine.users(codes=codes, key=key, columns=columns)


class CNMarketDaily(EngineFactory):

    def result(self,
               codes=None,
               key=None,
               is_adj_before=True,
               begin_date=None,
               end_date=None,
               dates=None,
               columns=None):
        return self._fetch_engine.cn_market_daily(codes=codes,
                                                  key=key,
                                                  is_adj_before=is_adj_before,
                                                  begin_date=begin_date,
                                                  end_date=end_date,
                                                  columns=columns,
                                                  dates=dates)


class HKMarketDaily(EngineFactory):

    def result(self,
               codes=None,
               key=None,
               is_adj_before=True,
               begin_date=None,
               end_date=None,
               dates=None,
               columns=None):
        return self._fetch_engine.hk_market_daily(codes=codes,
                                                  key=key,
                                                  is_adj_before=is_adj_before,
                                                  begin_date=begin_date,
                                                  end_date=end_date,
                                                  columns=columns,
                                                  dates=dates)


class USMarketDaily(EngineFactory):

    def result(self,
               codes=None,
               key=None,
               is_adj_before=False,
               begin_date=None,
               end_date=None,
               dates=None,
               columns=None):
        return self._fetch_engine.us_market_daily(codes=codes,
                                                  key=key,
                                                  is_adj_before=is_adj_before,
                                                  begin_date=begin_date,
                                                  end_date=end_date,
                                                  columns=columns,
                                                  dates=dates)
